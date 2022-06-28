from flask import Flask, render_template


app = Flask(__name__)



from app.controllers import  default
from app.models import  tables

# colocar o site no ar


