# Kriptografi: MAC & USAC Demo

Aplikasi demonstrasi interaktif untuk memahami konsep Message Authentication Code (MAC) dan Unconditional Secure Authentication Code (USAC) dalam kriptografi.

## 🚀 Fitur

### 1. Message Authentication Code (MAC)
- Generate MAC untuk memastikan integritas dan autentisitas pesan
- Verifikasi MAC untuk memvalidasi pesan
- Input field dengan toggle visibility untuk kunci rahasia
- Visual feedback untuk status verifikasi (valid/invalid)

### 2. Unconditional Secure Authentication Code (USAC)
- Implementasi USAC dengan keamanan tanpa syarat
- Generate dan verifikasi USAC
- Validasi panjang kunci sesuai dengan panjang pesan
- Feedback visual untuk status autentikasi

### 3. Perbandingan MAC vs USAC
- Analisis perbandingan keamanan
- Perbandingan performa
- Aplikasi praktis
- Demonstrasi ketahanan terhadap serangan

## 🛠️ Teknologi yang Digunakan

- Next.js 14
- React
- TypeScript
- Tailwind CSS
- Shadcn/ui Components
- Lucide Icons

## 📦 Instalasi

1. Clone repository:
```bash
git clone [repository-url]
cd crypto-mac
```

2. Install dependencies:
```bash
npm install
# atau
yarn install
# atau
pnpm install
```

3. Jalankan development server:
```bash
npm run dev
# atau
yarn dev
# atau
pnpm dev
```

4. Buka [http://localhost:3000](http://localhost:3000) di browser Anda

## 🎯 Cara Penggunaan

### MAC Demo
1. Masukkan pesan yang ingin di-MAC
2. Masukkan kunci rahasia (dapat di-toggle visibility)
3. Klik "Generate MAC" untuk menghasilkan MAC
4. Untuk verifikasi:
   - Masukkan MAC yang ingin diverifikasi
   - Klik "Verifikasi MAC"
   - Status verifikasi akan ditampilkan

### USAC Demo
1. Masukkan pesan yang ingin di-USAC
2. Masukkan kunci (harus ≥ panjang pesan)
3. Klik "Generate USAC"
4. Hasil USAC akan ditampilkan

## 🔒 Keamanan

- MAC menggunakan HMAC-SHA256 untuk keamanan komputasional
- USAC menggunakan one-time pad untuk keamanan tanpa syarat
- Kunci rahasia tidak disimpan di server
- Semua komputasi dilakukan di sisi client

## 📚 Penjelasan Konsep

### Message Authentication Code (MAC)
- Algoritma kriptografi yang menggunakan kunci rahasia
- Menghasilkan tag autentikasi dari pesan
- Memastikan integritas dan autentisitas pesan
- Dikembangkan pada tahun 1970-an oleh Whitfield Diffie dan Martin Hellman

### Unconditional Secure Authentication Code (USAC)
- Sistem autentikasi dengan keamanan tanpa syarat
- Berdasarkan teori informasi Shannon
- Memerlukan kunci dengan panjang ≥ pesan
- Dikembangkan berdasarkan penelitian Gustavus Simmons

## 🤝 Kontribusi

Kontribusi selalu diterima! Silakan buat pull request atau buka issue untuk diskusi.

## 📝 Lisensi

MIT License - Bayani Adam Sasaki 