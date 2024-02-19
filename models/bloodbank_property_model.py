from odoo import fields, models

class BloodBankProperty(models.Model):
    _name = "bloodbank.property"
    _description = "Blood Bank Properties"
    
    name = fields.Char('Donor Name', required=True, translate=True)  
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
    units = fields.Integer('Blood Units', default=1)
    donation_date = fields.Date('Donation Date', default=fields.Date.today())
    description = fields.Text('Description')
