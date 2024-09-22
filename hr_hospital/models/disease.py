from odoo import models, fields


class Disease(models.Model):
    _name = 'hr_hospital.disease'
    _description = 'Disease'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    parent_id = fields.Many2one('hr_hospital.disease', string='Parent Disease', ondelete='restrict')
    child_ids = fields.One2many('hr_hospital.disease', 'parent_id', string='Sub Diseases')
    patient_ids = fields.Many2many('hr_hospital.patient', string='Patients')
