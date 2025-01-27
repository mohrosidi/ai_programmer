
# AI Programmer Consultant

**AI Programmer Consultant** adalah aplikasi berbasis Streamlit yang dirancang untuk membantu pengembang perangkat lunak dalam menganalisis kode, melakukan debugging, memberikan rekomendasi optimasi, dan menghasilkan kode baru. Aplikasi ini memanfaatkan model AI dari OpenAI seperti GPT-4, GPT-4o-mini, dan lainnya.

## **Fitur Utama**

1. **Analisis Kode**  
   Aplikasi dapat membaca file kode (Python, SQL, JavaScript, dll.) yang diunggah pengguna dan memberikan analisis detail terkait fungsi dan logikanya.

2. **Debugging**  
   AI dapat membantu mendeteksi dan memperbaiki error dalam kode yang diunggah atau dikirim melalui chat.

3. **Optimasi Kode**  
   Memberikan saran untuk meningkatkan efisiensi kode agar lebih cepat, bersih, dan sesuai dengan praktik terbaik (*best practices*).

4. **Generasi Kode Baru**  
   Membantu pengguna menghasilkan kode berdasarkan kebutuhan spesifik.

5. **Manajemen Riwayat Chat**  
   - Riwayat percakapan akan dihapus otomatis jika file baru yang berbeda diunggah.
   - Jika file yang diunggah sama, riwayat percakapan tetap dipertahankan.

---

## **Cara Menjalankan Aplikasi**

### **Persyaratan**

1. Python 3.8 atau lebih baru.
2. OpenAI API Key (diperlukan untuk menggunakan model AI).

### **Langkah Instalasi**

1. **Clone Repository atau Salin Folder Proyek**  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Buat Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Aktifkan di Mac/Linux
   venv\Scripts\activate     # Aktifkan di Windows
   ```

3. **Instal Dependensi**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi**  
   ```bash
   streamlit run app.py
   ```

---

## **Cara Menggunakan Aplikasi**

1. **Masukkan OpenAI API Key**  
   - Di sidebar aplikasi, masukkan OpenAI API Key Anda. Pastikan API Key valid untuk mengakses model AI.

2. **Unggah File Kode**  
   - Klik tombol *Upload File* dan pilih file kode yang ingin dianalisis (format yang didukung: `.py`, `.txt`, `.sql`, `.js`).

3. **Berinteraksi dengan AI**  
   - Setelah file diunggah, Anda dapat mengetikkan pertanyaan atau instruksi di kolom input chat, seperti:
     - "Jelaskan apa yang dilakukan kode ini."
     - "Apakah ada error dalam kode ini? Jika ada, perbaiki."
     - "Tolong optimalkan kode agar berjalan lebih efisien."
     - "Buatkan fungsi baru berdasarkan spesifikasi berikut."

4. **Reset Riwayat Chat**  
   - Riwayat percakapan otomatis direset jika file baru (berbeda) diunggah. Jika file yang diunggah sama, riwayat percakapan tetap dipertahankan.

---

## **Contoh Penggunaan**

1. **Pertanyaan**:  
   "Jelaskan apa yang dilakukan kode ini."  
   **Hasil**: AI akan memberikan penjelasan terkait fungsi dan logika kode.

2. **Permintaan**:  
   "Tolong optimalkan kode berikut."  
   **Hasil**: AI akan memberikan saran dan versi kode yang lebih efisien.

3. **Debugging**:  
   "Apakah ada bug di dalam kode ini? Jika ada, perbaiki."  
   **Hasil**: AI akan mendeteksi dan memberikan solusi untuk memperbaiki bug.

---

## **Struktur Proyek**

```
project-folder/
│
├── app.py               # File utama aplikasi Streamlit
├── requirements.txt     # File daftar dependensi Python
└── README.md            # Dokumentasi aplikasi
```

---

## **Dependensi**

File `requirements.txt` berisi daftar library yang diperlukan untuk menjalankan aplikasi. Berikut beberapa di antaranya:

- `streamlit` - Untuk membangun antarmuka aplikasi.
- `langchain` - Untuk memanfaatkan model OpenAI secara efisien.
- `langchain_community` - Untuk menyimpan riwayat percakapan.
- `openai` - Library resmi OpenAI untuk mengakses model AI.

Instalasi semua dependensi dapat dilakukan dengan:
```bash
pip install -r requirements.txt
```

---

## **Catatan Penting**

- Aplikasi membutuhkan koneksi internet karena bergantung pada API OpenAI.
- Harap pastikan OpenAI API Key Anda aktif dan memiliki cukup kuota untuk menggunakan model GPT.

---

## **Lisensi**

Aplikasi ini dilisensikan di bawah [MIT License](https://opensource.org/licenses/MIT).

```
MIT License
Copyright (c) 2025
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```
