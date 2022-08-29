# -*- coding: utf-8 -*-
# from odoo import http


# class Prototype(http.Controller):
#     @http.route('/prototype/prototype', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prototype/prototype/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prototype.listing', {
#             'root': '/prototype/prototype',
#             'objects': http.request.env['prototype.prototype'].search([]),
#         })

#     @http.route('/prototype/prototype/objects/<model("prototype.prototype"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prototype.object', {
#             'object': obj
#         })
