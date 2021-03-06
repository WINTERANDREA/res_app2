from app import db
from sqlalchemy.dialects.postgresql import TIME



class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_username = db.Column(db.String(20), nullable=False)
    r_password = db.Column(db.String(200), nullable=False)
    r_name = db.Column(db.String(50), nullable = False)
    r_adress = db.Column(db.String(100), nullable = False)
    r_ownername = db.Column(db.String(50), nullable = False)
    r_key = db.Column(db.String(15), nullable = False, unique= True)
    r_reservations = db.relationship('Reservations', backref = 'restaurant')
    r_dsettings = db.relationship('ReSettings', backref = 'restaurant')
    
    def __repr__(self):
        return "{}".format(self.r_key)

class Reservations(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    s_day = db.Column(db.Date, nullable = False)
    s_freespot = db.Column(db.Integer, nullable = False)
    s_freespot_total = db.Column(db.Integer, nullable = False)
    s_r_id = db.Column(db.String(15), db.ForeignKey('restaurants.r_key'), nullable=False)

class ReSettings(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    d_days = db.Column(db.Integer, nullable = False)
    d_close = db.Column(db.Boolean, nullable = False)
    d_open_time = db.Column(TIME, nullable = False)
    d_close_time = db.Column(TIME, nullable = False)
    d_freespot_max = db.Column(db.Integer, nullable = False)
    d_r_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)


