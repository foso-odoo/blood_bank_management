from odoo import fields, models

class BloodBankBloodstockProperty(models.Model):
    _name = "bloodbank.bloodstock.property"
    _description = "Blood Bank Blood Stock Properties"
    
    blood_group = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')],
        string='Blood Group'
    )
    
    blood_bag=fields.Text("Blood Bag")
    available_quantity=fields.Integer("Available Quantity")
    expiry_date=fields.Date("Expiry Date")
    cost=fields.Integer("Cost Per Unit")
    

    description = fields.Text('Description')
    
    # Establishing a Many-to-One relationship with BloodBankBloodProperty
    blood_property_id = fields.Many2one('bloodbank.blood.property', string='Blood Property')
