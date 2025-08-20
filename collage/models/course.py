from odoo import models, fields

class CollageCourse(models.Model):
    _name = 'collage.course'
    _description = 'Course'

    name = fields.Char(string="Course Name", required=True)
    duration = fields.Integer(string="Duration (Years)")
    department_id = fields.Many2one('collage.department', string='Department', required=True)
    student_id = fields.One2many('collage.student', 'course_id', string = 'Students')

