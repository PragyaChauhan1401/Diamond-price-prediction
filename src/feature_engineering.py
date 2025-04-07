import os
import logging
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


log_dir = 'logs'
os.makedirs(log_dir,exist_ok=True)

logger = logging.getLogger('feature_engineering')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir,'feature_engineering.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def encode_data(df):
    """This is to encode the categorical  and numerical features"""
    try:
        s = (df.dtypes =="object")
        object_cols = list(s[s].index)

        lb = LabelEncoder()
        for col in object_cols:
            df[col] = lb.fit_transform(df[col])

        logger.debug('Encoding done successfully')

        #standard scaling numerical columns 
        numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
        scaler  = StandardScaler()
        df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
        logger.debug('sucessfully scaled the numerical cols')
        return df
    except KeyError as e:
        logger.error('Column not found %s',e)
        raise
    except Exception as e:
        logger.error("Unexpected error occured %s",e)
        raise

def main():
    """
    Main function to load raw data, preprocess it, and save the processed data.
    """
    try:
        df = pd.read_csv('./data/interim/preprocessed_data.csv')
        logger.debug('Data loaded successfully')

        df_scaled = encode_data(df)
        data_path = os.path.join('./data','processed_data')
        os.makedirs(data_path)

        df_scaled.to_csv(os.path.join(data_path,"processed_data.csv"),index=False)
        logger.debug('Processed data saved to %s', data_path)

    except FileNotFoundError as e:
        logger.error('File not found: %s', e)
    except pd.errors.EmptyDataError as e:
        logger.error('No data: %s', e)
    except Exception as e:
        logger.error('Failed to complete the data transformation process: %s', e)
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
