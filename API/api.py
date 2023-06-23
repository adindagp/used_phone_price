from fastapi import FastAPI, Query
import pickle 
import pandas as pd
import numpy as np
from pydantic import BaseModel
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder
import uvicorn


app = FastAPI(
    title="Used Phone Price",
    version='1.0',
    description='Decision Tree Regression model is used for prediction',
    debug=True  # Enable debug mode
)

pickle_file = open('/home/adinda_gita/used_phone_price/Model/DecisionTreeModel.pkl','rb')
model = pickle.load(pickle_file)

# Update with your API's URL

# print(model.predict(pd.DataFrame(columns=['Ukuran_Layar_(inchi)','Kamera_Utama_(mp)','Kapasitas_Baterai_(mah)','Kamera_Depan_(mp)','Kondisi','Tipe','Merek'],data=np.array([6.30,12,3500,10,"Well used","android","samsung"]).reshape(1,7))))

class Data(BaseModel):
    Storage : int
    Ukuran_Layar: float
    Kamera_Utama: int
    Kapasitas_Baterai: int
    Kamera_Depan: int
    Kondisi: str
    Tipe: str
    Merek: str

@app.get('/')
@app.get('/home')
def read_home():
    """
    Home endpoint which can be used to test the availability of the application.
    """
    return {'message': 'System is healthy'}

@app.get("/predict")
def predict(
    Storage: int = Query(...),
    Ukuran_Layar: float = Query(...),
    Kamera_Utama: int = Query(...),
    Kapasitas_Baterai: int = Query(...),
    Kamera_Depan: int = Query(...),
    Kondisi: str = Query(...),
    Tipe: str = Query(...),
    Merek: str = Query(...)
    ):
    input_data = {
        'Storage': Storage,
        'Ukuran_Layar_(inchi)': Ukuran_Layar,
        'Kamera_Utama_(mp)': Kamera_Utama,
        'Kapasitas_Baterai_(mah)': Kapasitas_Baterai,
        'Kamera_Depan_(mp)': Kamera_Depan,
        'Kondisi': Kondisi,
        'Tipe': Tipe,
        'Merek': Merek
    }
    input_data = pd.DataFrame(data=input_data, index=[0])
    result = model.predict(input_data)[0]
    
    return {"prediction": result}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000)


