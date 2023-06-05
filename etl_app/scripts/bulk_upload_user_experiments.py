import pandas as pd
import os
import csv
import psycopg2
from sqlalchemy import create_engine
from django.apps import apps

def csv_to_df(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path, sep=',\t')
    return df 


def df_to_db_ingest(df):
    engine = create_engine('postgresql://postgres:postgres@0.0.0.0:5432/postgres')

    # Inject the DataFrame into a table in the database
    df.to_sql('etl_app_compound', engine, if_exists='replace', index=False)

    # Close the database connection
    engine.dispose()
    return
    

def main():
    
    
    path = "csv_data/user_experiments.csv" #TODO This path can be dynamic if needed but hardcoded for now to a folder

    dataframe_info = csv_to_df(path)
    print(dataframe_info)
    df_to_db_ingest(dataframe_info)

if __name__ == "__main__":
    main()