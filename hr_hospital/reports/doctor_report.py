from odoo import api, models


class DiagnosisReport(models.AbstractModel):
    _name = 'report.hr_hospital.diagnosis_report_template'
    _description = 'Diagnosis Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['hr_hospital.diagnosis_report_wizard'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hr_hospital.diagnosis_report_wizard',
            'data': data,
            'docs': docs,
        }
