from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'kawagomart.kelompokbarang'
    _description = 'Model Kelompok Barang'

    name = fields.Selection([('makanan basah', 'Makanan Basah'), ('makanan kering',
                            'Makanan Kering'), ('minuman', 'Minuman')], string='Kelompok Barang')

    kode_kelompok = fields.Char(string='Kode Kelompok')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        # Validasi Karakter pada field 'name'
        if self.name == 'makanan basah':
            self.kode_kelompok = 'MB01'
        elif self.name == 'makanan kering':
            self.kode_kelompok = 'MK01'
        elif self.name == 'minuman':
            self.kode_kelompok = 'MN01'

    kode_rak = fields.Char(string='Kode Rak')
    barang_id = fields.One2many(
        'kawagomart.barang', 'kelompokbarang_id', string='Daftar Barang')
    jml_item = fields.Char(string='Jml Item', compute='_compute_jml_item')

    @api.depends('barang_id')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['kawagomart.barang'].search(
                [('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a

    daftar = fields.Char(string='Daftar Isi')
