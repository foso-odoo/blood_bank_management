from odoo import fields, models
from odoo import _,api, fields, models
from dateutil.relativedelta import relativedelta
from datetime import timedelta

class BloodBankProperty(models.Model):
    _name = "bloodbank.property"
    _description = "Blood Bank Properties"
    
    name = fields.Char('Donor Name')  
    donor_id = fields.Char('Donor ID', default=lambda self: self.env['ir.sequence'].next_by_code('blood_bank_property_sequence'))
    blood_group = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')],
        string='Blood Group'
    )
    weight = fields.Float('Donor Weight', required=True)
    age = fields.Integer('Donor Age', required=True)
    blood_bag = fields.Char('Blood Bag', copy=False)
    units = fields.Integer('Blood Units')
    donation_date = fields.Date('Donation Date', default=fields.Date.today())
    description = fields.Text('Description')
    expiry_date=fields.Date("Expiry Date" ,compute='_compute_expiry_date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('test', 'Test'),
        ('donate', 'Donate'),
        ('reject', 'Rejected'),
    ], 'State', required=True, default='draft', copy=False)
    blood_bank_id=fields.Many2one("bloodbank.bloodstock.property" ,string = "Blood Bank")
    
    
    def _compute_expiry_date(self):
        for record in self:
            if record.donation_date:
                record.expiry_date = record.donation_date + timedelta(days=30)
        