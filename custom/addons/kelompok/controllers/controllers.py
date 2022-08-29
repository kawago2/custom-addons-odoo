# -*- coding: utf-8 -*-
# from odoo import http


# class Kelompok(http.Controller):
#     @http.route('/kelompok/kelompok', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kelompok/kelompok/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kelompok.listing', {
#             'root': '/kelompok/kelompok',
#             'objects': http.request.env['kelompok.kelompok'].search([]),
#         })

#     @http.route('/kelompok/kelompok/objects/<model("kelompok.kelompok"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kelompok.object', {
#             'object': obj
#         })
