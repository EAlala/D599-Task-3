import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
import numpy as np

#Load data set
data_set = pd.read_csv("C:/Users/yeai2_6rsknlh/OneDrive/Visual/D599 Task 3/Megastore Dataset.csv")

#Create copy of data set for encoding 
data_set_encoded = data_set.copy()

#Order priority encoding
priority_map = {"critical" : 3, "High" : 2, "Medium" : 1, "Low" : 0}
data_set_encoded["OrderPriority_encoded"] =  data_set_encoded["OrderPriority"].map(priority_map)
