import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
import numpy as np

#Load data set
data_set = pd.read_csv("C:/Users/yeai2_6rsknlh/OneDrive/Visual/D599 Task 3/Megastore Dataset.csv")

#Create copy of data set
data_set_encoded = data_set.copy()


