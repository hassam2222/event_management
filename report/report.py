
from odoo import fields, models, api

# class GatePassReport(models.AbstractModel):
#     _name = 'report.event_management.report_event_gate_pass_temp'
#     _description = 'Gate Pass Report'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         docs = self.env['gate.pass'].browse(docids)
#         return {
#             'doc_ids': docids,
#             'doc_model': 'gate.pass',
#             'docs': docs,
#             'company': self.env.company,
#         }
