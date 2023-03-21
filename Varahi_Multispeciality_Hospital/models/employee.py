from datetime import date
from odoo import api, fields, models

class HospitalEmployee(models.Model):
    _name = "hospital.employee"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ="Hospital Employee Details"

    name = fields.Char(compute='employee_full_name', tracking=True)
    ref = fields.Char(string="Ref", tracking=True)
    first_name = fields.Char(string="First Name", tracking=True)
    middle_name = fields.Char(string="Middle Name", tracking=True)
    last_name = fields.Char(string="Last Name", tracking=True)
    date_of_birth = fields.Date(string="Birth Date", tracking=True)
    age = fields.Integer(string="Employee Age", compute="age_count", tracking=True, store=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", tracking=True)
    phone = fields.Char(string="Contact Number", tracking=True)
    address = fields.Char(string="Address", tracking=True)
    city =fields.Char(string="City", tracking=True)
    pin_code = fields.Char(string="Pin Code", tracking=True)
    education = fields.Char(string="Education", tracking=True)
    experience = fields.Char(string="Experience", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    emp_img = fields.Image(string="Employee Image")


    # Function
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.employee.sequence')
        return super(HospitalEmployee, self).create(vals)
    
    @api.depends('first_name','last_name')
    def employee_full_name(self):
        for rec in self:
            rec.name = (rec.first_name or '')+' '+(rec.last_name or '')

    @api.depends('date_of_birth')
    def age_count(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0