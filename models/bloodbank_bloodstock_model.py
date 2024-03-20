from odoo import fields, models ,api
import logging

_logger = logging.getLogger("blood_bank_management")


class BloodBankBloodstockProperty(models.Model):
    _name = "bloodbank.bloodstock.property"
    _description = "Blood Bank Blood Stock Properties"
    
    
    name=fields.Char("Name")
    blood_group_ids = fields.Many2many('bloodbank.blood.property' , string="Blood Group")
    blood_property_id = fields.Many2one("bloodbank.blood.property", string="Blood Property")
    blood_bag=fields.Text("Blood Bag")
    available_quantity=fields.Integer("Total Available Quantity",compute = "_compute_available_quantity" ,store=True)
    available_quantity_A=fields.Integer("Available Quantity : A",compute = "_compute_for_A" ,store=True)
    available_quantity_B=fields.Integer("Available Quantity : B",compute = "_compute_for_B" ,store=True)
    available_quantity_AB=fields.Integer("Available Quantity : AB",compute = "_compute_for_AB" ,store=True)
    available_quantity_O=fields.Integer("Available Quantity : O",compute = "_compute_for_O" ,store=True)
    blood_counts = fields.One2many('bloodbank.bloodcount', 'hospital_id', string='Blood Counts')  
    cost=fields.Integer("Cost Per Unit")
    description = fields.Text('Description')
        
    hospital_id = fields.Many2one('bloodbank.hospital.property', string='Hospital')
    donation_ids=fields.One2many('bloodbank.property',"blood_bank_id")
    
    
    
    @api.depends('donation_ids.units', 'donation_ids.blood_bank_id')
    def _compute_available_quantity(self):
        for record in self:
            # _logger.info(f"Computing available quantity for blood bank {record.name} and blood group {record.blood_group_ids}")
            total_units = sum(donation.units for donation in record.donation_ids)
            # _logger.info(f"Total units found: {total_units}")
            record.available_quantity = total_units
            
    
    @api.depends('donation_ids')
    def _compute_for_A(self):
        for record in self:
            donations_A = record.donation_ids.filtered(lambda d: d.blood_group == 'A')
            record.available_quantity_A = sum(donation.units for donation in donations_A)
            
    @api.depends('donation_ids')
    def _compute_for_B(self):
        for record in self:
            donations_B = record.donation_ids.filtered(lambda d: d.blood_group == 'B')
            record.available_quantity_B = sum(donation.units for donation in donations_B)
            
    @api.depends('donation_ids')
    def _compute_for_AB(self):
        for record in self:
            donations_AB = record.donation_ids.filtered(lambda d: d.blood_group == "AB")
            record.available_quantity_AB = sum(donation.units for donation in donations_AB)
            
    @api.depends('donation_ids')
    def _compute_for_O(self):
        for record in self:
            donations_O = record.donation_ids.filtered(lambda d: d.blood_group == 'O')
            record.available_quantity_O = sum(donation.units for donation in donations_O)
            
    

            
    
    


    
    

    
    

    
