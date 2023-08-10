**Langkah 1: Persiapan**

1. Pastikan Anda memiliki instalasi Python yang berfungsi di komputer Anda. Jika belum, Anda dapat mengunduh dan menginstal Python dari situs resmi python.org.

2. Pastikan semua instance klien dan server berada di jaringan WiFi yang sama.

**Langkah 2: Persiapan File dan Direktori**

1. Buat direktori baru dengan nama "received_files" di direktori yang sama dengan server.py. Ini adalah tempat di mana file yang diterima akan disimpan.

2. (Opsional) Jika Anda ingin memiliki kemampuan "mengunduh" file, buat direktori baru dengan nama "files_to_send" di direktori yang sama dengan server.py. Ini adalah tempat di mana file yang akan dikirim dari server ke klien akan disimpan.

**Langkah 3: Menjalankan Server**

1. Buka terminal atau command prompt.

2. Navigasi ke direktori di mana server.py berada menggunakan perintah `cd /path/to/directory`.

3. Jalankan server dengan perintah berikut:
   ```
   python server.py
   ```

**Langkah 4: Menjalankan Klien**

1. Buka terminal atau command prompt (buka beberapa instance sesuai jumlah klien yang ingin Anda jalankan).

2. Navigasi ke direktori di mana client.py berada menggunakan perintah `cd /path/to/directory`.

3. Jalankan klien dengan perintah berikut:
   ```
   python client.py
   ```

**Langkah 5: Berinteraksi dengan Aplikasi Chat**

1. Setiap jendela klien akan muncul. Anda bisa mengirim pesan teks ke semua klien, atau mengirim/menerima file.

2. Untuk mengirim pesan, tuliskan pesan di kotak input teks dan tekan tombol "Send Unicast" untuk mengirim pesan pribadi ke klien tertentu, atau "Send Multicast" untuk mengirim pesan ke semua klien, atau "Send Broadcast" untuk mengirim pesan broadcast ke semua klien.

3. Untuk mengirim file, tekan tombol "Send File Unicast", "Send File Multicast", atau "Send File Broadcast". Anda akan diminta untuk memilih file yang akan diunggah.

4. Jika Anda ingin mengunduh file, tekan tombol "Download File". Anda akan diminta untuk memasukkan nama file yang ingin Anda unduh.

5. Akan ada notifikasi untuk menginformasikan Anda ketika file berhasil diterima.

**Catatan Penting**:
- Pastikan untuk menjalankan server terlebih dahulu sebelum menjalankan klien.
- Pastikan alamat IP dan port yang digunakan di klien sesuai dengan yang digunakan di server.
- Pastikan izin akses yang sesuai untuk direktori penyimpanan file yang telah disebutkan sebelumnya.

Dengan mengikuti langkah-langkah di atas, Anda akan dapat menjalankan aplikasi chat dengan fitur mengirim dan menerima file serta berinteraksi dengan semua fitur yang telah dibuat. Pastikan untuk menjalankan beberapa instance klien untuk mengamati komunikasi antara klien-klien.