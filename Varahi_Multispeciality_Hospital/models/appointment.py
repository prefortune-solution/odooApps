from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ="Hospital Appointments Details"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string="Patient Name", ondelete="restrict")
    gender = fields.Selection(related="patient_id.gender")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor Name")
    booking_time = fields.Datetime(string="Appointment Book Time", default=fields.Datetime.now)
    appointment_date = fields.Date(string="Appointment Date", default=fields.Date.context_today)
    ref = fields.Char(string="Ref", tracking=True)
    doc_note = fields.Html(string="Doc Note", tracking=True)
    # attender_id =fields.Many2one('hospital.employee', string="Attender Name")
    receptionist_id = fields.Many2one('res.users', string="Receptionist")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1','Low'),
        ('2','high'),
        ('3','Very High'),
        ('4','Critical')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation','Consulating'),
        ('done','Done'),
        ('cancel','Cancelled')], default="draft", string="Status", required=True)
    pharmacy_record_ids = fields.One2many("hospital.appointment.pharmacy", 'appointment_pharmacy_id', string="Pharmacy List") 

    # def unlink(self):
    #     if self.state != 'draft':
    #         raise ValidationError(_("Only Draft Appointment Delete"))
    #     super(HospitalAppointment, self).unlink()
       
    
    @api.model
    def create(self, vals):
        vals['receptionist_id'] = self.env.user.id
        return super(HospitalAppointment, self).create(vals)

    @api.onchange('patient_id')
    def patient_change_event(self):
        self.ref = self.patient_id.ref

    def object_button(self):
       return{
           'effect':{
                'fadeout': 'slow',
                'message': 'My Button Clicked',
                'type': 'rainbow_man'
           }
       }
    
    def whats_app_button(self):
        if not self.patient_id.phone:
            raise ValidationError(_("Patient Contact Number not Availble"))
        message = "Hi, %s Your Appointment Booked With Dr.%s On %s. Please Availble Before 15 Minute of Your Appointment Time" %(self.patient_id.name, self.doctor_id.name, self.appointment_date)
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.patient_id.phone, message)
        return{
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url
        }

    def state_btn_in_consultation(self):
        for rec in self:
            rec.state = "in_consultation"

    def state_btn_done(self):
        for rec in self:
            rec.state = "done"

    def state_btn_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def state_btn_draft(self):
        for rec in self:
            rec.state = "draft"



