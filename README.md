
# 📄 DocSnap: File Converter dengan Pemantauan Aktivitas Tersembunyi

DocSnap adalah proyek simulasi *ethical hacking* dan *secure coding* yang terdiri dari dua bagian utama:  
1. **Web converter (klien)** – Mengonversi file PDF ke Word secara instan  
2. **Admin panel** – Memantau aktivitas pengguna melalui data yang dikirim balik saat file dibuka

🎯 Proyek ini bertujuan untuk mendemonstrasikan bagaimana file yang tampak tidak berbahaya bisa menyisipkan skrip untuk mengumpulkan informasi dari sisi pengguna dan menampilkannya secara real-time di panel admin.

## 🧩 Fitur Utama

### 🔹 Sisi Klien: `web_converter/`
- Web app untuk konversi PDF → Word
- Menyisipkan script pelacak dalam dokumen Word hasil konversi
- Skrip akan aktif saat file dibuka di sisi korban dan mengirim data ke server

### 🔹 Sisi Admin: `admin/`
- Dibangun dengan Flask (Python)
- Menampilkan data seperti:
  - Informasi sistem korban
  - Riwayat browsing (Chrome, Firefox, Edge)
  - Username dan password yang tersimpan di Edge
  - Lokasi IP publik
- Dashboard interaktif: `dashboard.html`, `overview.html`, `settings.html`, dll.

### 🔹 File Eksekusi: `system_info.exe`
- Dibangun dari script Python `system_info.py`
- Mengambil info korban, lalu mengirimkannya ke database MySQL secara otomatis

## 🧪 Contoh Data yang Dikumpulkan
✅ Sistem Operasi  
✅ Hostname & Username  
✅ IP Lokal & Publik + Lokasi geografis  
✅ Riwayat browser (Chrome, Firefox, Edge)  
✅ Username & password tersimpan (Edge)  
✅ Aktivitas jaringan (jumlah paket masuk/keluar)

## 🏗️ Struktur Folder

```
PBL_RKS_2014/
├── admin/
│   ├── static/
│   ├── templates/
│   ├── app.py
│   └── config.py
├── malware/
├── web_converter/
├── system_info.exe
├── system_info.sql
├── list_admin.sql
```

## 🛠️ Instalasi & Menjalankan

### 💻 Jalankan Admin Server

```bash
cd admin/
pip install -r requirements.txt
python app.py
```

Contoh isi `requirements.txt`:

```
Flask
pymysql
psutil
pycryptodome
requests
pywin32
```

### 🖥️ Jalankan file `system_info.exe` di korban

- Bisa dikirim melalui dokumen Word (hasil konversi)
- Akan mengambil data dan mengirim ke database MySQL server

## 🔐 Catatan Etis

> ⚠️ **Proyek ini hanya untuk keperluan edukasi!**  
> Jangan digunakan untuk aktivitas ilegal atau merugikan pihak lain tanpa izin eksplisit.

## 📜 Lisensi

Proyek ini bersifat open-source untuk keperluan pembelajaran, eksperimen secure coding, dan simulasi CTF. Tidak diperkenankan digunakan di luar lingkungan lab atau edukasi.

## 🧠 Ide Pengembangan Lanjutan

- Penyempurnaan script malware agar support Linux/MacOS
- Auto-koneksi reverse shell melalui file dokumen
- Integrasi sistem alert real-time ke admin
- Penambahan fitur logging aktivitas secara grafis (graf pola browsing dll.)
