import streamlit as st
import pandas as pd



# def clean_data_loader(path='C:/Users/Diriba/Desktop/10AC/Week2/Project/datawarehousing_pneuma_opentraffic_data/Data/20181024_d1_0830_0900.csv'):
#     # Read your data into a pandas DataFrame
#     try:
#         df = pd.read_csv(path,  delimiter=';')
#         return df
#     except BaseException:
#         return "file does not exist or path is not correct"  


#df = clean_data_loader()

#df = pd.read_csv('C:/Users/Diriba/Desktop/10AC/Week2/Project/datawarehousing_pneuma_opentraffic_data/Data/20181024_d1_0830_0900.csv', delimiter=';')
import pandas as pd

# Replace 'your_file_path.csv' with the actual path to your CSV file
file_path = 'C:/Users/Diriba/Desktop/10AC/Week2/Project/datawarehousing_pneuma_opentraffic_data/Data/20181024_d1_0830_0900.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, delimiter=';')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Display basic information about the DataFrame
print("\nDataFrame Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualize the distribution of vehicle types
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='type')
plt.title('Distribution of Vehicle Types')
plt.show()

# Geospatial analysis (assuming 'lat' and 'lon' columns)
import geopandas as gpd
from shapely.geometry import Point

# Create a GeoDataFrame
geometry = [Point(lon, lat) for lon, lat in zip(df['lon'], df['lat'])]
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

# Plot the geographical locations of vehicles
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, color='lightgrey')

geo_df.plot(ax=ax, markersize=10, color='red', alpha=0.5)
plt.title('Geographical Locations of Vehicles')
plt.show()
