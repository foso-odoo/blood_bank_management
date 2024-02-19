from odoo import fields, models, api ,_
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero


class BloodBankBloodProperty(models.Model):
    _name = "bloodbank.blood.property"
    _description = "Blood Bank Blood Properties"
    
    blood_group = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')],
        string='Blood Group'
    )
    

    description = fields.Text('Description')
    
    # Establishing a Many-to-One relationship with BloodBankProperty (Donors)
    donor_ids = fields.Many2many('bloodbank.property', string='Donors', compute='_compute_donors')
    patient_ids = fields.Many2many('bloodbank.patient.property', string='Patients', compute='_compute_patients')
    
    @api.depends('blood_group')
    def _compute_donors(self):
        for record in self:
            donors = self.env['bloodbank.property'].search([('blood_group', '=', record.blood_group)])
            record.donor_ids = [(6, 0, donors.ids)]
    
    @api.depends('blood_group')
    def _compute_patients(self):
        for record in self:
            patients = self.env['bloodbank.patient.property'].search([('blood_group', '=', record.blood_group)])
            record.patient_ids = [(6, 0, patients.ids)]

