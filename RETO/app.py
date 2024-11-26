import streamlit as st

create_page = st.Page("PAGE1.py", title="Análisis General", icon=":material/add_circle:")
page = st.Page("PAGE2.py", title="Análisis de la cara", icon=":material/add_circle:")

pg = st.navigation([create_page,page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:",layout="wide")

pg.run()