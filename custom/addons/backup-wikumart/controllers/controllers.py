# -*- coding: utf-8 -*-
# from odoo import http


# class Wikumart(http.Controller):
#     @http.route('/wikumart/wikumart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wikumart/wikumart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('wikumart.listing', {
#             'root': '/wikumart/wikumart',
#             'objects': http.request.env['wikumart.wikumart'].search([]),
#         })

#     @http.route('/wikumart/wikumart/objects/<model("wikumart.wikumart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wikumart.object', {
#             'object': obj
#         })
