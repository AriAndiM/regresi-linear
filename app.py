import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

logo = Image.open('makam.jpg')
st.image(logo, caption='')

pilih_bulan = st.selectbox(
    'Pilih Bulan',
    ('1', '2', '3', '4 ', '5', '6', '7', '8', '9', '10', '11', '12'))
btn = st.button('Prediksi')
if btn:
    df = pd.read_csv('https://raw.githubusercontent.com/AriAndiM/dataset/main/data-pariwisata-syaikhona.csv')
    X = df['Bulan']
    y = df['Jumlah']
    X = X.values.reshape(-1, 1)
    y = y.values.reshape(-1, 1)

    # Membuat objek model Linear Regression
    model = LinearRegression()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1,shuffle=False)
    # Melatih model
    model.fit(X_train, y_train)
    # Membuat prediksi pada data testing
    # y_pred = model.predict(X_test)
    bulan = int(pilih_bulan)
    if bulan==1:
        b = 'januari'
    elif bulan==2:
        b = 'februari'
    elif bulan==3:
        b = 'maret'
    elif bulan==4:
        b='april'
    elif bulan==5:
        b = 'mei'
    elif bulan==6:
        b = 'juni'
    elif bulan==7:
        b='juli'
    elif bulan==8:
        b = 'agustus'
    elif bulan==9:
        b = 'september'
    elif bulan==10:
        b='oktober'
    elif bulan==11:
        b = 'november'
    elif bulan==12:
        b = 'desember'

    y_pred = model.predict([[bulan]])
    hasil = int(y_pred[0])
    st.write('Prediksi pengunjung pada bulan', b,'sebanyak :', hasil, 'pengunjung')