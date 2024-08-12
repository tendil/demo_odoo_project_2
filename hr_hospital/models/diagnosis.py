from odoo import models, fields


class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Diagnosis'

    disease_id = fields.Many2one('hr_hospital.disease', string='Disease')
    visit_id = fields.Many2one('hr_hospital.visit', string='Visit')
    patient_id = fields.Many2one(related='visit_id.patient_id', string='Patient', store=True, readonly=True)
    parent_disease_id = fields.Many2one(related='disease_id.parent_id', string='Parent Disease', store=True,
                                        readonly=True)
    parent_disease_name = fields.Char(related='disease_id.parent_id.name', string='Parent Disease Name', store=True,
                                      readonly=True)
    description = fields.Text(string='Description')
    approved = fields.Boolean(string='Approved')
    create_date = fields.Datetime(string='Creation Date', default=fields.Datetime.now)
