from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'kawagomart.kelompokbarang'
    _description = 'Model Kelompok Barang'

    name = fields.Char(string='Nama Kelompok Barang')
    kode_kelompok = fields.Char(string='Kode Kelompok Barang')
    kode_rak = fields.Char(string='Kode Rak')
    barang_id = fields.One2many(
        'kawagomart.barang', 'kelompokbarang_id', string='Daftar Barang')
