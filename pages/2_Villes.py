import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium


# Charger les données à partir du fichier CSV
df = pd.read_excel('data/data_ville.xlsx')
df.dropna(subset=['Latitude'], inplace=True)
df.dropna(subset=['Longitude'], inplace=True)
df = df[df['Population'] >= 20000]

st.set_page_config(layout="wide")


def France(dataframe):
    center = [46.603354, 2.668561]
    zoom = 6
    ville_data = dataframe
    rad = 10
    return center, zoom, ville_data, rad


def Ville(dataframe, ville):
    ville_data = dataframe[dataframe['Ville'] == ville]
    center = [ville_data['Latitude'].mean(), ville_data['Longitude'].mean()]
    zoom = 13
    rad = 50
    return center, zoom, ville_data, rad


def circle_marker(map, row, rad, icon_color, popup):
    folium.CircleMarker(location=[row['Latitude'], row['Longitude']],
                        stroke=False,
                        radius=rad,
                        color=icon_color,
                        fill=True,
                        fill_color=icon_color,
                        fill_opacity=0.7,
                        popup=popup,
                        icon=folium.Icon(color=icon_color, icon='')).add_to(map)


def display_kpi_metrics2(ville_data, indicateur):
    taux_indicateurs = []
    other_indicateurs = []

    for indicator in indicateur:
        if "Taux" in indicator or "Part" in indicator or "Température" in indicator or "Température" in indicator or "Précipitations" in indicator or "Loyer" in indicator or "vent" in indicator or "Proportion" in indicator:
            taux_indicateurs.append(indicator)
        else:
            other_indicateurs.append(indicator)

    print(other_indicateurs)
    taux_kpi = ville_data[taux_indicateurs].mean()
    taux_kpi = {col: round(value, 2) for col, value in taux_kpi.items()}

    for col, value in taux_kpi.items():
        if 'Taux' in col or "Part" in col or "Proportion" in col:
            taux_kpi[col] = str(value) + '%'
        elif 'Température' in col:
            taux_kpi[col] = str(value) + '(°C)'
        elif 'Précipitations' in col:
            taux_kpi[col] = str(value) + 'mm'
        elif 'vent' in col:
            taux_kpi[col] = str(value) + 'm/s'
        elif 'Loyer' in col:
            taux_kpi[col] = str(value) + '€'
    taux_kpi = list(taux_kpi.values())

    other_kpi = ville_data[other_indicateurs].sum().tolist()
    other_kpi = [int(value) for value in other_kpi]
    kpi = taux_kpi + other_kpi
    kpi_name =  taux_indicateurs + other_indicateurs

    num_kpis = len(kpi_name)
    num_rows = (num_kpis + 1) // 2
    columns = st.columns(2)

    for i in range(num_rows):
        columns[0].metric(kpi_name[2*i], (kpi[2*i]))
        if 2*i + 1 < num_kpis:
            columns[1].metric(kpi_name[2*i + 1], (kpi[2*i + 1]))


def display_kpi_metrics3(ville_data, indicateur):
    taux_indicateurs = []
    other_indicateurs = []

    for indicator in indicateur:
        if "Taux" in indicator or "Part" in indicator or "Température" in indicator or "Température" in indicator or "Précipitations" in indicator or "Loyer" in indicator or "vent" in indicator or "Proportion" in indicator:
            taux_indicateurs.append(indicator)
        else:
            other_indicateurs.append(indicator)

    print(other_indicateurs)
    taux_kpi = ville_data[taux_indicateurs].mean()
    taux_kpi = {col: round(value, 2) for col, value in taux_kpi.items()}

    for col, value in taux_kpi.items():
        if 'Taux' in col or "Part" in col or "Proportion" in col:
            taux_kpi[col] = str(value) + '%'
        elif 'Température' in col:
            taux_kpi[col] = str(value) + '(°C)'
        elif 'Précipitations' in col:
            taux_kpi[col] = str(value) + 'mm'
        elif 'vent' in col:
            taux_kpi[col] = str(value) + 'm/s'
        elif 'Loyer' in col:
            taux_kpi[col] = str(value) + '€'
    taux_kpi = list(taux_kpi.values())

    other_kpi = ville_data[other_indicateurs].sum().tolist()
    other_kpi = [int(value) for value in other_kpi]
    kpi = taux_kpi + other_kpi
    kpi_name =  taux_indicateurs + other_indicateurs

    num_kpis = len(kpi_name)
    num_rows = (num_kpis + 2) // 3
    columns = st.columns(3)

    for i in range(num_rows):
        columns[0].metric(kpi_name[3*i], (kpi[3*i]))
        if 3*i + 1 < num_kpis:
            columns[1].metric(kpi_name[3*i + 1], (kpi[3*i + 1]))
        if 3*i + 2 < num_kpis:
            columns[2].metric(kpi_name[3*i + 2], (kpi[3*i + 2]))



