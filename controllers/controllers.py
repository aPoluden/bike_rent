# -*- coding: utf-8 -*-
# from odoo import http


# class ../customAddons/bikeRent(http.Controller):
#     @http.route('/../custom_addons/bike_rent/../custom_addons/bike_rent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../custom_addons/bike_rent/../custom_addons/bike_rent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../custom_addons/bike_rent.listing', {
#             'root': '/../custom_addons/bike_rent/../custom_addons/bike_rent',
#             'objects': http.request.env['../custom_addons/bike_rent.../custom_addons/bike_rent'].search([]),
#         })

#     @http.route('/../custom_addons/bike_rent/../custom_addons/bike_rent/objects/<model("../custom_addons/bike_rent.../custom_addons/bike_rent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../custom_addons/bike_rent.object', {
#             'object': obj
#         })
