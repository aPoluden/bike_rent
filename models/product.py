import datetime

from odoo import models, fields


class Product(models.Model):

    _inherit = 'product.product'

    bike_rent = fields.One2many(
        comodel_name='bike.rent', inverse_name='bike_id')


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    is_bike = fields.Boolean(string='Is bicycle')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
