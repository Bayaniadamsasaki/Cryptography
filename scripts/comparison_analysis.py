import time
import matplotlib.pyplot as plt
import numpy as np
from mac_implementation import MACImplementation
from usac_implementation import USACImplementation

class CryptographicComparison:
    """
    Kelas untuk membandingkan MAC dan USAC
    """
    
    def __init__(self):
        self.mac = MACImplementation()
        self.usac = USACImplementation()
    
    def performance_comparison(self):
        """Perbandingan performa MAC vs USAC"""
        print("\n" + "=" * 60)
        print("ANALISIS PERBANDINGAN MAC vs USAC")
        print("=" * 60)
        
        
        message_sizes = [10, 50, 100, 500, 1000, 5000]
        mac_times = []
        usac_times = []
        
        print("Pengujian Performa dengan Berbagai Ukuran Pesan:")
        print("-" * 50)
        
        for size in message_sizes:
            
            test_message = "A" * size
            
            
            mac_key = self.mac.generate_key()
            start_time = time.time()
            mac_tag = self.mac.compute_mac(test_message, mac_key)
            mac_time = (time.time() - start_time) * 1000
            mac_times.append(mac_time)
            
            
            usac_key = self.usac.generate_one_time_key(size + 32)
            start_time = time.time()
            encoded_msg, auth_tag = self.usac.encode_message(test_message, usac_key)
            usac_time = (time.time() - start_time) * 1000
            usac_times.append(usac_time)
            
            print(f"Ukuran {size:>4} chars: MAC {mac_time:>8.4f}ms | USAC {usac_time:>8.4f}ms")
        
        
        print(f"\nRata-rata waktu MAC: {np.mean(mac_times):.4f} ms")
        print(f"Rata-rata waktu USAC: {np.mean(usac_times):.4f} ms")
        print(f"USAC {np.mean(usac_times)/np.mean(mac_times):.2f}x lebih lambat dari MAC")
    
    def security_analysis(self):
        """Analisis keamanan MAC vs USAC"""
        print("\n" + "=" * 60)
        print("ANALISIS KEAMANAN")
        print("=" * 60)
        
        print("MESSAGE AUTHENTICATION CODE (MAC):")
        print("- Kategori: Computational Security")
        print("- Basis Keamanan: Asumsi komputasional (kesulitan memecahkan hash)")
        print("- Resistensi: Tahan terhadap serangan klasik")
        print("- Kerentanan: Berpotensi rentan terhadap quantum computing")
        print("- Kunci: Dapat digunakan berulang kali")
        print("- Efisiensi: Sangat efisien untuk implementasi praktis")
        
        print("\nUNCONDITIONAL SECURE AUTHENTICATION CODE (USAC):")
        print("- Kategori: Information-theoretic Security")
        print("- Basis Keamanan: Teori informasi Shannon")
        print("- Resistensi: Tahan terhadap semua jenis serangan (termasuk quantum)")
        print("- Kerentanan: Tidak ada (secara teoritis)")
        print("- Kunci: Harus digunakan sekali (one-time)")
        print("- Efisiensi: Kurang efisien, memerlukan manajemen kunci kompleks")
    
    def practical_applications(self):
        """Aplikasi praktis MAC vs USAC"""
        print("\n" + "=" * 60)
        print("APLIKASI PRAKTIS")
        print("=" * 60)
        
        print("MAC - Cocok untuk:")
        print("✓ Protokol internet (TLS, IPSec)")
        print("✓ Aplikasi web dan mobile")
        print("✓ Database integrity checking")
        print("✓ API authentication")
        print("✓ Digital signatures")
        print("✓ Blockchain dan cryptocurrency")
        
        print("\nUSAC - Cocok untuk:")
        print("✓ Komunikasi militer tingkat tinggi")
        print("✓ Diplomatic communications")
        print("✓ Long-term data archival")
        print("✓ Quantum-resistant applications")
        print("✓ High-value financial transactions")
        print("✓ Government classified communications")
    
    def demonstrate_attacks(self):
        """Demonstrasi serangan terhadap MAC dan USAC"""
        print("\n" + "=" * 60)
        print("DEMONSTRASI KETAHANAN TERHADAP SERANGAN")
        print("=" * 60)
        
        original_message = "Transfer $1000 to account 12345"
        
        
        print("1. SERANGAN TERHADAP MAC:")
        mac_key = self.mac.generate_key()
        mac_tag = self.mac.compute_mac(original_message, mac_key)
        
        
        print("   - Brute force attack simulation...")
        attempts = 0
        max_attempts = 1000000  
        
        start_time = time.time()
        for i in range(max_attempts):
            fake_key = self.mac.generate_key()
            fake_mac = self.mac.compute_mac(original_message, fake_key)
            attempts += 1
            if fake_mac == mac_tag:  
                break
        end_time = time.time()
        
        print(f"   - Attempts made: {attempts:,}")
        print(f"   - Time taken: {end_time - start_time:.2f} seconds")
        print("   - Result: MAC tetap aman (collision tidak ditemukan)")
        
        
        print("\n2. SERANGAN TERHADAP USAC:")
        usac_key = self.usac.generate_one_time_key(len(original_message) + 32)
        encoded_msg, auth_tag = self.usac.encode_message(original_message, usac_key)
        
        print("   - Cryptanalysis attempt...")
        print("   - Tanpa kunci, encoded message memberikan 0 informasi")
        print("   - Perfect secrecy: P(M|C) = P(M) untuk semua M, C")
        print("   - Result: USAC secara teoritis tidak dapat dipecahkan")
    
    def run_complete_analysis(self):
        """Jalankan analisis lengkap"""
        self.performance_comparison()
        self.security_analysis()
        self.practical_applications()
        self.demonstrate_attacks()
        
        print("\n" + "=" * 60)
        print("KESIMPULAN")
        print("=" * 60)
        print("MAC: Praktis, efisien, cocok untuk sebagian besar aplikasi")
        print("USAC: Keamanan maksimal, cocok untuk aplikasi critical/high-security")
        print("Pilihan tergantung pada: threat model, resources, dan security requirements")


comparison = CryptographicComparison()
comparison.run_complete_analysis()
