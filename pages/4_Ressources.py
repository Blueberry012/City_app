import streamlit as st
import pandas as pd

st.title("Bases de données")

st.image("image/map.png", width=250, use_column_width=False, clamp=True)

def afficher_data_dep():
    st.header("Données par département")
    data_dep = pd.read_excel('data/data_departement.xlsx')
    st.write(data_dep)

def afficher_data_meteo():
    st.header("Données météorologiques")
    data_meteo = pd.read_excel('data/meteo.xlsx')
    st.write(data_meteo)

def afficher_data_ville():
    st.header("Données par ville")
    data_ville = pd.read_excel('data/data_ville.xlsx')
    st.write(data_ville)

afficher_data_dep()
afficher_data_meteo()
afficher_data_ville()
