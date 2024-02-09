# from odoo import fields, models


# class BloodBank(models.Model):
#     _name = "blood_bank_property"
#     _description = "Blood Bank Properties"
#     # _order = "sequence"
#     name = fields.Char('Donor Name', required=True, translate=True)  
#     donor_id=fields.Integer('Donor id',sequence=)
#     blood_group=fields.Selection('Blood Group')
#     weight=fields.Float('Donor weight')
#     age=fields.Integer('Donor age')
#     blood_bag=fields.String('blood bag')
#     units=fields.Integer('Blood Units')
#     donation_date=fields.Date('Donation Date')
#     description=fields.Text('Description')

from odoo import fields, models

class BloodBank(models.Model):
    _name = "bloodbank_property"
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

    
    # sell_price = fields.Integer('Selling Price', readonly=True)
    # post_code = fields.Integer('Post Code ')
    # availability_date = fields.Date('Availability Date', copy=False)
    # number_of_bedrooms = fields.Integer('# Bedrooms', default=2)
    # expected_price=fields.Integer('Expected Price',copy=False)
    # active = fields.Boolean('Active', default=True)
    # state = fields.Selection([
    #     ('new', 'New'),
    #     ('offer_received', 'Offer Received'),
    #     ('offer_accepted', 'Offer Accepted'),
    #     ('sold', 'Sold'),
    #     ('canceled', 'Canceled')
    # ], 'State', required=True, default='new', copy=False)
    # description=fields.Text('Description')
    # living_area=fields.Integer('Living Area',default=500)
    # garden = fields.Boolean('Garden', default=True)
    # garden_area=fields.Boolean('Garden Area')