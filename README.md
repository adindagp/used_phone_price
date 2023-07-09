# used_phone_price
machine learning project for predicting used phone price

# Persyaratan dalam model proyek ini:
Storage: Kapasitas penyimpanan handphone
Ukuran layar: Ukuran layar handphone secara diagonal
Kamera utama: megapixel dari kamera utama
Kapasitas baterai: kapasitas baterai dalam mAh
Kondisi: Kondisi dari handphone (Like new, new, used, well used, lightly used, heavily used)
Tipe : Android/iphone
Merek : merek dari handphone (Samsung, iPhone, Oppo, Xiaomi) 

# Respon prediksi dari API:
Respon-nya berupa prediksi harga handphone bekas

# Alur Kerja:
API dan streamlit dijalankan menggunakan docker compose
command: docker-compose up

# Deskripsi Proyek:
1.	Pembelian handphone bekas merupakan salah satu alternatif yang lebih murah dan secara bersamaan membantu mengurangi limbah elektronik berupa handphone
2. Regulasi harga oleh pembeli dan penjual dapat meningkatkan kepercayaan yang diharapkan juga meningkatkan volume jual beli pada platform

# Ekspektasi Output Project
Prediksi harga handphone bekas yang cukup fair

# Dataset 
Data hasil scrap dari website carousell

# Kesimpulan dan Referensi
Kesimpulan yang didapatkan adalah variabel yang berpengaruh pada harga adalah tipe handphone, merek handphone, storage dan kondisi
Perbaikan yang bisa dilakukan ke depan-nya:
-	Perbanyakan variabel. Seperti RAM atau lama handphone dipakai
-	Sampel data dikumpulkan dari beberapa website
-	Kuesioner kepada para penjual untuk melihat pertimbangan ketika menjual handphone bekas

# Reference link
https://link.springer.com/article/10.1007/s11356-021-17061-w
https://core.ac.uk/download/pdf/235044836.pdf
https://medium.com/@furkankizilay/end-to-end-machine-learning-project-using-fastapi-streamlit-and-docker-6fda32d25c5d
