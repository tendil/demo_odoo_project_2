from odoo import models, fields


class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Diagnosis'

    visit_id = fields.Many2one('hr_hospital.visit', string='Visit', required=True)
    disease_id = fields.Many2one('hr_hospital.disease', string='Disease', required=True)
    description = fields.Text(string='Description')
    is_approved = fields.Boolean(string='Approved', default=False)
