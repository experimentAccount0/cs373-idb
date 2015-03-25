from app import db

class Element(db.Model):
    atomic_number = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(3))
    name = db.Column(db.String(50))
    atomic_mass = db.Column(db.Float)
    history = db.Column(db.Text)
    group_column = db.Column(db.Integer, db.ForeignKey('group.column'))
    period_row = db.Column(db.Integer, db.ForeignKey('period.row'))
    trivias = db.relationship('Trivia',backref='element',lazy='dynamic')
    
    def __repr__(self):
        return '<Element %s. atomic_number = %d, symbol %s, atomic_mass = %s, group = %s, period = %d>' % (self.name, self.atomic_number,self.symbol,self.atomic_mass,self.group.name,self.period.row)

class Period(db.Model):
    row = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    properties = db.Column(db.Text)
    elements = db.relationship('Element',backref='period',lazy='dynamic')
    trivias = db.relationship('Trivia',backref='period',lazy='dynamic')

    def __init__(self, row, description="None", properties="None"):
        self.row = row
        self.description = description
        self.properties = properties

    def __repr__(self):
        return '<Period %s>' % self.row

class Group(db.Model):
    column = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    information = db.Column(db.Text)
    elements = db.relationship('Element',backref='group',lazy='dynamic')
    trivias = db.relationship('Trivia',backref='group',lazy='dynamic')
    
    def __init__(self, column,name, description="None", properties="None"):
        self.column = column
        self.name = name
        self.description = description
        self.properties = properties

    def __repr__(self):
        return '<Group %s>' % self.name

class Trivia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    group_column = db.Column(db.Integer, db.ForeignKey('group.column'))
    period_row = db.Column(db.Integer, db.ForeignKey('period.row'))
    element_atomic_number = db.Column(db.Integer, db.ForeignKey('element.atomic_number'))
    
    
    def __repr__(self):
        return '<Group %s>' % self.name