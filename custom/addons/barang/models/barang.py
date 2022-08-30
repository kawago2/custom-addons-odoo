# -*- coding: utf-8 -*-


from odoo import models, fields


class BarangBarang(models.Model):
    _name = "barang.barang"
    _description = "Testing add module"

    name = fields.Char(string='Nama Barang', required=True)
    harga = fields.Float(string='Harga', required=True)
    description = fields.Text()
