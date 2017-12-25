from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer,DATETIME
from flask_sqlalchemy import SQLAlchemy, Model


class BaseModel(Model):
    create_date = Column(DateTime, default=datetime.utcnow())
    create_user = Column(String(50), default='')
    is_deleted = Column(Integer, default=0)

    def to_dict(self):
        columns = self.__table__.columns.keys()
        return {key: getattr(self, key) for key in columns}


db = SQLAlchemy(model_class=BaseModel)
