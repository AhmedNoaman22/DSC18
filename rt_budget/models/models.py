# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def project_budget_vals(self):
        val = {
            'name': self.name,
            'project_id': self.id,
            'company_id': self.company_id.id or self.env.company.id,
        }
        return val

    def create_project_budget(self):
        budget_obj = self.env['project.budget']
        for rec in self:
            val = rec.project_budget_vals()
            res = budget_obj.sudo().create(val)
            return res


class HrDepartment(models.Model):
    _inherit = 'hr.department'

    hour_cost = fields.Float(string='Hour Cost')


class ProjectBudgetModel(models.Model):
    _name = 'project.budget'
    _description = 'project budget model'

    name = fields.Char(string="Name", required=True)
    company_id = fields.Many2one(comodel_name='res.company', default='lambda self: self.env.user.company_id.id',
                                 string="Company", required=True)
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
    project_id = fields.Many2one(comodel_name='project.project', string="Project")
    note = fields.Html(string='Note')
    budget_line_ids = fields.One2many('project.budget.line', 'budget_id', string="Budget Line")


class BudgetLine(models.Model):
    _name = 'project.budget.line'
    _description = 'project budget line'

    name = fields.Char(string="Name")
    budget_id = fields.Many2one('project.budget', string="Budget")
    department_id = fields.Many2one(comodel_name="hr.department", string="Department")
    hour_cost = fields.Float(string='Department Hour Cost', related="department_id.hour_cost", store=True)
    task_planned_hours = fields.Float(string='Budget Hours')
    actually_time_sheet_hour = fields.Float(string='Timesheets Hours')
    actually_cost_hour = fields.Float(string='Actually Cost')
    multiplier = fields.Float(string='(%) Multiplier', default=65.0, store=True)
    actually_cost_hours = fields.Float(string='Actually Cost Hours + Indirect Overhead')
    pm_percentage = fields.Float(string='%PM', default=0)
    etc_hours = fields.Float(string='ETC Hours', default=0)
    etc_cost_planned = fields.Float(string='ETC Cost Planned', default=0)
    amount_planing_hours = fields.Float(string='Budget Amount')
    amount_actually_hours = fields.Float(string='Total Cost')

    note = fields.Char(string='Note')
