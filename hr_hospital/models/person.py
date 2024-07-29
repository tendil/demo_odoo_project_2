from odoo import models, fields, api


class Person(models.AbstractModel):
    _name = 'hr_hospital.person'
    _description = 'Person'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    name = fields.Char(string='Full Name', compute='_compute_name', store=True)
    phone = fields.Char(string='Phone')
    photo = fields.Binary(string='Photo')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for person in self:
            person.name = f"{person.first_name} {person.last_name}"
