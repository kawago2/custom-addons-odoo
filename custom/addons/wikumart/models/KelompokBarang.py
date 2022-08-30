from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'wikumart.kelompokbarang'
    _description = 'New Description'

    name = fields.Char(string='Nama Kelompok')
    kode_kelompok = fields.Char(string='Kode Kelompok')
    kode_rak = fields.Char(string='Kode Rak')
    barang_ids = fields.One2many(comodel_name='wikumart.barang', 
                                inverse_name='kelompokbarang_id', 
                                string='Daftar Barang')
    
    

