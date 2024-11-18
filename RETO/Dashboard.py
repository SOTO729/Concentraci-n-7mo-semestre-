import streamlit as st
from datetime import time
st.title('Análisis de datos')
tab1,tab2=st.tabs(['Análisis de las variables dinámicas en el tiempo','Análisis de líneas de la cara en el tiempo'])
st.sidebar.title('Panel de control')
files=st.sidebar.file_uploader('Carge un archivo por sesión en orden cronológico', type='csv', accept_multiple_files=True, label_visibility="visible")
n_files=['Sesión '+str(i+1) for i in range(len(files))]
SECTION=st.sidebar.selectbox(label='Seleccione una sesión:',options=n_files)
SLIDER = st.sidebar.slider(
    "Seleccione un rango de tiempo:", value=(time(11, 30), time(12, 45))
)
with tab1:
    st.bar_chart([3,5,6,7,1,8,2,7],color='#2dad9d')
with tab2:
    st.line_chart([3,5,6,7,1,8,2,7],color='#2dad9d')

