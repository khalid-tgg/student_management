import re
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Student(models.Model):

    _name = 'student'
    _description = 'Student'

    name = fields.Char(required=True)
    id_student = fields.Char(
        string='Student ID',
        required=True
    )
    id_number = fields.Char(string="Identification Number", required=True)
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        required=True
    )
    image = fields.Binary()
    date_of_birth = fields.Date(required=True)
    address = fields.Text(required=True)
    phone_number = fields.Char(required=True)
    current_gpa = fields.Float()
    current_classification = fields.Selection(
        selection=[
            ('excellent', 'Excellent'),
            ('good', 'Good'),
            ('average', 'Average'),
            ('poor', 'Poor')
        ],
        compute='_compute_current_classification',
        store=True
    )
    internal_note_ids = fields.One2many(
        comodel_name='internal.note', inverse_name='student_id')

    @api.constrains('id_number')
    def _check_id_number(self):
        for student in self:
            id_number = student.id_number
            if not bool(re.match(r'^\d*$', id_number)):
                raise ValidationError(_(
                    'Identification number should contain numbers only.'))

    @api.constrains('current_gpa')
    def _check_current_gpa(self):
        for student in self:
            current_gpa = student.current_gpa
            if current_gpa < 0 or current_gpa > 10:
                raise ValidationError(_(
                    'Current gpa should be in range from 0 to 10.'))

    @api.depends('current_gpa')
    def _compute_current_classification(self):
        for student in self:
            if student.current_gpa < 5:
                student.current_classification = 'poor'
            elif student.current_gpa < 6.5:
                student.current_classification = 'average'
            elif student.current_gpa < 9:
                student.current_classification = 'good'
            else:
                student.current_classification = 'excellent'
        return True
