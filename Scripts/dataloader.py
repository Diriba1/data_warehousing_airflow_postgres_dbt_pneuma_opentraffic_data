import streamlit as st
import pandas as pd



def clean_data_loader(path='C:/Users/Diriba/Desktop/10AC/Week2/Project/datawarehousing_pneuma_opentraffic_data/Data/20181024_d1_0830_0900.csv'):
    # Read your data into a pandas DataFrame
    try:
        df = pd.read_csv(path)
        return df
    except BaseException:
        return "file does not exist or path is not correct"  

df = clean_data_loader()
st.write(df)