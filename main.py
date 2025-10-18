import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
import numpy as np


#Load data set
data_set = pd.read_csv("C:/Users/yeai2_6rsknlh/OneDrive/Visual/D599 Task 3/Megastore Dataset.csv")

#While loop
print("Do you want to run endcoding? (Yes/No)")
while True:
    user_response = input("")
    if user_response == "Yes":

        #Create copy of data set for encoding 
        data_set_encoded = data_set.copy()

        #Order priority encoding
        priority_map = {"critical" : 3, "High" : 2, "Medium" : 1, "Low" : 0}
        data_set_encoded["OrderPriority_encoded"] =  data_set_encoded["OrderPriority"].map(priority_map)

        #Customer satisfaction encoding
        satisfaction_map = {"Very Dissatisfied": 0, "Dissatisfied": 1, "Neutral": 2, "Satisfied": 3,"Very Satisfied": 4}
        data_set_encoded["Satisfaction_encoded"] = data_set_encoded["CustomerOrderSatisfaction"].map(satisfaction_map)

        #Region encoding
        regions_map = {"Northeast": 0, "Midwest": 1, "South": 2, "West": 3}
        data_set_encoded["Region_encoded"] = data_set_encoded["Region"].map(regions_map)

        #Segment encoding
        segment_map = {"Corporate": 0, "Consumer": 1, "Home Office": 2}
        data_set_encoded["Segment_encoded"] = data_set_encoded["Segment"].map(segment_map)

        print("Encoding complete")

        #Export the encoded data set
        data_set_encoded.to_csv("encoded_dataset.csv", index=False)
        print("File saved as 'encoded_dataset.csv'")
        break

    elif user_response == "No":
        print("\nOkay moving on.")
        break



#Create transaction using OrderID & ProductName
transactions = data_set.groupby("OrderID")["ProductName"].apply(list).tolist()
print(f"Created {len(transactions)} transactions")

#Save transactions
pd.DataFrame(transactions).to_csv('transactions.csv', index=False)
print("Saved transactions to 'transactions.csv'")

#Association rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 

#print("Do you want to run market basket analysis? (Yes/No)")
#while True:

#    elif user_response == "No":
#        print("\nOkay moving on.")
#       break   
