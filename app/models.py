form app import db





class Commic(db.Model):
    __tablename__='comic'
    id=db.Column(db.Integer,primary_key=True)

    recommedations=db.relationship('Recommedation',backref='commics',lazy=dynamic)



class Recommedation(db.Model):
    __tablename__='recommedations'
    id=db.Column(db.Integer,primary_key=True)
    heading=db.Column(db.String(255),index=True)
    content=db.Column(db.Text)
    comic_id=db.Column(db.Integer,db.ForeignKey('commic.id'))

    def recommedation_save(self):
        db.session.add(self)
        db.session.commit()
