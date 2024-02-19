from odoo import fields, models

class BloodBankHospitalProperty(models.Model):
    _name = "bloodbank.hospital.property"
    _description = "Blood Bank Hospital Properties"
    
    name = fields.Char('Hospital Name', required=True, translate=True)  
    address=fields.Text('Hospital Address')
    contact_no=fields.Integer('Phone No')
    description=fields.Text('Description')