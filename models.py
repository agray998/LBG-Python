from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

STRING = 40
TEXT = 240


class ItemModel(db.Model):
    """
    ItemModel class for ORM
    """
    __tablename__ = "items"

    _id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(TEXT))
    name = db.Column(db.String(STRING))
    price = db.Column(db.Float())

    def __init__(self, _id: int, description: str, name: str, price: float):
        """
        class constructor
        """
        self.description = description
        self.name = name
        self.price = price
        self._id = _id

    def __str__(self) -> str:
        """
        string representation method for object
        """
        return f"'description':{self.description},'name':{self.name},'price':{self.price},'_id':{self._id}"

    @property
    def serialize(self):
        """
        serializable format for object
        """
        return {
            'description': self.description,
            'name': self.name,
            'price': self.price,
            '_id': self._id
        }
