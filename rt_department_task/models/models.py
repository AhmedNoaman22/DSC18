# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    task_id = fields.Many2one(
        'project.task', 'Task', index='btree_not_null',
        compute='_compute_task_id', store=True, readonly=False,
        domain="[('allow_timesheets', '=', True), "
               "('project_id', '=?', project_id), "
               "('department_id', '=', user_department)]"
    )

    user_department = fields.Many2one('hr.department', string="User Department", compute="_compute_user_department")

    @api.onchange('project_id')
    def _compute_user_department(self):
        employee = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)], limit=1)
        if employee:
            self.user_department = employee.department_id
        else:
            self.user_department = False
