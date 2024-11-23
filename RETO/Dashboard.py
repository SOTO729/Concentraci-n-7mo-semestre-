import streamlit as st
import datetime
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
st.sidebar.write("Tiempo seleccionado:", str(round(SLIDER[1]-SLIDER[0],2))+' '+'min')
df1,df2,df3,df4=filter(float(SLIDER[0]),float(SLIDER[1]))
with tab1:
    SECTION=st.sidebar.selectbox(label='Grafique en función del tiempo:',options=['Distancia','Velocidad','Aceleración','Presión','Velocidad de la presión','Aceleración de la presión'])
    MULTI_SECTION1=st.sidebar.multiselect(label='Radar variables dinámicas:',options=['Sesión 1','Sesión 2','Sesión 3','Sesión 4'])
    MULTI_SECTION2=st.sidebar.multiselect(label='Radar líneas de la cara:',options=['Sesión 1','Sesión 2','Sesión 3','Sesión 4'])
    import matplotlib.pyplot as plt
    sesiones = [df1, df2, df3, df4]
    sentiment_columns = ['01_C', '02_A', '03_D', '04_M']
    #creo la figura con 4 subplots en una columna
    fig, axs = plt.subplots(nrows=4, ncols=1,figsize=(10, 18))
    #itero sobre cada sesión y su subplot
    for s, ax in enumerate(axs):
        #sesión actual
        session_data = sesiones[s]
        #grafico cada columna de sentimiento en el subplot correspondiente
        for i, col in enumerate(sentiment_columns):
            #filtro los intervalos de tiempo donde el sentimiento está presente (valor = 1)
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
                        start = None
            # Capturar el último intervalo si termina en el último valor de la columna
            if start is not None:
                intervalos.append((start, session_data['Tiempo'].iloc[-1]))

            # Dibujar barras horizontales para los intervalos
            for (start, end) in intervalos:
                ax.hlines(y=i, xmin=start, xmax=end, color=plt.get_cmap("Set1")(i), linewidth=6)

        # Etiquetas y formato
        ax.set_yticks(range(len(sentiment_columns)))
        ax.set_yticklabels(sentiment_columns)
        ax.set_xlabel("Tiempo")
        ax.set_title(f"Presencia de sentimientos en intervalos de tiempo - Sesión {s + 1}")
        ax.grid(axis='x', linestyle='--', alpha=0.7)
    st.pyplot(fig)
with tab2:
    st.sidebar.empty()