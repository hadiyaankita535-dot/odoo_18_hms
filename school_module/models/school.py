from odoo import models, fields

class School(models.Model):
    _name = 'school.school'
    _description = 'School'

    name = fields.Char(string="School Name", required=True)
    address = fields.Char(string="Address")
    student_ids = fields.One2many('school.student', 'school_id', string='Students')