def main():
    st.markdown("<h1 style='text-align: center;'>Carte Ville</h1>", unsafe_allow_html=True)

    versus = st.sidebar.toggle('Versus')

    villes = df['Ville'].tolist()
    villes = sorted(villes)
    villes.insert(0, "France")

    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)



    domaine = ["Démographie","Economie","Emploi","Education","Mobilité","Logement","Services"]
    selected_domaine = st.sidebar.selectbox('Choisir un domaine', domaine)
    data1=df


    if selected_domaine =="Démographie":
        indicateur = ['Population']
    

    elif selected_domaine =="Economie":
        indicateur = ["Nombre d'entreprises",
                      "Nombre d'entreprises (Industrie)",
                      "Nombre d'entreprises (Construction)",
                      "Nombre d'entreprises (Commerce, transp., héberg. et restauration)",
                      "Nombre d'entreprises (Information et communication)",
                      "Nombre d'entreprises (Act. financières et assurance)",
                      "Nombre d'entreprises (Act. Immobilières)",
                      "Nombre d'entreprises (Act. scient. & techn., act. de serv. admi.)",
                      "Nombre d'entreprises (Adm. publ, enseign, santé, action sociale)",
                      "Nombre d'entreprises (Autres act. de services)"]


    elif selected_domaine =="Emploi":
        indicateur = ["Nombre d'actifs",
                      "Nombre d'inactifs",
                      "Nombre d'actifs occupés de 15-64 ans",
                      "Nombre de chômeurs",
                      "Taux d'activité des 15-64 ans",
                      "Taux d'emploi des 15-64 ans",
                      "Taux de chômage des 15-64 ans"]


    elif selected_domaine =="Revenu":
        indicateur = ["Taux d'épargne brute",
                      "Montant d'épargne brute",
                      "Médiane du revenu disponible",
                      "Part des revenus d'activité",
                      "Taux de pauvreté"]


    elif selected_domaine =="Education":
        indicateur = ["Nombre d'écoles maternelles",
                      "Nombre d'écoles élémentaires",
                      "Nombre de collèges",
                      "Nombre de lycées (général, technologique et/ou professionnel)",
                      "Effectif des établissements d'enseignement supérieur",
                      "Part des titulaires d'un diplôme de l'enseignement supérieur"]

    
    elif selected_domaine =="Mobilité":
        indicateur = ["Part des déplacements en voiture",
                      "Part des déplacements en transports en commun",
                      "Part des déplacements en deux roues",
                      "Proportion d'actifs occupés résidant à 30 minutes ou plus de leur lieu de travail"]

    
    elif selected_domaine =="Logement":
        indicateur = ["Nombre de logements",
                      "Nombre de logements vacants",
                      "Part des logements vacants",
                      "Loyer d'annonce par m² pour un appartement",
                      "Loyer d'annonce par m² pour une maison"]

    
    elif selected_domaine =="Services":
        indicateur = ["Nombre de licenciés sportifs",
                      "Nombre de cinémas",
                      "Nombre de structures France Services"]

    selected_indicateur = st.sidebar.selectbox('Choisir un indicateur', indicateur)
    data = data1[[selected_indicateur,'Latitude','Longitude','Ville']]
    

    if selected_indicateur=="Nombre de cinémas" or selected_indicateur=="Nombre de structures France Services":
        data['Catégorie'], bins =  pd.qcut(data[selected_indicateur].rank(method='first'), 3, retbins=True, labels=False)
    else:
        data['Catégorie'], bins =  pd.qcut(data[selected_indicateur], 3, labels=False, retbins=True)

    quantile_ranges = []
    for start, end in zip(bins[:-1], bins[1:]):
        start, end = int(start), int(end)
        formatted_range = f"{start} à {end}"
        quantile_ranges.append(formatted_range)

    data["Catégorie"] = data["Catégorie"].astype(str)

    purpose_colour = {
        '0': '#55E2E9',
        '1': '#0496C7',
        '2': '#02367B'
    }

    categ = st.sidebar.radio('Répartition',('Tous',
                                            quantile_ranges[0],
                                            quantile_ranges[1],
                                            quantile_ranges[2]))



    if versus:
        col1, col2 = st.columns(2)

        with col1:
            ville1 = st.selectbox("Choisissez une ville", villes, key='ville1')
            if ville1=="France":
                center1, zoom1, ville_data1, rad1 = France(df)
                zoom1=5

            else:
                center1, zoom1, ville_data1, rad1 = Ville(df, ville1)

            map1 = folium.Map(location=center1, zoom_start=zoom1, control_scale=True)

        with col2:
            ville2 = st.selectbox("Choisissez une ville", villes, key='ville2')
            if ville2=="France":
                center2, zoom2, ville_data2, rad2 = France(df)
                zoom2=5

            else:
                center2, zoom2, ville_data2, rad2 = Ville(df, ville2)

            map2 = folium.Map(location=center2, zoom_start=zoom2, control_scale=True)



    else:
        ville = st.selectbox("Choisissez une ville", villes, key='ville')
        if ville=="France":
            center, zoom, ville_data, rad = France(df)

        else:
            center, zoom, ville_data, rad = Ville(df, ville)

        map = folium.Map(location=center, zoom_start=zoom, control_scale=True)


    if versus:
        with col1:
            display_kpi_metrics2(ville_data1, indicateur)
            st.subheader(selected_indicateur)
            color1,color2,color3=st.columns(3)
            with color1:
                st.color_picker(quantile_ranges[0],'#55E2E9',key=color1)
            with color2:
                st.color_picker(quantile_ranges[1],'#0496C7',key=color2)
            with color3:
                st.color_picker(quantile_ranges[2],'#02367B',key=color3)
        with col2:
            display_kpi_metrics2(ville_data2, indicateur)
            st.subheader(selected_indicateur)
            color1,color2,color3=st.columns(3)
            with color1:
                st.color_picker(quantile_ranges[0],'#55E2E9',key=color1)
            with color2:
                st.color_picker(quantile_ranges[1],'#0496C7',key=color2)
            with color3:
                st.color_picker(quantile_ranges[2],'#02367B',key=color3)
    else:
        display_kpi_metrics3(ville_data, indicateur)
        st.subheader(selected_indicateur)
        color1,color2,color3=st.columns(3)
        with color1:
            st.color_picker(quantile_ranges[0],'#55E2E9',key=color1)
        with color2:
            st.color_picker(quantile_ranges[1],'#0496C7',key=color2)
        with color3:
            st.color_picker(quantile_ranges[2],'#02367B',key=color3)


    data2=data
    if categ == quantile_ranges[0]:
        data2=data2[(data2['Catégorie']== '0')]
    elif categ == quantile_ranges[1]:
        data2=data2[(data2['Catégorie']== '1')]
    elif categ == quantile_ranges[2]:
        data2=data2[(data2['Catégorie']== '2')]
    else:
        data2=data

    
    if versus:
        with col1:
            for i,row in data2.iterrows():
                content = f'Ville : {str(row["Ville"])}<br>' f'{selected_indicateur} : {str(row[selected_indicateur])}'
                iframe = folium.IFrame(content, width=400, height=55)
                popup = folium.Popup(iframe, min_width=400, max_width=500)
                        
                try:
                    icon_color = purpose_colour[row['Catégorie']]
                except:
                    icon_color = 'gray'
                circle_marker(map1, row, rad1, icon_color, popup)

        with col2:
            for i,row in data2.iterrows():
                content = f'Ville : {str(row["Ville"])}<br>' f'{selected_indicateur} : {str(row[selected_indicateur])}'
                iframe = folium.IFrame(content, width=400, height=55)
                popup = folium.Popup(iframe, min_width=400, max_width=500)
                        
                try:
                    icon_color = purpose_colour[row['Catégorie']]
                except:
                    icon_color = 'gray'
                circle_marker(map2, row, rad2, icon_color, popup)
    else:
        for i,row in data2.iterrows():
            content = f'Ville : {str(row["Ville"])}<br>' f'{selected_indicateur} : {str(row[selected_indicateur])}'
            iframe = folium.IFrame(content, width=400, height=55)
            popup = folium.Popup(iframe, min_width=400, max_width=500)
                        
            try:
                icon_color = purpose_colour[row['Catégorie']]
            except:
                icon_color = 'gray'
            circle_marker(map, row, rad, icon_color, popup)
    
    if versus:
        with col1:
            st_folium(map1, height=500, width=500, key='map1')
        with col2:
            st_folium(map2, height=500, width=500, key='map2')
    else:
        st_folium(map, height=650, width=1050, key='map')


if __name__ == "__main__":
    main()
