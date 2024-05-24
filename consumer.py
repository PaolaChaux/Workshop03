import pandas as pd
from json import loads
import joblib
import psycopg2 as psy
import json
from confluent_kafka import Consumer, KafkaException, KafkaError

modelo = joblib.load('RandomForestRegressor.pkl')


def database():
    with open('P:/ETL/workshop03/Workshop03---Kafka/config_db.json') as config_json:
        config = json.load(config_json)
    
    conn = psy.connect(dbname='postgres', user=config['user'], password=config['password'], host=config['host'], port= 5432)
    conn.autocommit = True
    cur = conn.cursor()
    
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (config['database'],))
    exists = cur.fetchone()
    if not exists:
        cur.execute(f"CREATE DATABASE {config['database']}")
    
    cur.close()
    conn.close()


    conn = psy.connect(dbname='happy', user=config['user'], password=config['password'], host=config['host'], port=config['port'])
    cur = conn.cursor()

    create_table_query = """CREATE TABLE IF NOT EXISTS HappyData (
        ID SERIAL PRIMARY KEY,
        "GDP per capita" FLOAT,
        "Health (Life Expectancy)" FLOAT,
        "Freedom" FLOAT,
        "Generosity" FLOAT,
        "Government Corruption" FLOAT,
        "Continent_Africa" BOOLEAN,
        "Continent_South America" BOOLEAN,
        "Continent_North America" BOOLEAN,
        "Continent_Asia" BOOLEAN,
        "Continent_Europe" BOOLEAN,
        "Continent_Oceania" BOOLEAN,
        "Happiness Score" FLOAT,
        "Predicted_Happy" FLOAT
    )"""
    

    print("Tabla creada con éxito.")
    cur.execute(create_table_query)
    conn.commit()

    cur.close()
    
    return conn


query = """
            INSERT INTO HappyData ("GDP per capita", "Health (Life Expectancy)", "Freedom", "Generosity", 
                    "Government Corruption", "Continent_Africa", "Continent_Asia", "Continent_Europe",
                    "Continent_North America", "Continent_Oceania", "Continent_South America", "Happiness Score", 
                    "Predicted_Happy") 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

def kafka_consumer_1():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'my-group-1',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': True
    })

    consumer.subscribe(['kafka-happy'])
    conn = database()
    
    try:
        while True:
            msg = consumer.poll(timeout=5000)
            if not msg:
                print("No hay más mensajes, saliendo del bucle")
                break

            message_value = msg.value().decode('utf-8')
            json_msg = json.loads(message_value)
            df = pd.DataFrame([json_msg])
            features = ["GDP per capita", "Health (Life Expectancy)", "Freedom", "Generosity", 
                    "Government Corruption", "Continent_Africa", "Continent_Asia", "Continent_Europe",
                    "Continent_North America", "Continent_Oceania", "Continent_South America"]

            prediction = modelo.predict(df[features])
            with conn.cursor() as cur:
                insert_values = (
                    json_msg['GDP per capita'], 
                    json_msg['Health (Life Expectancy)'], 
                    json_msg['Freedom'], 
                    json_msg['Generosity'], 
                    json_msg['Government Corruption'], 
                    json_msg.get('Continent_Africa', False), 
                    json_msg.get('Continent_South America', False), 
                    json_msg.get('Continent_North America', False), 
                    json_msg.get('Continent_Asia', False), 
                    json_msg.get('Continent_Europe', False), 
                    json_msg.get('Continent_Oceania', False), 
                    json_msg['Happiness Score'], 
                    prediction[0]
                )
          
                cur.execute(query, insert_values)
                conn.commit()

            print(f"Datos insertados en la base de datos correctamente: {insert_values}")
    except Exception as e:
        print(f"Error in consumer loop: {e}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        conn.close()

if __name__ == "__main__":
    kafka_consumer_1()


