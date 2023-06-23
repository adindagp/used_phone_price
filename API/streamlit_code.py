import streamlit as st
import pandas as pd
import requests

df = pd.read_csv("/home/adinda_gita/used_phone_price/Data/phone_final_filtered.csv")
df.drop("Jenis Handphone",axis=1)

def main():
    st.title("Used Phone Price Prediction")
    Storage = st.number_input("Storage (GB)")
    Ukuran_Layar = st.number_input("Ukuran Layar (inchi)")
    Kamera_Utama = st.number_input("Kamera Utama (MP)",value=0, step=1)
    Kapasitas_Baterai = st.number_input("Kapasitas Baterai (mAh)",value=0, step=1)
    Kamera_Depan = st.number_input("Kamera Depan (MP)",value=0, step=1)
    Kondisi = st.selectbox("Kondisi", df.Kondisi.unique())
    Tipe = st.selectbox("Tipe", df.Tipe.unique())
    Merek = st.selectbox("Merek", df.Merek.unique())

    if st.button("Predict"):
        params = {
            "Storage": int(Storage),
            "Ukuran_Layar": Ukuran_Layar,
            "Kamera_Utama": int(Kamera_Utama),
            "Kapasitas_Baterai": int(Kapasitas_Baterai),
            "Kamera_Depan" : int(Kamera_Depan),
            "Kondisi": Kondisi,
            "Tipe": Tipe,
            "Merek": Merek
            }
        # Make a GET request to the API endpoint
        api_url = "http://localhost:8000/predict"
        response = requests.get(api_url, params=params)
        # Process the response as needed
        if response.status_code == 200:
            result = response.json()
            st.write("Prediction:", result["prediction"])
        else:
            st.error("An error occurred while processing the request.")
            
if __name__ == "__main__":
    main()