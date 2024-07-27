from odoo import models, fields


class Disease(models.Model):
    _name = 'hr_hospital.disease'
    _description = 'Disease'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    patient_ids = fields.Many2many('hr_hospital.patient', string='Patients')
