from odoo import api, fields, models


class BarangDatang(models.TransientModel):
    _name = 'kawagomart.barangdatang'

    def button_barang_datang(self):
        for rec in self:
            self.env['kawagomart.barang'].search(
                [('id', '=', rec.barang_id.id)]).write({'stok': rec.barang_id.stok + rec.jumlah})  # noqa

    def default_value_namabarang(self):
        pass   # noqa

    def default_value_jumlah(self):
        pass

    barang_id = fields.Many2one(
        'kawagomart.barang', string='Nama Barang', required=True)  # noqa

    jumlah = fields.Integer(
        string='Jumlah', required=False, default=default_value_jumlah)
