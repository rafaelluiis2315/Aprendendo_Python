from sre_parse import expand_template
from typing import Type
from PySimpleGUI import PySimpleGUI as sg
import mysql.connector

theme_name_list = sg.theme_list()
print(theme_name_list)