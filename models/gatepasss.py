from odoo import models, fields, api


class GatePass(models.Model):
    _name = 'gate.pass'
    _description = 'Gate Pass'
    _rec_name="event_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    event_id = fields.Many2one('event.management', string='Event',required=True)
    visitor_id = fields.Many2one('event.visitor', string='Visitor Name')
    creator_id = fields.Many2one('event.creator', string='Creator Name')
    datefrom = fields.Date(string='Date From',required=True)
    dateto = fields.Date(string='Date To',required=True)
    role = fields.Selection([
        ('creator', 'Creator'),
        ('visitor', 'Visitor')
    ], string="Role",required=True)
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    @api.onchange('event_id')
    def date_change(self):
        self.datefrom = self.event_id.datefrom
        self.dateto = self.event_id.dateto

