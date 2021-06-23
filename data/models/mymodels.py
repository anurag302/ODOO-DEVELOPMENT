from odoo import models, fields


class Prodect(models.Model):
    _name = 'prodect.prodect'
    _description = 'Product'

    name = fields.Char(string='Name', required=True)
    photo = fields.Binary(string='Photo')
    header = fields.Char(string='Header')
    prodect_details = fields.Char(string='Prodect details')
    company = fields.Many2one('res.company', string='company')
    date_order = fields.Datetime(
        'purchase', required=True, default=fields.Datetime.now)
    price_total = fields.Float(string='Ammount')
    receipt_no = fields.Integer(string='Receipt no')
    product_type = fields.Selection([('applience', 'Home Applience'), (
        'applience', 'Kitchen Applience')],
        required=True, string='product type')


class Resume(models.Model):
    _name = 'resume.resume'
    _description = 'Resume'

    name = fields.Char(string='Name', required=True)
    photo = fields.Binary(string='Photo')
    brother = fields.Char(string="Brother")

    father_name = fields.Char(string='Father Name', required=True)
    mother_name = fields.Char(string='mother name', required=True)
    qualification = fields.Selection([('m', 'MCA'), ('m', 'M.SC'), (
        'm', 'MA'), ('b', 'BCA'), ('b', 'B.SC'), ('b', 'B.COM'), ('b', 'BA')])
    college = fields.Char(string='College', required=True)
    dob = fields.Date(string='Date', required=True)
    address = fields.Char(string='Address', required=True)
    hobbies_id = fields.Many2one('hobbies.hobbies', string='Hobbies')
    family_id = fields.One2many(
        'myfamily.myfamily', 'brother_id', string='brother')


class Hobbies(models.Model):
    _name = "hobbies.hobbies"
    _rec_name = 'name'
    _description = 'Hobbies'

    name = fields.Char(string='Name', required=True)


class MyFamily(models.Model):
    _name = 'myfamily.myfamily'
    _description = 'MyFamily'

    name = fields.Char(string="Name")
    father_name = fields.Char(string="Father Name")
    photo = fields.Binary(string='Photo')

    mother_name = fields.Char(string="Mother Name")
    grand_father = fields.Char(string="Grand Father")
    brother = fields.Char(string="Brother")
    sister = fields.Char(string="Sister")

    my_age = fields.Integer(string="Age")
    my_marks = fields.Float(string="Marks")
    country = fields.Many2one('res.country', required=True)
    state = fields.Many2one('res.country.state', required=True)
    brother_id = fields.Many2one('resume.resume', string='Brother')


class Developer(models.Model):
    _name = 'developer.developer'
    _description = 'Developer'

    ceo = fields.Char(string="CEO")
    photo = fields.Binary(string='Photo')

    manager = fields.Char(string="Manager")
    team_member = fields.Integer(string="Team Member")
    team_leader = fields.Char(string="Team Leader")
    technology = fields.Selection(
        [('p', 'Python'), ('j', 'Java'), ('c', 'C++'), ('r', 'Ruby')])
    python_developer_total = fields.Integer(string="Python Developer Total")
    java_developer_total = fields.Integer(string="Java Developer Total")
    country = fields.Many2one('res.country', string="Country")


class Record(models.Model):
    _name = "record.record"
    _description = "Record"

    name = fields.Char(string='Name', required=True)
    middle_name = fields.Char(string='Middle Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    photo = fields.Binary(string='Photo')
    student_age = fields.Integer(string='Age')
    student_dob = fields.Date(string="Date of Birth")
    student_gender = fields.Selection(
        [('ma', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
