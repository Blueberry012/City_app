import streamlit as st
print(st.__version__)

CURRENT_THEME = "blue"
IS_DARK_THEME = True

st.set_page_config(layout="wide")

st.title('Application City Fighting')

st.header("Bienvenue sur City Fighting !")

st.image("image/map.png", width=250, use_column_width=False, clamp=True)

st.subheader("Qu'est-ce que City Fighting ?")

st.write("City Fighting est une application web qui vous permet de comparer différentes villes françaises sur une variété d'aspects importants pour vous aider à prendre une décision éclairée pour votre prochain déménagement. Que vous recherchiez un nouvel emploi, un meilleur climat, des activités culturelles dynamiques ou simplement un changement de cadre de vie, City Fighting vous fournit les données nécessaires pour comparer les options qui s'offrent à vous.")

st.subheader("Pourquoi utiliser City Fighting ?")

st.write("Comparaison facile: Notre interface conviviale vous permet de comparer rapidement les villes sur une multitude de critères, des données économiques aux informations sur le logement en passant par la météo et plus encore.")

st.write("Données fiables: Nous utilisons des sources de données ouvertes et vérifiées pour vous fournir des informations précises et à jour sur chaque ville.")

st.write("Prise de décision informée: En ayant accès à une gamme variée de données sur chaque ville, vous pouvez prendre une décision éclairée et trouver l'endroit qui correspond le mieux à vos besoins et à vos préférences.")

st.divider()

st.write("N'hésitez pas à parcourir notre application pour trouver la ville qui vous correspond.")
