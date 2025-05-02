import streamlit as st
import pandas as pd
import pickle
import numpy as np
with open("model.pickle","rb") as m:
    modelo = pickle.load(m)

st.title('WAGE ANALISIS')
tab1, tab2, tab3 = st.tabs(['ANALISIS UNIVARIADO', 'ANALISIS BIVARIADO', 'MODELO'])


with tab1:
    st.header('ANALISIS UNIVARIADO')

    wage = pd.read_csv('wage.csv')



    import plotly.express as px


    fig_wage = px.histogram(wage, x="wage", nbins=40, title="Wage Distribution")
    fig_educ = px.histogram(wage, x="educ", nbins=40, title="Education Distribution")
    fig_exper = px.histogram(wage, x="exper", nbins=40, title="Experience Distribution")
    fig_gender = px.bar(wage['gender'].value_counts().reset_index(), x='gender', y='count', title='Gender Distribution') 
    fig_race = px.bar(wage['race'].value_counts().reset_index(), x='race', y='count', title='Race Distribution') 
    fig_married = px.bar(wage['married'].value_counts().reset_index(), x='married', y='count', title = 'Married Distribution')

    st.plotly_chart(fig_wage)
    st.plotly_chart(fig_educ)
    st.plotly_chart(fig_exper)
    st.plotly_chart(fig_gender)
    st.plotly_chart(fig_race)
    st.plotly_chart(fig_married)

with tab2:
    fig_educ_wage = px.scatter(wage, x="educ", y="wage", title="Education vs. Wage")
    fig_exper_wage = px.scatter(wage, x="exper", y="wage", title="Experience vs. Wage")

    st.plotly_chart(fig_educ_wage)
    st.plotly_chart(fig_exper_wage)


with tab3:

    st.title('modelo')

    educ= st.slider('seleccione su educacion', 0, 25)
    exper=st.slider('seleccione su experiencia', 0, 20)
    sexo = st.selectbox('sexo', ['F','M'])

    if sexo == 'F':
        sexo = 1
    else:
        sexo = 0

    raza = st.selectbox('raza',['white', 'no white'] )
    
    if raza == 'white':
        raza = 1
    else:
        raza = 0

    estado_civil = st.selectbox('estado civil',['married', 'no married'])

    if estado_civil == 'married':
        estado_civil = 1
    else:
        estado_civil = 0

    if st.button('predecir'):
        pred = modelo.predict(np.array([[educ, exper, sexo, raza, estado_civil]]))
        st.write(pred[0])



