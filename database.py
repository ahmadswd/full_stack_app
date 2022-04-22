from config import app_key
import requests
import pandas as pd
from sqlalchemy import create_engine

url =f"https://samples.openweathermap.org/data/2.5/forecast?id={app_key}"

response = requests.get(url)

print(response.status_code)
# print(response.json()["list"][0])

list_date = []
list_temp =[]
list_temp_max=[]
list_temp_min=[]
for row in response.json()["list"]:
    list_date.append(row['dt'])
    list_temp.append(row['main']['temp'])
    list_temp_max.append(row['main']['temp_max'])
    list_temp_min.append(row['main']['temp_min'])
df_weather = pd.DataFrame({"Date":list_date,
"Temp":list_temp,
"Temp_Max":list_temp_max,
"Temp_Min":list_temp_min,})

# df_weather.to_csv("file.csv")
engine = create_engine('postgresql://postgres:postgres@localhost:5432/weather')

df_weather.to_sql('weather_forecast', engine, if_exists='replace',index=False) #drops old table and creates new empty table
