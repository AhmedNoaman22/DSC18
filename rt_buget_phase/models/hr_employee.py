# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Hr Employee Inherit'

    @api.model_create_multi
    def create(self, vals):
        res = super(HrEmployee, self).create(vals)
        for rec in res:
            if rec.hourly_cost or rec.name:
                if rec['hourly_cost'] == 0.00:
                    raise ValidationError(_("The Hourly cost is required field when create."))
        return res

    def write(self, vals):
        res = super().write(vals)
        if 'hourly_cost' in vals or 'name' in vals :
            for rec in self:
                if rec.hourly_cost == 0.00:
                    raise ValidationError(_("The Hourly cost is required field."))
        return res

    # @api.onchange('hourly_cost')
    # def _constraints_on_hourly_cost(self):
    #     if self.hourly_cost == 0.00:
    #         raise ValidationError(_("The Hourly cost is required field."))

    # @api.constrains('hourly_cost')
    # def _constraints_on_hourly_cost(self):
    #     if self.hourly_cost == 0.00:
    #         raise ValidationError(_("The Hourly cost is required field."))
