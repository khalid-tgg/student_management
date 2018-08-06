from odoo import fields, models


class InternalNote(models.Model):

    _name = 'internal.note'
    _description = 'Internal Note'

    description = fields.Char(required=True)
    user_id = fields.Char()
    student_id = fields.Many2one(comodel_name='student')
