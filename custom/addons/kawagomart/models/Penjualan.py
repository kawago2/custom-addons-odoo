from odoo import api, fields, models, _


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

    @api.onchange('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = self.env['kawagomart.detailpenjualan'].search(  # noqa
                [('penjualan_id', '=', rec.id)]).mapped('subtotal')  # noqa
            rec.total_bayar = sum(a)


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
