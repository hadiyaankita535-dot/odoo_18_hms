from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patients'
    
    serial_no = fields.Char(string="Patient ID", copy=False, readonly=True)
    name = fields.Char(string='Patient Name')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ])
    date_of_birth = fields.Datetime(string='Date & Time Of Birth', required=True)
    age_display = fields.Char(string='Age', compute='_compute_age_display')
    phone_no = fields.Char(string='Contact Number')
    address = fields.Text(string='Address')
    disease_id = fields.Many2many('hospital.disease', string='Diseases')
    
    allowed_department_ids = fields.Many2many(
        'hospital.department',
        string="Allowed Departments",
        compute="_compute_allowed_departments",
        store=False
        )

    @api.depends('disease_id')
    def _compute_allowed_departments(self):
        for rec in self:
            print(rec.disease_id.mapped('department_id'))
            rec.allowed_department_ids = rec.disease_id.mapped('department_id')
            print(f"[('id', 'in', {rec.disease_id.mapped('department_id')})]")


    department_id = fields.Many2one(
    'hospital.department',
    string='Department',
    domain="[('id', 'in', allowed_department_ids)]")

    description = fields.Html(string='Description')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor',domain="[('department_id', '=', department_id)]")
    photo = fields.Binary(string='Profile Photo')
    departments = fields.Many2many('hospital.department',string="Departments",readonly=1)

    @api.onchange('disease_id')
    def _onchange_disease_id(self):
        if self.disease_id:
            return {
                'domain': {
                    'department_id': [('id', 'in', self.disease_id.mapped('department_id').ids)]
                }
            }


    # @api.onchange('disease_id')
    # def _onchange_disease_id(self):
    #     self.departments = self.disease_id.mapped('department_id')
    #     return {
    #         'domain': {'department_id': [('id', 'in', self.departments.ids)]}
    # }


    @api.model
    def create(self, vals):
        print(vals)
        if vals.get('serial_no', 'New') == 'New':
            print("Called -")
            vals['serial_no'] = self.env['ir.sequence'].next_by_code('hospital.patient.name')
        print(vals)
        return super(HospitalPatient, self).create(vals)


    @api.depends('date_of_birth')
    def _compute_age_display(self):
        for rec in self:
            if rec.date_of_birth:
                now = fields.Datetime.now()
                dob = rec.date_of_birth
                delta = relativedelta(now, dob)

                if delta.years > 0:
                    rec.age_display = f'{delta.years} years {delta.months} months'
                elif delta.months > 0:
                    rec.age_display = f'{delta.months} months {delta.days} days'
                elif delta.days > 0:
                    rec.age_display = f'{delta.days} days {delta.hours} hours'
                elif delta.hours > 0:
                    rec.age_display = f'{delta.hours} hours {delta.minutes} minutes'
                else:
                    rec.age_display = f'{delta.minutes} minutes'
            else:
                rec.age_display = 'N/A'
