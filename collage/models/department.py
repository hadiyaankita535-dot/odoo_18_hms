from odoo import models, fields

class CollageDepartment(models.Model):
    _name = 'collage.department'
    _description = 'Department'

    name = fields.Char(string = 'Department Name', required = True)
    course_id = fields.One2many('collage.course', 'department_id', string = 'Course')
