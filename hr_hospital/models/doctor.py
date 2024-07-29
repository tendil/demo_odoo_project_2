from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _inherit = 'hr_hospital.person'
    _description = 'Doctor'

    specialty_id = fields.Many2one('hr_hospital.specialty', string='Specialty')
    is_intern = fields.Boolean(string='Intern')
    mentor_id = fields.Many2one('hr_hospital.doctor', string='Mentor', domain=[('is_intern', '=', False)])
    patient_ids = fields.One2many('hr_hospital.patient', 'doctor_id', string='Patients')
    visit_ids = fields.One2many('hr_hospital.visit', 'doctor_id', string='Visits')

    @api.constrains('mentor_id', 'is_intern')
    def _check_mentor(self):
        for doctor in self:
            if doctor.is_intern and not doctor.mentor_id:
                raise ValidationError('Intern must have a mentor.')
            if not doctor.is_intern and doctor.mentor_id:
                raise ValidationError('Non-intern doctor cannot have a mentor.')
            if doctor.is_intern and doctor.mentor_id == doctor:
                raise ValidationError('Doctor cannot be their own mentor.')
