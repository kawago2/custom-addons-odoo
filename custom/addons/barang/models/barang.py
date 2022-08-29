# -*- coding: utf-8 -*-

from odoo import models, fields


class BarangBarang(models.Model):
    _name = "barang.barang"
    _description = "Testing add module"

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
