from odoo import models, fields


class StudentStudent(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
   # prime_minister_name =fields.Char(string="prime_minister_name")
    age = fields.Integer(string='Age')
    photo = fields.Binary(string='Image')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
        string='Gender')
    student_dob = fields.Date(string="Date of Birth")
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
    subject_id = fields.Many2one('subject.subject', string="Subject")
    subject_ids = fields.One2many(
        'subject.subject', 'student_id', string="Subject")
    Student_id = fields.Many2one('company.company', string='Student id')
    Student_ide = fields.Many2one('state.state', string='Student ide')


class Subject(models.Model):
    _name = "subject.subject"
    _rec_name = 'name'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True)
    student_id = fields.Many2one('student.student', string="Student")

    def sdd(self):
        self.name = self.student_id.name
        print('rrrrrrrr')


class ButtonActionDemo(models.Model):
    _name = 'button.demo'
    _description = "button_action_demo"

    name = fields.Char(required=True, default='Click on generate name!')
    password = fields.Char(string="Password")
    first = fields.Integer(string="first", required=True)
    second = fields.Integer(string="second", required=True)
    result = fields.Char(string="Result")

    def generate_record_name(self):
        temp = self.name
        self.name = self.password
        self.password = temp
        print('output', self.name)

    def generate_record_password(self):
        self.password = self.password
        print("hello", self)

    def first_no(self):
        self.first = self.first
        print("first_no", self)

    def second_no(self):
        self.second = self.second
        print("second", self)

    def results(self):
        self.result = self.first + self.second
        self.result = self.result
        print("result", self)


class Company(models.Model):
    _name = 'company.company'
    _description = 'Company'

    name = fields.Char(string="name")

    owner = fields.Char(string="Owner")

    company_type = fields.Char(string='Company Type')
    company_name = fields.Char(string='Company Name')
    location = fields.Char(string='Location')
    total_employee = fields.Integer(string='Total Employee')
    hr_name = fields.Char(string='Hr Name')
    employee_id = fields.One2many(
        'student.student', 'Student_id', string="Student")

    def employee(self):
        self.owner = self.owner
        print("owner", self)

    def addd(self):
        self.name = self.employee_id.name
    print("hello")


class Government(models.Model):
    _name = 'government.government'
    _description = 'Government'
    _rec_name = 'prime_minister_name'

    country = fields.Many2one('res.country', string='Country')
    prime_minister_name = fields.Char(string='prime_minister_name')
    condition = fields.Char(string="condition")
    home_minister_name = fields.Char(string='Home Minister Name')
    defance_minister_name = fields.Char(string='Defance Minister name')
    it_minister_name = fields.Char(string='It Minister Name')
    capital = fields.Char(string='Capital')
    notes = fields.Text(string='Terms and Conditions')
    state = fields.One2many(
        'state.state', 'state', string='state')


class State(models.Model):
    _name = 'state.state'
    _description = 'State'

    state = fields.Many2one(
        'government.government', string='STATE')
    cheef_minister = fields.Char(string="Cheef Minister")
    education_minister = fields.Char(string="Education Minister")
    pa = fields.Char(string="P.A")
    dg = fields.Char(string="D.G")
    country = fields.Many2one('res.country', string="Country")
    student_ide = fields.One2many(
        'student.student', 'Student_ide', string="Student Ide")
