from unicodedata import name
from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'kawagomart.supplier'
    _description = 'Model Supplier'

    name = fields.Char(string='Nama Supplier')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telp')

    barang_id = fields.Many2many(
        string='Barang',
        comodel_name='kawagomart.barang',
    )
