from odoo import api, fields, models


class Person(models.Model):
    _name = 'kawagomart.person'
    _description = 'Person Model'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')


class Kasir(models.Model):
    _name = 'kawagomart.kasir'
    _inherit = 'kawagomart.person'
    _description = 'Inherintence of Person Model'

    id_kasir = fields.Char(string='ID Kasir')


class CleaningService(models.Model):
    _name = 'kawagomart.cleaningservice'
    _inherit = 'kawagomart.person'
    _description = 'Inherintence of Person Model'

    id_cln = fields.Char(string='ID Cleaning Service')
