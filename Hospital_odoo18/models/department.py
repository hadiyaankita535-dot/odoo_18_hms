from odoo import fields, models, api

class HospitalDepartment(models.Model):
    _name = 'hospital.department'
    _description = 'Departments'

    name = fields.Char(string='Department Name')
    doctor_id = fields.One2many('hospital.doctor', 'department_id', string='Doctors')
    patient_id = fields.One2many('hospital.patient', 'department_id', string='Patients')
    disease_id = fields.One2many('hospital.disease', 'department_id', string='Disease')
    patient_id = fields.Many2many('hospital.patient',string='Patients')

