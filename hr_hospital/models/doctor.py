from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _inherit = 'hr_hospital.person'
    _description = 'Doctor'

    name = fields.Char(string='Name', required=True)
    specialty_id = fields.Many2one('hr_hospital.specialty', string='Specialty')
    phone = fields.Char(string='Phone')
    is_intern = fields.Boolean(string='Intern')
    mentor_id = fields.Many2one('hr_hospital.doctor', string='Mentor', domain=[('is_intern', '=', False)])
    intern_ids = fields.One2many('hr_hospital.doctor', 'mentor_id', string='Interns')
    mentor_specialty_id = fields.Many2one(related='mentor_id.specialty_id', string='Mentor Specialty', store=True,
                                          readonly=True)
    mentor_phone = fields.Char(related='mentor_id.phone', string='Mentor Phone', store=True, readonly=True)
    patient_ids = fields.One2many('hr_hospital.patient', 'doctor_id', string='Patients')
    visit_ids = fields.One2many('hr_hospital.visit', 'doctor_id', string='Visits')

    @api.constrains('mentor_id', 'is_intern')
    def _check_mentor(self):
        for doctor in self:
            if doctor.is_intern and not doctor.mentor_id:
                raise ValidationError(_('Intern must have a mentor.'))
            if not doctor.is_intern and doctor.mentor_id:
                raise ValidationError(_('Non-intern doctor cannot have a mentor.'))
            if doctor.is_intern and doctor.mentor_id == doctor:
                raise ValidationError(_('Doctor cannot be their own mentor.'))

    def get_report(self):
        return self.env.ref('your_module_name.report_doctor_document').report_action(self)
