import pandas as pd
from sqlalchemy import create_engine

df= pd.read_csv('data_logistics_total.csv')

engine = create_engine('mysql+pymysql://root:xxxx@localhost:3306/mysql', echo=False)
df.to_sql(name='data_logistics_total', con=engine, if_exists='replace', index=False)