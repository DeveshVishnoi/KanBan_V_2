from application.database import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    email_id = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    lists = db.relationship("List",backref= "user",lazy = True)
    # randn = db.Column(db.String, nullable=False, unique=True)

    # def __repr__(self) -> str:
    #     return f"{self.user_idd}-{self.randn}"


class List(db.Model):
    __tablename__ = 'list'
    list_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.user_id"), nullable=False)
    cards = db.relationship("Card",backref= "list",lazy = True)    

    # def __repr__(self) -> str:
    #     return f"{self.list_id}"


class Card(db.Model):
    __tablename__ = 'cards'
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_title = db.Column(db.String(50), nullable=False)
    card_desc = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.String(), nullable=False)
    completed = db.Column(db.String(), default=False)
    last_seen=db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.user_id"), nullable=False)

    list_id = db.Column(db.Integer, db.ForeignKey(
        "list.list_id"), nullable=False)

    def __repr__(self) -> str:

        return f"{self.card_title} - {self.deadline} - {self.completed} - {self.list_id}"
