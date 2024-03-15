import pandas as pd
from utils import db_connect

engine = db_connect()


engine
if engine:
    print("Conexión exitosa")

data = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/regularized-linear-regression-project-tutorial/main/demographic_health_data.csv')
data.to_sql('tabla health', engine, if_exists='replace', index=False)