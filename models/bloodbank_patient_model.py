from odoo import fields, models

class BloodBankPatientProperty(models.Model):
    _name = "bloodbank.patient.property"
    _description = "Blood Bank Patient Properties"
    
    name=fields.Char('Patient Name')
    request_date=fields.Date('Request Date')
    blood_group = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')],
        string='Blood Group'
    )
    approx_date=fields.Date('Approx Requirement Date')
    is_urgent=fields.Boolean('Is Urgent?')
    phone_no=fields.Integer('Phone No')
    current_disease=fields.Char('Current Disease')
    required_units=fields.Integer('Required Units')
    description=fields.Text('Description')
    
    #blood_bag
