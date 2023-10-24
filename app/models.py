from datetime import datetime
from flask import url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    body = db.Column(db.Text)
    craeted_at = db.Column(db.DateTime , default=datetime.utcnow)
    updated_at = db.Column(db.DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    @classmethod
    def get_all_objects(cls):
        return cls.query.all()
    
    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create_post(cls , request_form):
        post = cls(**request_form)
        db.session.add(post)
        db.session.commit()
        return post
    
    @classmethod
    def get_spacific_post(cls , id):
        return cls.query.get_or_404(id)
    
    @property
    def get_image_url(self):
        return url_for('static' , filename=f'posts/images/{self.image}')
    
    @property
    def get_show_url(self):
        return url_for('posts.show' , id=self.id)
    
    @property
    def get_delete_url(self):
        return url_for('posts.delete' , id=self.id)