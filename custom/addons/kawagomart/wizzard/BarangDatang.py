from odoo import api, fields, models


class BarangDatang(models.TransientModel):
    _name = 'kawagomart.barangdatang'

    barang_id = fields.Many2one(
        'kawagomart.barang', string='Nama Barang', required=True)

    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_barang_datang(self):
        for rec in self:
            self.env['kawagomart.barang'].search(
                [('id', '=', rec.barang_id.id)]).write({'stok': rec.barang_id.stok + rec.jumlah})  # noqa
