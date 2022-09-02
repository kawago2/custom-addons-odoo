from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Contact'

    is_konsumen = fields.Boolean(string='Konsumen')
    is_direksi = fields.Boolean(string='Direksi')
    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')
