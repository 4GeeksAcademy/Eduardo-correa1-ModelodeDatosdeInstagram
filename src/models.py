import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    bio = Column(String(250), nullable=False)
    comentarios = relationship("Comentarios", backref = "usuarios",lazy = True)
    post = relationship("Post", backref = "usuarios",lazy = True)
      



class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    contenido = Column(String(250), nullable=False)
    image_url = Column(String(250), nullable=False)
    fecha = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('usuarios.id'))


class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    contenido = Column(String(250), nullable=False)    
    fecha = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('usuarios.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)    
    user_id = Column(Integer, ForeignKey('usuarios.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
