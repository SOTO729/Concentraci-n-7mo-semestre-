#@st.cache_data
def load_df(arg):
    import pandas as pd
    import datetime
    data=pd.read_csv(arg)
    data.dropna(inplace=True)
    data['Tiempo']=data.index*3
    data.dropna(inplace=True)
    data['Tiempo']=data['Tiempo'].apply(lambda x: datetime.timedelta(seconds=x).total_seconds() / 60)
    return data
print(load_df('03may.csv'))