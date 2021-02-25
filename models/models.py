# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api
from odoo.exceptions import UserError


class Partner(models.Model):

    _inherit = 'res.partner'

    def action_view_partner_rent_list(self) -> dict:
        # https://supportuae.wordpress.com/2017/10/01/redirect-to-tree-view-from-button-click-odoo/
        partner_ids = [
            contact.id for contact in self.child_ids] if self.is_company else []
        partner_ids.append(self.id)
        return {
            'name':   ('Partner rent list'),
            'type':   'ir.actions.act_window',
            # 'view_type':   'form',
            'view_mode':   'tree',  # pivot
            'target':   'new',  # shows in panel
            'res_model':   'bike.rent',
            # 'view_id':   False,
            'domain':   [('partner_id', 'in', partner_ids)]
        }


class Product(models.Model):

    _inherit = 'product.product'

    bike_rent = fields.One2many(
        comodel_name='bike.rent', inverse_name='bike_id')


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    is_bike = fields.Boolean(string='Is bicycle')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')


class BikeRent(models.Model):

    _name = 'bike.rent'
    _description = 'BikeRent'

    partner_id = fields.Many2one('res.partner')
    bike_id = fields.Many2one('product.product')
    currency_id = fields.Many2one('res.currency', string='Currency')
    price = fields.Monetary(help='Price in Euros')
    rent_start = fields.Datetime(help='Rent start', required=True)
    rent_stop = fields.Datetime(help='Rent stop', required=True)
    notes = fields.Text('Notes')
    number_of_days = fields.Integer(
        string="Rent days", compute='_compute_rent_delta')

    @ classmethod
    def _validate_rent_dates(cls, rent_start: datetime, rent_stop: datetime):
        if rent_start > rent_stop:
            raise UserError("Rent start greater than rent stop")

    @ api.depends('rent_start', 'rent_stop')
    def _compute_rent_delta(self):
        for record in self:
            dt = record.rent_stop.date() - record.rent_start.date()
            record.number_of_days = 1 if dt.days == 0 else dt.days

    @ api.onchange('rent_stop')
    def _onchange_rent_stop(self):
        if self.rent_start:
            self._validate_rent_dates(self.rent_start, self.rent_stop)

    @ api.onchange('rent_start')
    def _onchange_rent_start(self):
        if self.rent_stop:
            self._validate_rent_dates(self.rent_start, self.rent_stop)
