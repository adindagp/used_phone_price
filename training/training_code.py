import pickle
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

data = pd.read_csv("phone_final_filtered_raw.csv")
ohe = OneHotEncoder()
ohe_ = ["Kondisi", "Tipe", "Merek"]
def extractInputOutput(data,output_column_name,column_to_drop,ohe_column):
    ohe.fit(data[ohe_column])
    data = data.drop(columns=column_to_drop, axis=1)
    output_data = data[output_column_name]
    input_data = data.drop(output_column_name,axis=1)
    return input_data, output_data

# variabel dependen
output_column_name = ["Harga"]

X, y = extractInputOutput(data = data,output_column_name = output_column_name,column_to_drop = "Jenis Handphone",ohe_column=ohe_)
print(X.head(5))

tree = DecisionTreeRegressor(max_depth = 2,random_state = 123)

column_trans=make_column_transformer((OneHotEncoder(categories=ohe.categories_),["Kondisi","Tipe","Merek"]),
                                remainder='passthrough')

#pipe to encode incoming data and make prediction
pipe=make_pipeline(column_trans,tree)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Training the pipe
pipe.fit(X_train,y_train)
#Testing the pipe
y_pred=pipe.predict(X_test)

#Testing the pipe
testing = pipe.predict(pd.DataFrame(columns=X_test.columns,data=np.array([128,6.30,12,3500,10,"Well used","android","samsung"]).reshape(1,8)))
print(testing)

# Pickle Decision Tree Model
# with open('DecisionTreeModel.pkl', 'wb') as file:
#     pickle.dump(pipe, file)