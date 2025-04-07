import os 
import pandas as pd 
import numpy as np
import logging 


log_dirs = "logs"
os.makedirs(log_dirs,exist_ok=True)
logger = logging.getLogger('data_preprocessing')
logger.setLevel("DEBUG")

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dirs,'data_preprocessing.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def preprocess_df(df):
    """This function helps clean the dataset like removing outliers, duplicate values etc"""
    try:
        logger.debug("starting the preprocessing")
        #dropping unnecessary columns
        df.drop(columns=['Unnamed: 0'],axis=1,inplace=True)
        logger.debug('Unnecessary column removed ')

        #removing duplicated 
        df.drop_duplicates(inplace=True)
        logger.debug('Duplicates dropped')

        # Handling invalid data points 
        df.drop(df[df['x']==0].index,inplace=True)
        df.drop(df[df['y']==0].index,inplace=True)
        df.drop(df[df['z']==0].index,inplace=True)
        logger.debug('Invalid data points removed')
        
        #outlier removal
        df = df[(df['depth']<75) & (df['depth']>50)]
        df = df[(df['table']<80) & (df['table']>45)]
        df = df[(df['x']<30)]
        df = df[(df['y']<30)]
        df = df[(df['z']<30) & (df['z']>2)]
        logger.debug("Outliers handled successfully")
        return df
    except KeyError as e:
        logger.error('Column not found: %s',e)
        raise
    except Exception as e:
        logger.error('Error while data preprocessing %s',e)

def main():
    """
    Main function to load raw data, preprocess it, and save the processed data.
    """
    try:
        data = pd.read_csv('./data/raw/diamonds.csv')
        logger.debug('Data loaded properly')
        preprocessed_df = preprocess_df(data)

        data_path = os.path.join('./data','interim')
        os.makedirs(data_path,exist_ok=True)

        preprocessed_df.to_csv(os.path.join(data_path,'preprocessed_data.csv'),index=False)
        logger.debug('Processed data saved to %s', data_path)
    except FileNotFoundError as e:
        logger.error('File not found: %s', e)
    except pd.errors.EmptyDataError as e:
        logger.error('No data: %s', e)
    except Exception as e:
        logger.error('Failed to complete the data transformation process: %s', e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()