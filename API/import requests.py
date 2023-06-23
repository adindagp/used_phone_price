import requests

base_url = "http://127.0.0.1:8000"  # Update with your API's URL

endpoint = "/predict"

data = {
    "Ukuran_Layar(inchi)": 6.30,
    "Kamera_Utama_(mp)": 12,
    "Kapasitas_Baterai_(mah)": 3500,
    "Kamera_Depan_(mp)": 10,
    "Kondisi": "Like new",
    "Tipe": "android",
    "Merek": "samsung"
}

response = requests.post(base_url + endpoint, json=data)

if response.status_code == 200:
    result = response.json()
    print("Prediction:", result)
else:
    print("Request failed with status code:", response.status_code)