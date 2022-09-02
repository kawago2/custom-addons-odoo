from odoo import api, fields, models


class Barang(models.Model):
    _name = 'kawagomart.barang'
    _description = 'Model Barang'

    name = fields.Char(string='Nama Barang')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    kelompokbarang_id = fields.Many2one(
        'kawagomart.kelompokbarang', string='Kelompok Barang', ondelete='cascade')  # noqa

    supplier_id = fields.Many2many(
        string='Supplier',
        comodel_name='kawagomart.supplier',
    )
