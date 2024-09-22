from datetime import date
from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _inherit = 'hr_hospital.person'
    _description = 'Patient'

    doctor_id = fields.Many2one('hr_hospital.doctor', string='Personal Doctor')
    birth_date = fields.Date(string='Birth Date')
    passport_info = fields.Char(string='Passport Information')
    contact_person = fields.Char(string='Contact Person')
    age = fields.Integer(string='Age', compute='_compute_age')
    disease_ids = fields.Many2many('hr_hospital.disease', string='Diseases')
    visit_ids = fields.One2many('hr_hospital.visit', 'patient_id', string='Visits')
    diagnosis_ids = fields.One2many('hr_hospital.diagnosis', 'patient_id', string='Diagnoses')

    @api.depends('birth_date')
    def _compute_age(self):
        for patient in self:
            if patient.birth_date:
                patient.age = date.today().year - patient.birth_date.year
            else:
                patient.age = 0

    def action_create_visit(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'hr_hospital.visit',
            'view_mode': 'form',
            'context': {
                'default_patient_id': self.id,
                'default_doctor_id': self.doctor_id.id if self.doctor_id else False,
            },
            'target': 'new',
        }
