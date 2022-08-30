# -*- coding: utf-8 -*-
# from odoo import http


# class Kawagomart(http.Controller):
#     @http.route('/kawagomart/kawagomart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kawagomart/kawagomart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kawagomart.listing', {
#             'root': '/kawagomart/kawagomart',
#             'objects': http.request.env['kawagomart.kawagomart'].search([]),
#         })

#     @http.route('/kawagomart/kawagomart/objects/<model("kawagomart.kawagomart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kawagomart.object', {
#             'object': obj
#         })
