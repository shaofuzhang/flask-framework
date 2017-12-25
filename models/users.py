from models.baseModel import db


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    user_pwd = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='customer')


    def __repr__(self):
        return '<User %r>' % self.user_name
