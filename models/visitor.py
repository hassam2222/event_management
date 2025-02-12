from odoo import models, fields


class EventVisitor(models.Model):
    _name = "event.visitor"
    _description = "Event Visitor Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Visitor Name",required=True)
    age = fields.Integer(string="Visitor Age",required=True)
    phone = fields.Char(string="Phone Number",required=True)
    email = fields.Char(string="Email Address",required=True)
    event_id = fields.Many2one('event.management', string="Event",required=True)
