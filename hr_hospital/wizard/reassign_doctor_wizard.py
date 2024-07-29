from odoo import models, fields


class ReassignDoctorWizard(models.TransientModel):
    _name = 'hr_hospital.reassign_doctor_wizard'
    _description = 'Reassign Personal Doctor Wizard'

    doctor_id = fields.Many2one('hr_hospital.doctor', string='New Doctor', required=True)
    patient_ids = fields.Many2many('hr_hospital.patient', string='Patients')

    def reassign_doctor(self):
        for patient in self.patient_ids:
            patient.doctor_id = self.doctor_id
        return {'type': 'ir.actions.act_window_close'}
