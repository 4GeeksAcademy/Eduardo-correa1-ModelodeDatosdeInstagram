import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

seguir = Table("seguir", Base.metadata,
               Column("seguidor_id", Integer, ForeignKey("usuarios.id"), primary_key=True),
               Column('seguido_id', Integer, ForeignKey('usuarios.id'), primary_key=True)

)

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    bio = Column(String(250), nullable=False)
    comentarios = relationship("Comentarios", backref="usuario", lazy=True)
    posts = relationship("Post", backref="usuario", lazy=True)
    likes = relationship("Likes", backref="usuario", lazy=True)
    seguidores = relationship("usuarios",
                              secondary=seguir,
                              primaryjoin=id==seguir.c.seguidor_id,
                              secondaryjoin=id==seguir.c.seguido_id,
                              backref='seguidos'
                              )

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    contenido = Column(String(250), nullable=False)
    image_url = Column(String(250), nullable=False)
    fecha = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('usuarios.id'))
    comentarios = relationship("Comentarios", backref="post", lazy=True)
    likes = relationship("Likes", backref="post", lazy=True)

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
