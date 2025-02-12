from odoo import models, fields


class EventCreator(models.Model):
    _name = "event.creator"
    _description = "Event creator Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Creator Name", required=True)
    age = fields.Integer(string="Creator Age",required=True)
    phone = fields.Char(string="Phone Number",required=True)
    email = fields.Char(string="Email Address",required=True)
    event_id = fields.Many2one('event.management', string="Event",required=True)
    industry = fields.Selection([
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ], string='Industry', default='other')