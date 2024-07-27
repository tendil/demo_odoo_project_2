from odoo import models, fields


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Name', required=True)
    specialty = fields.Char(string='Specialty')
    phone = fields.Char(string='Phone')
    patient_ids = fields.One2many('hr_hospital.patient', 'doctor_id', string='Patients')
    visit_ids = fields.One2many('hr_hospital.visit', 'doctor_id', string='Visits')
