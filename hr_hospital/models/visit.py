from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Patient Visit'

    patient_id = fields.Many2one('hr_hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor', required=True)
    planned_datetime = fields.Datetime(string='Planned Date and Time', required=True)
    visit_datetime = fields.Datetime(string='Visit Date and Time')
    status = fields.Selection([
        ('planned', 'Planned'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='planned')
    diagnosis_ids = fields.One2many('hr_hospital.diagnosis', 'visit_id', string='Diagnosis')
    notes = fields.Text(string='Notes')

    @api.constrains('planned_datetime', 'doctor_id', 'patient_id')
    def _check_visit_uniqueness(self):
        for visit in self:
            overlapping_visits = self.search([
                ('planned_datetime', '=', visit.planned_datetime),
                ('doctor_id', '=', visit.doctor_id.id),
                ('patient_id', '=', visit.patient_id.id),
                ('id', '!=', visit.id)
            ])
            if overlapping_visits:
                raise ValidationError(_('A patient cannot have more than one visit with the same doctor on the same day.'))

    @api.constrains('status', 'visit_datetime', 'doctor_id', 'planned_datetime')
    def _check_visit_modification(self):
        for visit in self:
            if visit.status == 'done':
                if 'doctor_id' in visit._origin and visit.doctor_id != visit._origin.doctor_id:
                    raise ValidationError(_('Cannot modify the doctor of a completed visit.'))
                if 'planned_datetime' in visit._origin and visit.planned_datetime != visit._origin.planned_datetime:
                    raise ValidationError(_('Cannot modify the planned date and time of a completed visit.'))
                if 'visit_datetime' in visit._origin and visit.visit_datetime != visit._origin.visit_datetime:
                    raise ValidationError(_('Cannot modify the visit date and time of a completed visit.'))

    @api.constrains('diagnosis_ids')
    def _check_visit_archiving(self):
        for visit in self:
            if visit.diagnosis_ids and (visit.status == 'cancelled'):
                raise ValidationError(_('Cannot cancel a visit with diagnoses.'))
