from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True)  #sql vars must match init vars below
      #sql vars must match init vars below
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy = 'dynamic') #wiht lazy now its query, everytime we call json method we look in items table to match id which is slower


    def __init__ (self,name):
        self.name = name      

    def json (self):
        return {
            'name': self.name,
            'items': [item.json() for item in self.items.all()]
        }

    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM __tablename__(which is items) WHERE name=name
            #it returns ItemModel object that has selfname and price
        
    
    def save_to_db (self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()