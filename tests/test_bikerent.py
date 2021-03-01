import datetime as dt

from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestSaleOrder(TransactionCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        # self.BikeRent = self.env['bike.rent']
        # self.SaleOrder = self.env['sale.order']
        # self.SaleOrderLine = self.env['sale.order.line']
        # sale_order = self.SaleOrder.create()
        # sale_order_line = self.SaleOrderLine.create()


class BikeRentCommon(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        self.BikeRent = self.env['bike.rent']

    def test_rent_date_compute(self):
        # case when User returns rental same day
        bike_rent_ode_0 = self.BikeRent.create({
            'rent_start': dt.datetime.now(),
            'rent_stop': dt.datetime.now(),
        })
        bike_rent_ode_1 = self.BikeRent.create({
            'rent_start': dt.datetime(2020, 1, 1),
            'rent_stop': dt.datetime(2020, 1, 2),
        })
        self.assertEqual(bike_rent_ode_0.number_of_days, 1)
        self.assertEqual(bike_rent_ode_1.number_of_days, 1)

    def test_rent_date_validation_incorect_date(self):
        rent_start, rent_stop = dt.datetime(
            2020, 2, 1), dt.datetime(2020, 1, 1)
        with self.assertRaises(UserError):
            self.BikeRent._validate_rent_dates(rent_start, rent_stop)

    def test_rent_date_validation_same_date(self):
        rent_start, rent_stop = dt.datetime(
            2020, 1, 1), dt.datetime(2020, 1, 1)
        self.BikeRent._validate_rent_dates(rent_start, rent_stop)

    def test_rent_date_validation_correct_date(self):
        rent_start, rent_stop = dt.datetime(
            2020, 1, 1), dt.datetime(2020, 1, 2)
        self.BikeRent._validate_rent_dates(rent_start, rent_stop)
