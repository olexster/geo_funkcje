import os

from datetime import date
from peewee import *
def  nowaBaza(file = "baza_" + str(date.today())):  # todo: domyślan nazawa pliku "data i godzina"
    # todo: zmienna godło
  file = file+".db"
    if os.path.exists(file):
        os.remove(file)
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase(file)  # ':memory:'


class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza