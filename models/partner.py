import datetime

from odoo import models, fields


class Partner(models.Model):

    _inherit = 'res.partner'

    def action_view_partner_rent_list(self) -> dict:
        # https://supportuae.wordpress.com/2017/10/01/redirect-to-tree-view-from-button-click-odoo/
        partner_ids = [
            contact.id for contact in self.child_ids] if self.is_company else []
        partner_ids.append(self.id)
        return {
            'name':   ('Partner Rent List'),
            'type':   'ir.actions.act_window',
            # 'view_type':   'form',
            'view_mode':   'tree',  # pivot
            'target':   'new',  # shows in panel
            'res_model':   'bike.rent',
            # 'view_id':   False,
            'domain':   [('partner_id', 'in', partner_ids)]
        }
