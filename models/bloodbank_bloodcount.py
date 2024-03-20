from odoo import fields, models, api



class BloodBankBloodCount(models.Model):
    _name = "bloodbank.bloodcount"
    _description = "Blood Bank Blood Counts"
    
    blood_stock_id = fields.Many2one('bloodbank.bloodstock.property', string='Blood Stock')
    blood_group = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')], string='Blood Group')
    count = fields.Integer('Count')
    hospital_id= fields.Many2one('bloodbank.bloodstock.property')