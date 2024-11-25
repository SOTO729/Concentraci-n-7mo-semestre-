import streamlit as st
#@st.cache_data
import os
def load_df(arg):
    import pandas as pd
    import datetime
    import math
    data=pd.read_csv(arg)
    data.dropna(inplace=True)
    def distance(x, y, z):
        return math.sqrt(x**2 + y**2 + z**2)
    data['Distancia'] = data.apply(lambda row: distance(row['Des_x'], row['Des_y'], row['Des_z']), axis=1)
    data['01_C']= data['01_C'].replace({-1:0})
    data['02_A']= data['02_A'].replace({-1:0})
    data['03_D']= data['03_D'].replace({-1:0})
    data['04_M']= data['04_M'].replace({-1:0})
    return data

folder_paths = ['./Paciente 1','./Paciente 2','./Paciente 3']
pacientes=[]
def read_patient(folder_path):
    paciente=[]
    files = os.listdir(folder_path)
    for file_name in files[:4]:  # Limitar a los primeros 4 archivos
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
            paciente.append(content)
    return paciente

for i in folder_paths:
    pacientes.append(read_patient(i))
df1p1=load_df(pacientes[0][0])
df2p1=load_df(pacientes[0][1])
df3p1=load_df(pacientes[0][2])
df4p1=load_df(pacientes[0][3])

df1p2=load_df(pacientes[1][0])
df2p2=load_df(pacientes[1][1])
df3p2=load_df(pacientes[1][2])
df4p2=load_df(pacientes[1][3])

df1p3=load_df(pacientes[2][0])
df2p3=load_df(pacientes[2][1])
df3p3=load_df(pacientes[2][2])
df4p3=load_df(pacientes[2][3])
print(len(pacientes))