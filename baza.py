import os
import time
from peewee import *

def  nowaBaza(file = "baza_" + time.strftime("%Y-%m-%d_%H-%M-%S")):
    file = file + ".db"
    if os.path.exists(file):
        os.remove(file)
# tworzymy instancję bazy używanej przez modele
    baza = SqliteDatabase(file)  # ':memory:'


"""class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza"""