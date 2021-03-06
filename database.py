
import os

import sys

from sqlalchemy import Column, ForeignKey, Integer, String, true, false
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):

      __tablename__ = 'restaurant'

      name = Column( String(80), nullable = False )

      id = Column( Integer, primary_key = True )

class MenuItems(Base):

      __tablename__ = 'menu_item'

      name = Column( String(80), nullable = False )

      id = Column( Integer, primary_key = True )

      course = Column( String(250) )

      description = Column( String(250) )

      price = Column( String(8))

      restaurant_id = Column( Integer, ForeignKey( 'restaurant.id' ))

      restaurant = relationship( Restaurant )

      def serialize(self):
          return{
          'name' : self.name,
          'id'   : self.id,
          'course': self.course,
          'description': self.description,
          'price':self.price,
          'restaurant_id':self.restaurant_id,
         }

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
