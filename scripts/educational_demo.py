from mac_implementation import MACImplementation
from usac_implementation import USACImplementation

def educational_demonstration():
    """
    Demonstrasi edukatif untuk memahami MAC dan USAC
    """
    print("=" * 80)
    print("DEMONSTRASI EDUKATIF: KRIPTOGRAFI HASH - MAC & USAC")
    print("=" * 80)
    
    print("\n📚 PENJELASAN KONSEP:")
    print("-" * 40)
    
    print("\n1. MESSAGE AUTHENTICATION CODE (MAC):")
    print("   • Deskripsi: Algoritma kriptografi yang menggunakan kunci rahasia")
    print("     untuk menghasilkan tag autentikasi dari sebuah pesan.")
    print("   • Penemu: Dikembangkan pada tahun 1970-an oleh Whitfield Diffie")
    print("     dan Martin Hellman sebagai bagian dari kriptografi kunci publik.")
    print("   • Kategori: Symmetric key cryptography, Cryptographic hash functions")
    print("   • Spesifikasi/Objek Sasaran:")
    print("     - Verifikasi integritas pesan")
    print("     - Autentikasi sumber pesan")
    print("     - Deteksi manipulasi data")
    print("     - Protokol komunikasi aman (TLS, IPSec, SSH)")
    print("   • Parameter Pengujian:")
    print("     - Keamanan kriptografi: Resistensi terhadap serangan")
    print("     - Kecepatan komputasi: Efisiensi pemrosesan")
    print("     - Ukuran output: Panjang MAC yang dihasilkan")
    print("   • Cara Kerja:")
    print("     1. Input: Pesan (M) + Kunci rahasia (K)")
    print("     2. Proses: MAC = H(K || M) atau MAC = H(K ⊕ opad || H(K ⊕ ipad || M))")
    print("     3. Output: Tag autentikasi dengan panjang tetap")
    print("     4. Verifikasi: Penerima menghitung MAC dengan kunci yang sama dan membandingkan")
    
    print("\n2. UNCONDITIONAL SECURE AUTHENTICATION CODE (USAC):")
    print("   • Deskripsi: Sistem autentikasi yang memberikan keamanan tanpa syarat")
    print("     (unconditional security) berdasarkan teori informasi Shannon.")
    print("   • Penemu: Dikembangkan berdasarkan penelitian Gustavus Simmons")
    print("     pada tahun 1980-an tentang authentication codes.")
    print("   • Kategori: Information-theoretic cryptography, Unconditionally secure systems")
    print("   • Spesifikasi/Objek Sasaran:")
    print("     - Keamanan teoretis maksimal")
    print("     - Aplikasi militer dan pemerintahan")
    print("     - Komunikasi jangka panjang yang critical")
    print("   • Parameter Pengujian:")
    print("     - Keamanan informasi-teoritis")
    print("     - Manajemen kunci")
    print("     - Overhead komunikasi")
    print("   • Cara Kerja:")
    print("     1. Input: Pesan (M) + One-time key (K) dengan |K| ≥ |M|")
    print("     2. Proses: Encoded = M ⊕ K, Auth_tag = f(M, K_auth)")
    print("     3. Output: Encoded message + Authentication tag")
    print("     4. Verifikasi: Decode dan verifikasi tag autentikasi")
    
    
    print("\n" + "=" * 80)
    print("DEMONSTRASI STEP-BY-STEP")
    print("=" * 80)
    
    
    alice_message = "Meet me at the library at 3 PM"
    print(f"\n📨 Skenario: Alice ingin mengirim pesan ke Bob")
    print(f"Pesan: '{alice_message}'")
    
    
    print("\n" + "🔐 PROSES MAC (HMAC-SHA256):")
    print("-" * 50)
    
    mac_impl = MACImplementation('sha256')
    shared_key = mac_impl.generate_key()
    
    print(f"1. Alice dan Bob berbagi kunci: {shared_key.hex()[:32]}...")
    print(f"2. Alice menghitung MAC dari pesan...")
    
    mac_tag = mac_impl.compute_mac(alice_message, shared_key)
    print(f"3. MAC Tag: {mac_tag}")
    
    print(f"4. Alice mengirim: (pesan, MAC) ke Bob")
    print(f"5. Bob menerima dan memverifikasi...")
    
    is_valid = mac_impl.verify_mac(alice_message, shared_key, mac_tag)
    print(f"6. Hasil verifikasi: {'✅ VALID' if is_valid else '❌ INVALID'}")
    
    
    print(f"\n🚨 Simulasi Serangan:")
    tampered_message = "Meet me at the bank at 3 PM"  
    is_tampered_valid = mac_impl.verify_mac(tampered_message, shared_key, mac_tag)
    print(f"   Pesan diubah: '{tampered_message}'")
    print(f"   Verifikasi: {'✅ VALID' if is_tampered_valid else '❌ INVALID (Serangan terdeteksi!)'}")
    
    
    print("\n" + "🛡️ PROSES USAC (One-Time Pad + Auth):")
    print("-" * 50)
    
    usac_impl = USACImplementation()
    otp_key = usac_impl.generate_one_time_key(len(alice_message) + 32)
    
    print(f"1. Alice generate one-time key: {otp_key.hex()[:32]}...")
    print(f"2. Key length: {len(otp_key)} bytes (≥ message length)")
    print(f"3. Alice encode pesan dengan XOR...")
    
    encoded_msg, auth_tag = usac_impl.encode_message(alice_message, otp_key)
    print(f"4. Encoded message: {encoded_msg.hex()}")
    print(f"5. Auth tag: {auth_tag}")
    
    print(f"6. Alice mengirim: (encoded_msg, auth_tag) ke Bob")
    print(f"7. Bob decode dengan key yang sama...")
    
    decoded_msg = usac_impl.decode_message(encoded_msg, otp_key)
    print(f"8. Decoded message: '{decoded_msg}'")
    
    is_authentic = usac_impl.verify_authenticity(encoded_msg, otp_key, auth_tag, len(alice_message))
    print(f"9. Autentikasi: {'✅ VALID' if is_authentic else '❌ INVALID'}")
    
    
    print("\n" + "🔄 PERBEDAAN SEBELUM DAN SETELAH PENERAPAN:")
    print("-" * 50)
    
    print("Sebelum Penerapan MAC/USAC:")
    print("  • Pesan dapat diubah tanpa deteksi")
    print("  • Tidak ada jaminan autentisitas pengirim")
    print("  • Rentan terhadap man-in-the-middle attacks")
    print("  • Tidak ada mekanisme verifikasi integritas")
    
    print("\nSetelah Penerapan MAC/USAC:")
    print("  • Perubahan pesan dapat terdeteksi")
    print("  • Autentisitas pengirim terjamin")
    print("  • Perlindungan terhadap replay attacks")
    print("  • Integritas data terjaga selama transmisi")
    
    print("\n" + "=" * 80)
    print("KESIMPULAN")
    print("=" * 80)
    
    print("1. MESSAGE AUTHENTICATION CODE (MAC):")
    print("   • Keamanan: Computational security")
    print("   • Kunci: Tetap, dapat digunakan berulang")
    print("   • Efisiensi: Sangat efisien, cocok untuk aplikasi praktis")
    print("   • Penggunaan: TLS, IPSec, SSH, aplikasi web")
    
    print("\n2. UNCONDITIONAL SECURE AUTHENTICATION CODE (USAC):")
    print("   • Keamanan: Information-theoretic security")
    print("   • Kunci: One-time pad, panjang ≥ pesan")
    print("   • Efisiensi: Kurang efisien, memerlukan manajemen kunci kompleks")
    print("   • Penggunaan: Aplikasi militer, komunikasi high-security")


educational_demonstration()
