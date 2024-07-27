from odoo import models, fields


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor')
    disease_ids = fields.Many2many('hr_hospital.disease', string='Diseases')
    visit_ids = fields.One2many('hr_hospital.visit', 'patient_id', string='Visits')
