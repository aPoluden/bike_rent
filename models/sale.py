import datetime

from odoo import models, fields


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    rent_days = fields.Integer(string='Rent days', required=True, default=1)


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        current_datetime = datetime.datetime.now()
        BikeRent = self.env['bike.rent']
        for order_line in self.order_line:
            BikeRent.create({
                'bike_id': order_line.product_id.id,
                'price': order_line.price_unit,
                'partner_id': self.partner_id.id,
                'rent_start': current_datetime,
                'rent_stop': current_datetime + datetime.timedelta(days=order_line.rent_days)
            })
