import streamlit as st 
import altair as alt
import plotly.express as px 

# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime
import json
import requests

url1 = 'https://recommend-cosinus-app.azurewebsites.net/api/HttpTrigger1'
url2 = 'https://recommendmodelapp.azurewebsites.net/api/HttpTrigger1'




st.title("Application de recommandation de contenu based content")
resultat = []
txt_widget1 = st.empty()
user_input = txt_widget1.text_input("Entrez un User_id pour obtenir 5 recommandation de livres")


st.title("Result Input - Modèle")
resultat = []

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
serialized_as_json = json.dumps({"user_id":user_input})
response = requests.post(url1, data=serialized_as_json, headers=headers)
if response.status_code == 200:
        resultat = response.text
if resultat != []:
    st.write(resultat)


st.title("Application de recommandation de collaborative filtering")
resultat_cf = []
#text = st.text_area("Écrivez ici pour savoir si votre texte a un sentiment négatif ou positif")

txt_widget2 = st.empty()
user_input_cf = txt_widget2.text_input("Entrez un User_id pour obtenir 5 recommandation de livres", key="key2")


st.title("Result Input - Modèle")
resultat_cf = []

headers_cf = {'Content-type': 'application/json', 'Accept': 'text/plain'}
serialized_as_json_cf = json.dumps({"user_id":user_input_cf})
response_cf = requests.post(url2, data=serialized_as_json_cf, headers=headers_cf)
if response_cf.status_code == 200:
    resultat_cf = response_cf.text
if resultat_cf != []:
    st.write(resultat_cf)
