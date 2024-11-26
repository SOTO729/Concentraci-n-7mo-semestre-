import streamlit as st
import datetime
import numpy as np
from datetime import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
plt.style.use('dark_background')
#@st.cache
PATIENT=st.sidebar.selectbox(label='Eliga un paciente:',options=['Paciente 1','Paciente 2','Paciente 3'])
def times(data):
    data['Tiempo']=data.index*3
    data.dropna(inplace=True)
    data['Tiempo']=data['Tiempo'].apply(lambda x: datetime.timedelta(seconds=x).total_seconds() / 60)
    return data
def filter(minn,maxx):
    if 'Paciente 1' in PATIENT:
        from config import df1p1
        from config import df2p1
        from config import df3p1
        from config import df4p1
        df1 = times(df1p1)
        df2 = times(df2p1)
        df3 = times(df3p1)
        df4 = times(df4p1)
    elif 'Paciente 2' in PATIENT:
        from config import df1p2
        from config import df2p2
        from config import df3p2
        from config import df4p2
        df1 = times(df1p2)
        df2 = times(df2p2)
        df3 = times(df3p2)
        df4 = times(df4p2)
    elif 'Paciente 3' in PATIENT:
        from config import df1p3
        from config import df2p3
        from config import df3p3
        from config import df4p3
        df1 = times(df1p3)
        df2 = times(df2p3)
        df3 = times(df3p3)
        df4 = times(df4p3)
    df1= df1[(df1['Tiempo'] >= minn) & (df1['Tiempo'] <= maxx)]
    df2 = df2[(df2['Tiempo'] >= minn) & (df2['Tiempo'] <= maxx)]
    df3 = df3[(df3['Tiempo'] >= minn) & (df3['Tiempo'] <= maxx)]
    df4 = df4[(df4['Tiempo'] >= minn) & (df4['Tiempo'] <= maxx)]
    return df1,df2,df3,df4
#st.set_page_config(page_title='Análisis de datos',layout="wide")
#st.title('Análisis de datos')
#tab1,tab2=st.tabs(['Análisis de variables en el tiempo','Análisis comparativo'])
#st.sidebar.title('Panel de control')
st.sidebar.empty()
df1,df2,df3,df4=filter(0,1e70)
lista=[df1,df2,df3,df4]
maxim=[]
for df in lista:
    maxim.append(max(df['Tiempo']))
SLIDER = st.sidebar.slider("Seleccione un rango de tiempo:", value=(0.0,min(maxim)))
st.sidebar.write("Tiempo seleccionado:\n", str(round(SLIDER[1]-SLIDER[0],2))+' '+'min')
df1,df2,df3,df4=filter(float(SLIDER[0]),float(SLIDER[1]))

import streamlit as st

col1, col2 = st.columns(2)
def pir(dfg):
    # Filtros para derecho e izquierdo
    derecho = dfg[['F1EBX', 'F4EBX', 'F5EEX', 'F8EIX', 'F14EV', 'F9EEX', 'F11EX', 'F15MS', 'F19MH', 'F17MS']]
    izquierdo = dfg[['F2EBS', 'F3EBS', 'F6EES', 'F7EIS', 'F13EV', 'F12ES', 'F10ES', 'F16MX', 'F20MH', 'F18MX']]

    # Estandarización de las columnas numéricas
    scaler = StandardScaler()
    derecho_normalized = pd.DataFrame(scaler.fit_transform(derecho), columns=derecho.columns)
    izquierdo_normalized = pd.DataFrame(scaler.fit_transform(izquierdo), columns=izquierdo.columns)

    # Contar cruces por cero para cada columna
    cross_zero_counts_derecho = [
        ((derecho_normalized[col].shift(1) * derecho_normalized[col]) < 0).sum()
        for col in derecho_normalized.columns
    ]

    cross_zero_counts_izquierdo = [
        ((izquierdo_normalized[col].shift(1) * izquierdo_normalized[col]) < 0).sum()
        for col in izquierdo_normalized.columns
    ]

    # Crear un DataFrame con los valores de los cruces por cero
    df_paired = pd.DataFrame({
        'Columnas_Derecho': derecho.columns,
        'Columnas_Izquierdo': izquierdo.columns,
        'Derecho': cross_zero_counts_derecho,
        'Izquierdo': cross_zero_counts_izquierdo
    })

    # Agregar una fila para las sumatorias totales utilizando pd.concat()
    sumatoria_derecho = sum(df_paired['Derecho'])
    sumatoria_izquierdo = sum(df_paired['Izquierdo'])
    df_sumatoria = pd.DataFrame({
        'Columnas_Derecho': ['Sumatoria Total'],
        'Columnas_Izquierdo': ['Sumatoria Total'],
        'Derecho': [sumatoria_derecho],
        'Izquierdo': [sumatoria_izquierdo]
    })
    df_paired = pd.concat([df_paired], ignore_index=True)

    # Crear la gráfica de pirámide
    fig, ax = plt.subplots(figsize=(19, 17))

    # Posiciones en el eje y (una posición por cada par de columnas más la fila de sumatorias)
    y_positions = range(len(df_paired))

    # Dibujar las barras horizontales para cada par de columnas y la sumatoria
    ax.barh(y_positions, df_paired['Derecho'], color='purple', label='Derecho', align='center')
    ax.barh(y_positions, -df_paired['Izquierdo'], color='green', label='Izquierdo', align='center')  # Negativo para enfrentar

    # Configuración del eje y con etiquetas a ambos lados
    ax.set_yticks(y_positions)
    ax.set_yticklabels([''] * len(df_paired))  # Ocultamos temporalmente las etiquetas centrales
    ax.invert_yaxis()  # Para que las barras más grandes queden en la parte superior

    # Etiquetas a la izquierda y derecha de las barras
    for i, (col_derecho, col_izquierdo) in enumerate(zip(df_paired['Columnas_Derecho'], df_paired['Columnas_Izquierdo'])):
        ax.text(-max(df_paired['Izquierdo']) * 1.1, i, col_izquierdo, ha='right', va='center', fontsize=10, color='white')  # Etiquetas de izquierdo
        ax.text(max(df_paired['Derecho']) * 1.1, i, col_derecho, ha='left', va='center', fontsize=10, color='white')  # Etiquetas de derecho

    # Configuración de etiquetas y leyenda
    ax.set_xlabel('Zero Crossings')
    ax.set_title('Comparación de Cruces por Cero: Derecho vs Izquierdo')
    ax.legend(loc='upper right')

    # Línea central para separar los lados
    ax.axvline(0, color='black', linewidth=0.8)

    # Ajustar diseño y mostrar la gráfica
    plt.tight_layout()
    return fig
col9,col10=st.columns(2)
with col9:
    col11,col12=st.columns(2)
    with col11:
        st.pyplot(pir(df1))
        st.pyplot(pir(df3))
    with col12:
        st.pyplot(pir(df2))
        st.pyplot(pir(df4))
with col10:
    st.sidebar.empty()