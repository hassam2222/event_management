from odoo import models, fields


class EventManagement(models.Model):
    _name = "event.management"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Event Management"

    name = fields.Char(string="Event Name", required=True)
    datefrom = fields.Date(string="Date From", required=True)
    dateto = fields.Date(string="Date To", required=True)
    location = fields.Char(string="Event Location", required=True)
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ], string='Status',default="draft")

    def action_start(self):
        self.state = 'started'

    def action_complete(self):
        self.state = 'completed'

    def action_cancel(self):
        self.state = 'canceled'
