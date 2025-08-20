from odoo import fields, models, api

class HospitalDisease(models.Model):
	_name = 'hospital.disease'
	_description = 'Disease'

	name = fields.Char(string = 'Disease Name')
	patient_id = fields.Many2many('hospital.patient', string = 'Patients')
	department_id = fields.Many2one('hospital.department', string='Departments')
	
	