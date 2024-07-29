from odoo import models, fields


class Specialty(models.Model):
    _name = 'hr_hospital.specialty'
    _description = 'Specialty'

    name = fields.Char(string='Specialty Name', required=True)
