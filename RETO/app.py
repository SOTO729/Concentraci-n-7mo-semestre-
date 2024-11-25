import streamlit as st

create_page = st.Page("Dashboard.py", title="Análisis General", icon=":material/add_circle:")
page = st.Page("config.py", title="Análisis de la cara", icon=":material/add_circle:")

pg = st.navigation([create_page,page])
#st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()