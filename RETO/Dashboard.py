import streamlit as st
import datetime
import numpy as np
from datetime import time
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
def filter(minn,maxx):
    from config import df1
    from config import df2
    from config import df3
    from config import df4
    df1= df1[(df1['Tiempo'] >= minn) & (df1['Tiempo'] <= maxx)]
    df2 = df2[(df2['Tiempo'] >= minn) & (df2['Tiempo'] <= maxx)]
    df3 = df3[(df3['Tiempo'] >= minn) & (df3['Tiempo'] <= maxx)]
    df4 = df4[(df4['Tiempo'] >= minn) & (df4['Tiempo'] <= maxx)]
    return df1,df2,df3,df4
st.set_page_config(page_title='Análisis de datos',layout="wide")
#st.title('Análisis de datos')
tab1,tab2=st.tabs(['Análisis de variables en el tiempo','Análisis comparativo'])
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
with tab1:
    import streamlit as st

    col1, col2 = st.columns(2)

    SECTION=st.sidebar.selectbox(label='Grafique en función del tiempo:',options=['Distancia','Velocidad','Aceleración','Presión','Velocidad de la presión','Aceleración de la presión'])
    MULTI_SECTION1=st.sidebar.multiselect(label='Radar variables dinámicas:',options=['Sesión 1','Sesión 2','Sesión 3','Sesión 4'])
    MULTI_SECTION2=st.sidebar.multiselect(label='Radar líneas de la cara:',options=['Sesión 1','Sesión 2','Sesión 3','Sesión 4'])
    import matplotlib.pyplot as plt
    # Asumiendo que df1, df2, df3 y df4 son DataFrames ya definidos
    sesiones = [df1, df2, df3, df4]
    list_sesiones,intervalos_main,emoc=[],[],[]
    sentiment_columns = ['01_C', '02_A', '03_D', '04_M']
    # Creo la figura con 4 subplots en 2 filas y 2 columnas
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
    # Itero sobre cada sesión y su subplot
    for s, ax in enumerate(axs.flatten()):
        # Sesión actual
        session_data = sesiones[s]
        # Grafico cada columna de sentimiento en el subplot correspondiente
        for i, col in enumerate(sentiment_columns):
            # Filtro los intervalos de tiempo donde el sentimiento está presente (valor = 1)
            intervalos = []
            start = None
            for j in range(len(session_data)):
                if session_data[col].iloc[j] == 1:
                    if start is None:
                        start = session_data['Tiempo'].iloc[j]
                else:
                    if start is not None:
                        end = session_data['Tiempo'].iloc[j - 1]
                        intervalos.append((start, end))
                        list_sesiones.append(s+1)
                        intervalos_main.append((start, end))
                        emoc.append(col)
                        start = None
            # Capturar el último intervalo si termina en el último valor de la columna
            if start is not None:
                intervalos.append((start, session_data['Tiempo'].iloc[-1]))
                list_sesiones.append(s+1)
                intervalos_main.append((start, session_data['Tiempo'].iloc[-1]))
                emoc.append(col)

            # Dibujar barras horizontales para los intervalos
            for (start, end) in intervalos:
                ax.hlines(y=i, xmin=start, xmax=end, color=plt.get_cmap("Set1")(i), linewidth=6)

        # Etiquetas y formato
        ax.set_yticks(range(len(sentiment_columns)))
        ax.set_yticklabels(sentiment_columns)
        ax.set_xlabel("Tiempo")
        ax.set_title(f"Presencia de sentimientos en intervalos de tiempo - Sesión {s + 1}")
        ax.grid(axis='x', linestyle='--', alpha=0.7)
    maximos,etiquetas=[],[]
    con=0
    for i,j in intervalos_main:
        maximos.append(round(j-i,2))
        etiquetas.append(list_sesiones[con])
        con+=1
    data_mini=pd.DataFrame()
    data_mini['sesion']=etiquetas
    data_mini['valor']=maximos
    data_mini['emocion']=emoc
    data_mini['emocion']= data_mini['emocion'].replace({'01_C':'Cansancio'})
    data_mini['emocion']= data_mini['emocion'].replace({'02_A':'Ansiedad'})
    data_mini['emocion']= data_mini['emocion'].replace({'03_D':'Dolor'})
    data_mini['emocion']= data_mini['emocion'].replace({'04_M':'Motivación'})
        
    plt.tight_layout()
    with col1: 
        st.pyplot(fig)
    with col2:
        if 'Distancia' in SECTION:
            var='Distancia'
            var2='Distancia'
        if 'Velocidad' in SECTION:
            var='Velocidad'
            var2='Veloc'
        if 'Aceleración' in SECTION:
            var='Aceleración'
            var2='Acele'
        if 'Presión' in SECTION:
            var='Presión'
            var2='Presn'
        if 'Velocidad de la presión' in SECTION:
            var='Velocidad de la presión'
            var2='VelPr'
        if 'Aceleración de la presión' in SECTION:
            var='Aceleración de la presión'
            var2='AcePr'
        fig2, axs2 = plt.subplots(nrows=1, ncols=1, figsize=(10, 6.23))
        # Crear el gráfico de áreas
        plt.fill_between(df1['Tiempo'], df1[var2].cumsum(), color='green', alpha=0.5, label='Sesión 1')
        plt.fill_between(df2['Tiempo'], df2[var2].cumsum(), color='lightblue', alpha=0.5, label='Sesión 2')
        plt.fill_between(df3['Tiempo'], df3[var2].cumsum(), color='blue', alpha=0.5, label='Sesión 3')
        plt.fill_between(df4['Tiempo'], df4[var2].cumsum(), color='purple', alpha=0.5, label='Sesión 4')

        # Etiquetas y título
        plt.xlabel('Tiempo de la sesión (min)')
        plt.ylabel(f'{var}')
        plt.title(f'{var} acumulada en el tiempo')
        plt.legend(loc='upper left')
        plt.tight_layout()
        st.pyplot(fig2)
        import matplotlib.pyplot as plt

        # Datos para cada sección
        s1c=data_mini[(data_mini['emocion']=='Cansancio') & (data_mini['sesion']==1)]
        s1a=data_mini[(data_mini['emocion']=='Ansiedad') & (data_mini['sesion']==1)]
        s1d=data_mini[(data_mini['emocion']=='Dolor') & (data_mini['sesion']==1)]
        s1m=data_mini[(data_mini['emocion']=='Motivación') & (data_mini['sesion']==1)]
        seccion1 = [np.where(np.isnan(s1c['valor'].max()),0,s1c['valor'].max()), np.where(np.isnan(s1a['valor'].max()),0,s1a['valor'].max()), np.where(np.isnan(s1d['valor'].max()),0,s1d['valor'].max()),np.where(np.isnan(s1m['valor'].max()),0,s1m['valor'].max())]
        
        s1c=data_mini[(data_mini['emocion']=='Cansancio') & (data_mini['sesion']==2)]
        s1a=data_mini[(data_mini['emocion']=='Ansiedad') & (data_mini['sesion']==2)]
        s1d=data_mini[(data_mini['emocion']=='Dolor') & (data_mini['sesion']==2)]
        s1m=data_mini[(data_mini['emocion']=='Motivación') & (data_mini['sesion']==2)]
        seccion2 = [np.where(np.isnan(s1c['valor'].max()),0,s1c['valor'].max()), np.where(np.isnan(s1a['valor'].max()),0,s1a['valor'].max()), np.where(np.isnan(s1d['valor'].max()),0,s1d['valor'].max()),np.where(np.isnan(s1m['valor'].max()),0,s1m['valor'].max())]

        s1c=data_mini[(data_mini['emocion']=='Cansancio') & (data_mini['sesion']==3)]
        s1a=data_mini[(data_mini['emocion']=='Ansiedad') & (data_mini['sesion']==3)]
        s1d=data_mini[(data_mini['emocion']=='Dolor') & (data_mini['sesion']==3)]
        s1m=data_mini[(data_mini['emocion']=='Motivación') & (data_mini['sesion']==3)]
        seccion3 = [np.where(np.isnan(s1c['valor'].max()),0,s1c['valor'].max()), np.where(np.isnan(s1a['valor'].max()),0,s1a['valor'].max()), np.where(np.isnan(s1d['valor'].max()),0,s1d['valor'].max()),np.where(np.isnan(s1m['valor'].max()),0,s1m['valor'].max())]

        s1c=data_mini[(data_mini['emocion']=='Cansancio') & (data_mini['sesion']==4)]
        s1a=data_mini[(data_mini['emocion']=='Ansiedad') & (data_mini['sesion']==4)]
        s1d=data_mini[(data_mini['emocion']=='Dolor') & (data_mini['sesion']==4)]
        s1m=data_mini[(data_mini['emocion']=='Motivación') & (data_mini['sesion']==4)]
        seccion4 = [np.where(np.isnan(s1c['valor'].max()),0,s1c['valor'].max()), np.where(np.isnan(s1a['valor'].max()),0,s1a['valor'].max()), np.where(np.isnan(s1d['valor'].max()),0,s1d['valor'].max()),np.where(np.isnan(s1m['valor'].max()),0,s1m['valor'].max())]
        print(s1c)

        # Etiquetas para el eje x
        labels = ['Cansancio', 'Ansiedad', 'Dolor', 'Motivación']

        # Crear subplots
        fig3, axs3 = plt.subplots(2, 2, figsize=(10, 8))

        # Gráfico para la sección 1
        axs3[0, 0].bar(labels, seccion1, color='green')
        axs3[0, 0].set_title('Tiempo máximo en una emoción Sesión 1')
        axs3[0, 0].set_ylabel('Tiempo')

        # Gráfico para la sección 2
        axs3[0, 1].bar(labels, seccion2, color='lightblue')
        axs3[0, 1].set_title('Tiempo máximo en una emoción Sesión 2')
        axs3[0, 1].set_ylabel('Tiempo')

        # Gráfico para la sección 3
        axs3[1, 0].bar(labels, seccion3, color='blue')
        axs3[1, 0].set_title('Tiempo máximo en una emoción Sesión 3')
        axs3[1, 0].set_ylabel('Tiempo')

        # Gráfico para la sección 4
        axs3[1, 1].bar(labels, seccion4, color='purple')
        axs3[1, 1].set_title('Tiempo máximo en una emoción Sesión 4')
        axs3[1, 1].set_ylabel('Tiempo')

        # Ajustar el diseño
        plt.tight_layout()
        st.pyplot(fig3)
with tab2:
    st.sidebar.empty()