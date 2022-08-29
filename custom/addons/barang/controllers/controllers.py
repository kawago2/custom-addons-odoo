# -*- coding: utf-8 -*-
# from odoo import http


# class Barang(http.Controller):
#     @http.route('/barang/barang', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barang/barang/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('barang.listing', {
#             'root': '/barang/barang',
#             'objects': http.request.env['barang.barang'].search([]),
#         })

#     @http.route('/barang/barang/objects/<model("barang.barang"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barang.object', {
#             'object': obj
#         })
