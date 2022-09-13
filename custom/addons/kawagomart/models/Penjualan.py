from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Penjualan(models.Model):
    _name = 'kawagomart.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='No. Penjualan')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tanggal Penjualan', default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Bayar', compute='_compute_totalbayar')

    detailpenjualan_ids = fields.One2many(
        comodel_name='kawagomart.detailpenjualan', inverse_name='penjualan_id', string='Detail Penjualan')  # noqa

    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Confirm'),  ('done', 'Done'),
                                                            ('cancel', 'Cancel'), ], required=True, readonly=True, copy=False, tracking=True, default='draft')

    @api.onchange('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = self.env['kawagomart.detailpenjualan'].search(  # noqa
                [('penjualan_id', '=', rec.id)]).mapped('subtotal')  # noqa
            rec.total_bayar = sum(a)

    # penggunaan untuk odoo 15
    @api.ondelete(at_uninstall=False)
    def _ondelete_penjualan(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError(
                'You can only delete draft penjualan')
        else:
            pass
        if self.detailpenjualan_ids:
            a = []
            for rec in self:
                a = self.env['kawagomart.detailpenjualan'].search(  # noqa
                    [('penjualan_id', '=', rec.id)])
                # print(a) # for debugging
            for ob in a:
                # print(str(ob.barang_id.name) + ' ' + str(ob.qty)) # for debugging # noqa
                ob.barang_id.stok += ob.qty

    # # untuk odoo 14 ke bawah
    # def unlink(self):
    #     if self.detailpenjualan_ids:
    #         a = []
    #         for rec in self:
    #             a = self.env['kawagomart.detailpenjualan'].search(  # noqa
    #                 [('penjualan_id', '=', rec.id)])
    #             # print(a) # for debugging
    #         for ob in a:
    #             # print(str(ob.barang_id.name) + ' ' + str(ob.qty)) # for debugging # noqa
    #             ob.barang_id.stok += ob.qty
    #     record = super(Penjualan, self).unlink()
    #     return record

    def write(self, vals):
        for rec in self:
            a = self.env['kawagomart.detailpenjualan'].search(  # noqa
                    [('penjualan_id', '=', rec.id)])
            print(a)
            for data in a:
                # print(str(data.barang_id.name) +str(data.qty) + str(data.barang_id.stock))
                data.barang_id.stok += data.qty
        record = super(Penjualan, self).write(vals)
        for rec in self:
            b = self.env['kawagomart.detailpenjualan'].search(  # noqa
                    [('penjualan_id', '=', rec.id)])
            print(b)
            for databaru in b:
                if databaru in a:
                    # print(str(data.barang_id.name) +str(data.qty) + str(data.barang_id.stock))
                    data.barang_id.stok -= databaru.qty
                else:
                    pass
        return record

    # _sql_constraints = [
    #     ('name_unique', 'UNIQUE(name)', 'No. Penjualan tidak boleh sama')]

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            a = []
            a = self.env['kawagomart.penjualan'].search(
                [('name', '=', self.name)]).mapped('name')
            b = len(a)
            if b > 1:
                if rec.name in a:
                    raise ValidationError('No. Penjualan tidak boleh sama !!')

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def action_draft(self):
        self.write({'state': 'draft'})


class DetailPenjualan(models.Model):
    _name = 'kawagomart.detailpenjualan'
    _description = 'Detail Penjualan'

    name = fields.Char(string='Nama Barang')
    penjualan_id = fields.Many2one(
        comodel_name='kawagomart.penjualan', string='Detail Penjualan')
    barang_id = fields.Many2one(
        comodel_name='kawagomart.barang', string='List Barang')
    harga_satuan = fields.Integer(string='Harga Satuan',)
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.harga_satuan * rec.qty

    @api.onchange('barang_id')
    def _onchange_barang_id(self):
        if (self.barang_id.harga_jual):
            self.harga_satuan = self.barang_id.harga_jual

    # @api.onchange('qty')
    # def _onchange_qty(self):

    @api.model
    def create(self, vals):
        record = super(DetailPenjualan, self).create(vals)
        if record.qty:
            self.env['kawagomart.barang'].search([('id', '=', record.barang_id.id)]).write({'stok': record.barang_id.stok - record.qty})  # noqa
        return record

    # _sql_constraints = [
    #     ('no_qty_check', 'CHECK (qty<1)', 'Mau belanja berapa banyak sih..')]

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty < 1:
                raise ValidationError(
                    "Mau belanja {} berapa banyak sih..".format(rec.barang_id.name))  # noqa
            elif (rec.barang_id.stok < rec.qty):
                raise ValidationError("Stok barang {} tidak mencukupi. hanya tersedia {}".format(rec.barang_id.name, rec.barang_id.stok))  # noqa
