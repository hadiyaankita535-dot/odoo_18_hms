from odoo import fields, models, api

class DoctorPatientWizard(models.TransientModel):
    _name = "doctor.patient.wizard"
    _description = 'Doctor Patient Wizard'

    is_new_patient = fields.Boolean(string="Is New Patient?")

    patient_name = fields.Char(string='Patient Name')
    patient_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender")
    patient_date_of_birth = fields.Datetime(string='Date of Birth')
    patient_phone = fields.Char(string='Contact Number')
    patient_address = fields.Text(string='Address')
    patient_photo = fields.Binary(string='Profile Photo', attachment=True)
    patient_disease_ids = fields.Many2many('hospital.disease', string='Diseases')
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", readonly=True)

 
    patient_id = fields.Many2one('hospital.patient', string="Existing Patient")
    old_age = fields.Char(related="patient_id.age_display", readonly=True)
    old_phone = fields.Char(related="patient_id.phone_no", readonly=False)
    old_disease_ids = fields.Many2many(related="patient_id.disease_id", readonly=False)

    def action_confirm(self):
        if self.is_new_patient:
            # create new patient
            self.env['hospital.patient'].create({
                'name': self.patient_name,
                'gender': self.patient_gender,
                'address': self.patient_address,
                'photo': self.patient_photo,
                'date_of_birth': self.patient_date_of_birth,
                'phone_no': self.patient_phone,
                'disease_id': [(6, 0, self.patient_disease_ids.ids)],
                'doctor_id': self.doctor_id.id
            })
        else:
            # editing existing patient → already updated via related fields
            pass
