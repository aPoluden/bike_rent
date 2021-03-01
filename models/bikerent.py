import datetime

from odoo import models, fields, api
from odoo.exceptions import UserError


class BikeRent(models.Model):

    _name = 'bike.rent'  # model name
    _description = 'BikeRent'  # model title

    name = 'Bike Rent'
    description = 'BlaB la'
    partner_id = fields.Many2one('res.partner')
    bike_id = fields.Many2one('product.product')
    currency_id = fields.Many2one('res.currency', string='Currency')
    price = fields.Monetary(help='Price in Euros')
    rent_start = fields.Datetime(help='Rent start', required=True)
    rent_stop = fields.Datetime(help='Rent stop', required=True)
    notes = fields.Text('Notes')
    number_of_days = fields.Integer(
        string="Rent days", compute='_compute_rent_delta')

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

    @ classmethod
    def _validate_rent_dates(cls, rent_start: datetime, rent_stop: datetime):
        if rent_start > rent_stop:
            raise UserError("Rent start greater than rent stop")
