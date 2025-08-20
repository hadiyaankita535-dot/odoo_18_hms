
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CollageStudent(models.Model):
    _name = 'collage.student'
    _description = 'Students'

    name = fields.Char(string='Student Name', required=True)
    email = fields.Char(string='Email', required=True)
    roll_no = fields.Char(string='Roll Number', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    course_id = fields.Many2one('collage.course', string='Course', required=True)
    photo = fields.Binary(string='Profile Photo')
    skill_ids = fields.Many2many(
    'collage.skill',
    'student_skill_rel',
    'student_id',
    'skill_id',
    string='Skills'
)

# -----------------------------
# CREATE
# -----------------------------
    @api.model
    def create(self, vals):
        print("\n===== CREATE METHOD =====")
        print("Incoming vals:", vals) 
        print( vals['name'], vals['age'], vals['email'])

        if 'name' in vals and isinstance(vals['name'], str):
            vals['name'] = vals['name'].title()

        if 'age' in vals and vals['age']:
            if vals['age'] < 18:
                raise ValidationError("Age is not valid")
        print(">>>>>>>>>>>>>>>>>> Successfully created <<<<<<<<<<<<<<<<<<<<<<<<")
        record =  super(CollageStudent, self).create(vals)
        return record
        # import pdb;pdb.set_trace()


# ----------------------
# Search
# ------------------------
    def action_read_methods_demo(self):
        student_ids = self.env['collage.student'].search([('age', '>', 18)])
        print(">>>>>>>>>>>>>>>>>> Successfully created Search() <<<<<<<<<<<<<<<<<<<<<<<<")
        print("Search() → Records with age > 18:", student_ids)



# -----------------------------
# UPDATE (WRITE)
# -----------------------------
    def write(self, vals):
        print("\n===== WRITE (UPDATE) METHOD =====")
        print("Incoming vals:", vals)
        res = super(CollageStudent, self).write(vals)
        print("!!!!!!!!!!!!!!!!!!!!!",res)
        return res

# -----------------------------
# DELETE (UNLINK)
# -----------------------------
    def unlink(self):
        print("\n===== UNLINK (DELETE) METHOD =====")
        print("Self (recordset to delete):", self)
        for record in self:
            if record.age < 18:
                raise ValidationError(f"Cannot delete student {record.name} because they are under 18.")
        res = super(CollageStudent, self).unlink()
        return res

# -----------------------------
# COPY
# -----------------------------
    def copy(self, default=None):
        print("\n===== COPY METHOD =====")
        print("Self (record being copied):", self)
        print("Default values dict:", default)
        new_record = super(CollageStudent, self).copy(default)
        return new_record


# -----------------------------
# Relational Field Commands Demo
# -----------------------------

# 1. Create a new record and link it

    # def action_relational_commands_demo(self):
    #     print("\n===== RELATIONAL FIELD COMMANDS DEMO =====")
    #     self.write({'skill_ids': [(0, 0, {'name': 'Odoo'})]})
    #     print("Create Records:", self.skill_ids)


# # 2. to update an existing linked record.

    def action_relational_commands_demo(self):
        print("<<<<<<<<<<<<<<<<<Update>>>>>>>>>>>>>>>>>>>> ")
        # import pdb;pdb.set_trace()
        self.write({'skill_ids': [(1, 67, {'name' : 'QWeb'})]})
        print('Updatd record', self.skill_ids)


# # 3. to delete the linked record

#     def action_relational_commands_demo(self):
#         print("<<<<<<<<<<<<<<<<<< Delete>>>>>>>>>>>>>>>>>>")
#         self.write({"skill_ids" : [(2, 5)]})
#         print("Deleted record", self.skill_ids)


# # unlink method
#     def action_relational_commands_demo(self):
#         print("<<<<<<<<<<< Unlink record>>>>>>>>>>>>>>>>>>")
#         self.write({"skill_ids" : [(3, 4)]})
#         print("Unlink record", self.skill_ids)


class CollageSkill(models.Model):
    _name = 'collage.skill'
    _description = 'Skills'

    name = fields.Char("Skill Name", required=True)




