import streamlit as st
import datetime
from datetime import time
import pandas as pd
st.title('Análisis de datos')
tab1,tab2=st.tabs(['Análisis de las variables dinámicas en el tiempo','Análisis de líneas de la cara en el tiempo'])
st.sidebar.title('Panel de control')
files=st.sidebar.file_uploader('Carge un archivo por sesión en orden cronológico', type='csv', accept_multiple_files=True, label_visibility="visible")
n_files=['Sesión '+str(i+1) for i in range(len(files))]
SECTION=st.sidebar.selectbox(label='Seleccione una sesión:',options=n_files)
try:
    selected_file=n_files.index(SECTION)
    data=pd.read_csv(files[selected_file])
    data.dropna(inplace=True)
    data['Tiempo']=data.index*3
    data.dropna(inplace=True)
    t_max=max(data['Tiempo'])
    t_min=min(data['Tiempo'])
    t_min=datetime.timedelta(seconds=t_min)
    t_max=datetime.timedelta(seconds=t_max)
    t_min=t_min.total_seconds() / 60
    t_max=t_max.total_seconds() / 60
    SLIDER = st.sidebar.slider("Seleccione un rango de tiempo:", value=(t_min,t_max))
    st.sidebar.write("Rango seleccionado:", str(round(SLIDER[1]-SLIDER[0],2))+' '+'min')
except:
    pass
with tab1:
    st.bar_chart([3,5,6,7,1,8,2,7],color='#2dad9d')
with tab2:
    st.line_chart([3,5,6,7,1,8,2,7],color='#2dad9d')