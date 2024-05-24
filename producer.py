import pandas as pd
from confluent_kafka import Producer
import json
from time import sleep
from sklearn.model_selection import train_test_split
from tranformations import country_continent, drop_rank, drop_country, dummies

def process_happy_data(df):
    df['Continent'] = df['Country'].apply(country_continent)
    df = drop_rank(df)
    df = dummies(df, 'Continent')
    df = drop_country(df)
    
    predictoras = ["GDP per capita", "Health (Life Expectancy)", "Freedom", "Generosity", "Government Corruption",
                   "Continent_Africa", "Continent_Asia", "Continent_Europe", "Continent_North America", 
                   "Continent_Oceania", "Continent_South America"]
    columna_predecir = "Happiness Score"
    X = df[predictoras]
    y = df[columna_predecir]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)
    return X_train, X_test, y_train, y_test

def kafka_producer(df, kafka_bootstrap_servers):
    producer = Producer({
        'bootstrap.servers': ','.join(kafka_bootstrap_servers)
    })
    
    for i in range(len(df)):
        row_json = df.iloc[i].to_json()
        producer.produce("kafka-happy", value=row_json)
        print(f"new message sent: {row_json}")
        sleep(1)

    producer.flush()

    print("Fin del envio")

if __name__ == "__main__":
    
    df = pd.read_csv("happy.csv")

    X_train, X_test, y_train, y_test = process_happy_data(df)
    
    test_df = X_test.copy()
    test_df['Happiness Score'] = y_test
    
    kafka_bootstrap_servers = ['localhost:9092'] 
    kafka_producer(test_df, kafka_bootstrap_servers)



