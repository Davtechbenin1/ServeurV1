#Coding:utf-8

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
try:
	from base_hand import *
except ImportError:
	from .base_hand import *

import json

app = FastAPI()

class data_form(BaseModel):
	data:dict

class date_data(BaseModel):
	date:str
	fichier:str
	data:dict

general_data = Get('Général')

# Gestion des données de la base général
@app.get("/Général/{fichier}")
async def read_general(fichier: str):
	return general_data.get(fichier,dict())

@app.get("/Général")
async def read_all_general():
	return general_data

@app.put('/Général/{fichier}')
async def put_general(fichier : str, data: dict):
	general_data[fichier] = data
	Update("Général",fichier,data)
	return {"Message":'Donnée ajouter'}

# Gestion des données en détails
"""
	Ici, on suppose que le fichier est combiné
	avec la date
"""
@app.get("/Détails/{fichier}")
async def read_details(fichier: str):
	return Get(fichier)


@app.put("/Détails/{fichier}")
async def put_details(fichier : str, data: dict):
	Save(fichier,data)
	return {"Méssage":"Donnée ajouter"}



