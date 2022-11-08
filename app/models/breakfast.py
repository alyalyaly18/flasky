from app import db

class Breakfast(db.Model): # class inherits Model from SQLALChemy
    # define all of the attributes (columns) using static definition in class
    # SQLALchemy will know what to do
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    rating = db.Column(db.Float)
    prep_time = db.Column(db.Integer)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    menu = db.relationship('Menu', back_populates='breakfast_items')

    def to_dict(self):
    # self using a created instance 
        return {
            "id":self.id,
            "name":self.name,
            "rating":self.rating,
            "prep_time":self.prep_time,
            "menu_id":self.menu_id
        }
    # use function to pass through items in breakfast.py of routes

    @classmethod
    def from_dict(cls, breakfast_dict): # class method
    # cls populated with class itself (whole bfat class)
    # dict with information about breakfast coming in
    # use knowledge to create a breakfast (not based on a previous instance)
    # do have an overall class (concept) - use to think of how to create
    # take dictionary and use to create instance of bfast class
        return cls(
        name=breakfast_dict['name'],
        rating=breakfast_dict['rating'],
        prep_time=breakfast_dict['prep_time'],
        menu_id=breakfast_dict["menu_id"]
        )