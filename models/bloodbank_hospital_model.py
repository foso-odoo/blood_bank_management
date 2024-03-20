from odoo import fields, models, api

class BloodBankHospitalProperty(models.Model):
    _name = "bloodbank.hospital.property"
    _description = "Blood Bank Hospital Properties"
    
    name = fields.Char('Hospital Name', required=True, translate=True)  
    address=fields.Text('Hospital Address')
    contact_no=fields.Integer('Phone No')
    required_units=fields.Integer('Required Units' ,required=True)
    description=fields.Text('Description')
    blood_bank_ids = fields.One2many('bloodbank.bloodstock.property', 'hospital_id', string='Blood Banks')

    #stat button
    bloodbank_count_for_A = fields.Integer(string="BloodBank Count : Group A", compute="_compute_bloodbank_A")
    bloodbank_count_for_B = fields.Integer(string="BloodBank Count : Group B", compute="_compute_bloodbank_B")
    bloodbank_count_for_C = fields.Integer(string="BloodBank Count : Group C", compute="_compute_bloodbank_C")    
    bloodbank_count_for_D = fields.Integer(string="BloodBank Count : Group D", compute="_compute_bloodbank_D")    
    
    
        
    # @api.depends('required_bg', 'required_units', 'blood_bank_ids.available_quantity', 'blood_bank_ids.blood_group')
    # def _compute_bloodbank(self):
    #     for hos in self:
    #         blood_bank_count = len(self.env["bloodbank.bloodstock.property"].search([
    #         ("blood_group", "=", hos.required_bg),
    #         ("available_quantity", ">=", hos.required_units)
    #     ]))
    #         hos.bloodbank_count = blood_bank_count
            
    @api.depends('blood_bank_ids')
    def _compute_bloodbank_A(self):
        for hospital in self:
            blood_bank_count = 0
            for blood_bank in hospital.blood_bank_ids:
                if blood_bank.available_quantity_A > 0:
                    blood_bank_count += 1
            hospital.bloodbank_count_for_A = blood_bank_count
            
    @api.depends('blood_bank_ids')
    def _compute_bloodbank_B(self):
        for hospital in self:
            blood_bank_count = 0
            for blood_bank in hospital.blood_bank_ids:
                if blood_bank.available_quantity_B > 0:
                    blood_bank_count += 1
            hospital.bloodbank_count_for_B = blood_bank_count
            
    @api.depends('blood_bank_ids')
    def _compute_bloodbank_C(self):
        for hospital in self:
            blood_bank_count = 0
            for blood_bank in hospital.blood_bank_ids:
                if blood_bank.available_quantity_AB > 0:
                    blood_bank_count += 1
            hospital.bloodbank_count_for_C = blood_bank_count
            
    @api.depends('blood_bank_ids')
    def _compute_bloodbank_D(self):
        for hospital in self:
            blood_bank_count = 0
            for blood_bank in hospital.blood_bank_ids:
                if blood_bank.available_quantity_O > 0:
                    blood_bank_count += 1
            hospital.bloodbank_count_for_D = blood_bank_count



            

    # @api.depends('required_bg', 'required_units', 'blood_bank_ids.available_quantity', 'blood_bank_ids.blood_group')
    # def _compute_bloodbank(self):
    #     for hos in self:
    #         blood_bank_count = 0
    #         for blood_bank in hos.blood_bank_ids:
    #             if blood_bank.blood_group == hos.required_bg and blood_bank.available_quantity >= hos.required_units:
    #                 print(blood_bank.blood_group)
    #                 print(hos.required_bg)
    #                 print(blood_bank.available_quantity)
    #                 print(hos.required_units)
    #                 blood_bank_count += 1
    #             hos.bloodbank_count = blood_bank_count

            


                    
                
                
