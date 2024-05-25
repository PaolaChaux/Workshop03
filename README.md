<h1 align="center"> Workshop03 </h1>
<p align="left">
   <img src="https://img.shields.io/badge/STATUS-FINISHED-green">
   </p>

### Presented by Paola Andrea Chaux Campo, students of Autonoma de Occidente University

## Table of contents
* [Description](#Description)

* [Quick](#Quick)

* [Objective](#Objective)

* [Requeriments](#Requeriments)

* [RepositoryStructure](#RepositoryStructure)

* [Installation](#Installation)

* [Considerations](#Considerations)

* [Conclusión](#conclusión)

* [References](#References)

## Description
Welcome to the Machine learning Data Streaming Code Challenge. This project leverages Apache Kafka to predict happiness scores in different countries with a regression machine learning model, using a dataset of 5 CSV files containing information about each country. The entire process includes Exploratory Data Analysis (EDA) and Extract, Transform, Load (ETL) operations on the 5 CSV files such as transformations, feature selection, a 70-30 data split for training, streaming transformed data, performig predictions, and storing predictions in a database.

## Quick data overview
#### The CSV's files are data from 5 csv's, the combined dataset, spanning 2015 to 2019, contains information for 782 countries across 10 columns. The fields are: 

* Country
* Rank
* Happines Score
* gdp_per_capita
* Social_Support
* Freedom
* Life_expectancy
* Generosity
* Corruption
* Year


## Objective 



## Requeriments
Before running this project, you need to have the following prerequisites in place:

Python
MySQL Database
Datasets Used
2015.csv
2016.csv
2017.csv
2018.csv
2019.csv
All of these datasets contain information about the happiness in different countries, with multiple variables that contribute to the evaluation of the happinnes of a country such as GDP per capita, Life expectancy, among others. Offering a comprehensive overview of happiness metrics and contributing factors across different nations.

## Repository Structure

requirements.txt: This file contains the necessary dependencies for the project.

utils folder:
db_operations.py: This file contains all the methods used for the database such as connection, creating table, and loading data.

transformations.py: This file contains all the methods used for the transformation of the data.

producer.py: This file contains the kafka producer that streams the data after applying transformations.

consumer.py: This file contains the kafka consumer that receives the data, makes the prediction and loads into the database.

docker-compose.yml: This file contains the kafka configuration.

notebooks folder:
model_train.ipynb: This file contains the exploratory data analysis of the data and the model training.
rf_regressor.pkl: This file corresponds to the trained model.
metrics.py: This file contains the evaluation of the model's performance.

## Installation
## How to run this project
Follow these steps to run the project:

Clone the repository: git clone https://github.com/PaolaChaux/Workshop03---Kafka.git
Install project dependencies: pip install -r requirements.txt
Create database credentials file 'db_config.json' in a folder called config with the following content:

{
  "user": "your_username",
  "password": "your_password",
  "host": "your_host"
  "server": "your_server",
  "db": "your_database"
}

## Considerations
 This file is necessary, by not having it you won't be able to access the database unless you state the credentials directly (not recommended). If you choose to give it a different name or location, you must change the the access route in the code.

Launch the containers:

docker compose up
Now you are all set to start exploring the project.

## Conclusión
Data Exploration (EDA) and Extraction, Transformation and Loading (ETL) are fundamental steps in any data science project. In this workshop 03, I was able to appreciate how EDA helps us to better understand the data and select the most relevant features for our machine learning model.

Data pre-processing is crucial to ensure that the data is clean and suitable for modeling. In this workshop 03, I learned about techniques such as categorical variable coding and feature scaling, which are important for improving model performance.

The process of training a machine learning model and evaluating its performance was fundamental and a new experience for me as I had not understood or performed this way and it helped me to understand and have more knowledge. In this workshop 03, we used a 70-30 data split to train and test the model, and then evaluated its performance using metrics suitable for regression problems.

The use of streaming data allowed me to process data in real time and make decisions based on up-to-date information, something new that I had also never experienced before. In this workshop 03, we implemented a data stream in which the model predicts the happiness score in real time and stores the predictions in a database.

Finally, evaluation of the model is crucial to determine its effectiveness in predicting the happiness score. In this project, we computed performance metrics such as mean squared error (MSE) to evaluate the model's performance.

In summary, this work allowed me to apply the theoretical knowledge acquired in class and acquire many more of the errors or complications I had; this considering that it is solving a realistic or real-world problem, which helped me to better understand the entire process for these projects, from EDA to model evaluation.

