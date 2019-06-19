from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

#Database Tables
class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Integer,  nullable=False)
    
    def __repr__(self):
        return self.description

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exp_description = db.Column(db.Text, nullable=False)
    exp_amount = db.Column(db.Integer,  nullable=False)
  
    def __repr__(self):
        return self.exp_description

