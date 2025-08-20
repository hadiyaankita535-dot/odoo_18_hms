from odoo import fields, models, api
from datetime import datetime

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctors'


    serial_no = fields.Char(string="Doctor ID", copy=False, readonly=True)
    name = fields.Char(string='Doctor Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    schedule_start = fields.Datetime(string='Available From')
    schedule_end = fields.Datetime(string='Available To')
    experience = fields.Integer(string='Year of Experience')
    phone_no = fields.Char(string='Contact Number')
    department_id = fields.Many2one('hospital.department', string="Department")
    patient_id = fields.One2many('hospital.patient', 'doctor_id', string='Patients', readonly=1)
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')
    photo = fields.Binary(string='Profile Photo', attachment=True) 

   
    @api.model
    def create(self, vals):
        print(vals)
        if vals.get('serial_no', 'New') == 'New':
            print("Called -")
            vals['serial_no'] = self.env['ir.sequence'].next_by_code('hospital.doctor.name')
        print("===============================",vals)
        return super(HospitalDoctor, self).create(vals)   # Without super, you’re only modifying vals in memory — nothing would be stored in the DB


    def set_active(self):
        for doctor in self:
            doctor.status = 'active'


    def set_inactive(self):
        for doctor in self:
            doctor.write({
                'status': 'inactive',
                'schedule_start': False,
                'schedule_end': False
            })


    # -----------Wizard--------------------

    def action_open_doctor_patient_wizard(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'Patients Wizard',
        'res_model': 'doctor.patient.wizard',
        'view_mode': 'form',
        'target': 'new',
    }

        
        





    