# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import pandas as pd
import accessAPI as servicio
import json

st.header("FORMULARIO PARA SOLICITAR CRÉDITO")
st.subheader("Datos generales")
st.write("Llena todos los datos para determinar si eres apto para recibir el crédito:")
df = pd.read_csv('Herramientas3_2023_banco.csv.csv')

Ccol1, Ccol2 = st.columns(2)
with Ccol1:
    # Campo alojamiento
    listaCasa = df["housing"].unique().tolist()
    housing = st.selectbox(
        '¿Tienes casa propia? (housing: yes)',
        (listaCasa))
with Ccol2:
    # Campo contacto
    listaCont = df["contact"].unique().tolist()
    contact = st.selectbox(
        'Ingresa un tipo de contacto (contact: cellular)',
        (listaCont))

# Campo trabajo
listaTrabajo = df["job"].unique().tolist()
job = st.selectbox(
    'Selecciona un trabajo de la lista (job: unknow)',
    (listaTrabajo))

# Campo estado civil
listaEstado = df["marital"].unique().tolist()
marital = st.selectbox(
    '¿Cuál es tu estado civil? (marital: single)',
    (listaEstado))

# Campo estudios
listaEstudios = df["education"].unique().tolist()
education = st.selectbox(
    'Selecciona tu grado máximo de estudios (education: high.school)',
    (listaEstudios))

# Campo edad
listaEdad = df["age"].unique().tolist()
minEdad = min(listaEdad)
mayEdad = max(listaEdad)
age = st.slider('Elige una edad en el siguiente rango (age: 25)', minEdad, mayEdad, 30)

# Campo duracion
listaDur = df["duration"].unique().tolist()
minDur = min(listaDur)
mayDur = max(listaDur)
duration = st.slider('¿Cuántos días consideras que te tardarías en liquidar tu deuda? (duration: 4900)', minDur, mayDur)

# Campo veces
listaVeces = df["campaign"].unique().tolist()
minVez = min(listaVeces)
mayVez = max(listaVeces)
campaign = st.slider('Contando esta, ¿Cuántas veces nos solicitarías un crédito? (campaign: 50)', minVez, mayVez)

st.subheader("Antecedentes")

Bcol1, Bcol2 = st.columns(2)
with Bcol1:
    # Campo prestamo
    listaPrest = df["loan"].unique().tolist()
    loan = st.selectbox(
        '¿Has solicitado antes un préstamo? (loan: yes)',
        (listaPrest))
with Bcol2:
# Campo default
    listaDef = df["default"].unique().tolist()
    default = st.selectbox(
        '¿Has estado en buró de crédito? (default: yes)',
        (listaDef))

# Campo poutcome
listaPout = df["poutcome"].unique().tolist()
poutcome = st.selectbox(
    'Estado de tu última solicitud de crédito (poutcome: nonexistent)',
    (listaPout))

st.subheader("Campos de configuración")

listaPDays = df["pdays"].unique().tolist()
minDur = min(listaPDays)
mayDur = max(listaPDays)
pdays = st.slider('Días mínimos de pago (pdays: 500)', minDur, mayDur)

Acol3, Acol4 = st.columns(2)
# Campo default
with Acol3:
    listaMes = df["month"].unique().tolist()
    month = st.selectbox(
        'Ingresa un mes disponible (month: jan)',
        ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
with Acol4:
    listaPrev = df["previous"].unique().tolist()
    previous = st.selectbox(
        'Pagos al mes (previous: 5)',
        (listaPrev))

listaZ = df["emp.var.rate"].unique().tolist()
minZ = min(listaZ)
mayZ = max(listaZ)
emp = st.slider('emp.var.rate: (1)', minZ, mayZ)

listaX = df["cons.price.idx"].unique().tolist()
minX = min(listaX)
mayX = max(listaX)
cons = st.slider('cons.price.idx: (94)', minX, mayX)

listaU = df["nr.employed"].unique().tolist()
minU = min(listaU)
mayU = max(listaU)
nr = st.slider('nr.employed: (5001)', minU, mayU)

st.caption("** Los campos con valores entre paréntesis sirven de guía para ejecutar una prueba positiva.")

if st.button('CALCULAR'):
    result=servicio.llamarservicio(age, job, marital, education, default, housing, loan, contact, month, duration, campaign, pdays, previous, poutcome, emp, cons, nr)
    result_dict = json.loads(result.decode("utf-8"))
    resultado = result_dict["Results"][0]
    if resultado == "yes":
        st.success("ERES APTO PARA RECIBIR EL CRÉDITO  =)")
    else:
        st.error("LO SENTIMOS, NO ERES APTO PARA EL CRÉDITO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
