from odoo import models, fields, api


class DiagnosisReportWizard(models.TransientModel):
    _name = 'hr_hospital.diagnosis_report_wizard'
    _description = 'Diagnosis Report Wizard'

    doctor_ids = fields.Many2many('hr_hospital.doctor', string='Doctors')
    disease_ids = fields.Many2many('hr_hospital.disease', string='Diseases')
    date_from = fields.Date(string='From Date', default=fields.Date.context_today)
    date_to = fields.Date(string='To Date', default=fields.Date.context_today)

    def generate_report(self):
        domain = [('visit_id.visit_datetime', '>=', self.date_from),
                  ('visit_id.visit_datetime', '<=', self.date_to)]
        if self.doctor_ids:
            domain.append(('visit_id.doctor_id', 'in', self.doctor_ids.ids))
        if self.disease_ids:
            domain.append(('disease_id', 'in', self.disease_ids.ids))

        diagnoses = self.env['hr_hospital.diagnosis'].search(domain)
        grouped_diagnoses = {}
        for diagnosis in diagnoses:
            disease_name = diagnosis.disease_id.name
            if disease_name not in grouped_diagnoses:
                grouped_diagnoses[disease_name] = []
            grouped_diagnoses[disease_name].append(diagnosis)

        return self.env.ref('hr_hospital.action_diagnosis_report').report_action(self, data={
            'grouped_diagnoses': grouped_diagnoses})
