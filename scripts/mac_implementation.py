import hashlib
import hmac
import secrets
import time
from typing import Tuple, Optional

class MACImplementation:
    """
    Message Authentication Code (MAC) Implementation
    
    Deskripsi: MAC adalah algoritma kriptografi yang menggunakan kunci rahasia
    untuk menghasilkan tag autentikasi dari sebuah pesan.
    
    Penemu: Konsep MAC dikembangkan pada tahun 1970-an oleh Whitfield Diffie
    dan Martin Hellman sebagai bagian dari kriptografi kunci publik.
    """
    
    def __init__(self, algorithm: str = 'sha256'):
        """
        Inisialisasi MAC dengan algoritma hash tertentu
        
        Args:
            algorithm: Algoritma hash yang digunakan (sha256, sha1, md5)
        """
        self.algorithm = algorithm
        self.supported_algorithms = ['sha256', 'sha1', 'md5', 'sha512']
        
        if algorithm not in self.supported_algorithms:
            raise ValueError(f"Algorithm {algorithm} not supported")
    
    def generate_key(self, length: int = 32) -> bytes:
        """
        Generate kunci rahasia secara acak
        
        Args:
            length: Panjang kunci dalam bytes
            
        Returns:
            Kunci rahasia dalam bentuk bytes
        """
        return secrets.token_bytes(length)
    
    def compute_mac(self, message: str, key: bytes) -> str:
        """
        Menghitung MAC dari pesan menggunakan HMAC
        
        Args:
            message: Pesan yang akan di-MAC
            key: Kunci rahasia
            
        Returns:
            MAC dalam format hexadecimal
        """
        message_bytes = message.encode('utf-8')
        mac_object = hmac.new(key, message_bytes, getattr(hashlib, self.algorithm))
        return mac_object.hexdigest()
    
    def verify_mac(self, message: str, key: bytes, received_mac: str) -> bool:
        """
        Verifikasi MAC untuk memastikan integritas pesan
        
        Args:
            message: Pesan asli
            key: Kunci rahasia
            received_mac: MAC yang diterima
            
        Returns:
            True jika MAC valid, False jika tidak
        """
        computed_mac = self.compute_mac(message, key)
        return hmac.compare_digest(computed_mac, received_mac)
    
    def demonstrate_mac(self):
        """Demonstrasi penggunaan MAC"""
        print("=" * 60)
        print("DEMONSTRASI MESSAGE AUTHENTICATION CODE (MAC)")
        print("=" * 60)
        
        
        key = self.generate_key()
        print(f"Kunci yang digunakan: {key.hex()}")
        
        
        original_message = "Ini adalah pesan rahasia yang harus diautentikasi"
        print(f"Pesan asli: {original_message}")
        
        
        start_time = time.time()
        mac_tag = self.compute_mac(original_message, key)
        end_time = time.time()
        
        print(f"MAC Tag ({self.algorithm}): {mac_tag}")
        print(f"Waktu komputasi: {(end_time - start_time) * 1000:.4f} ms")
        
        
        is_valid = self.verify_mac(original_message, key, mac_tag)
        print(f"Verifikasi MAC (pesan asli): {'VALID' if is_valid else 'INVALID'}")
        
        
        tampered_message = "Ini adalah pesan rahasia yang telah diubah"
        is_valid_tampered = self.verify_mac(tampered_message, key, mac_tag)
        print(f"Verifikasi MAC (pesan diubah): {'VALID' if is_valid_tampered else 'INVALID'}")
        
        
        print("\n--- Perbandingan Algoritma MAC ---")
        algorithms = ['md5', 'sha1', 'sha256', 'sha512']
        
        for algo in algorithms:
            try:
                mac_impl = MACImplementation(algo)
                start_time = time.time()
                mac_result = mac_impl.compute_mac(original_message, key)
                end_time = time.time()
                
                print(f"{algo.upper():>8}: {mac_result} ({(end_time - start_time) * 1000:.4f} ms)")
            except Exception as e:
                print(f"{algo.upper():>8}: Error - {e}")


mac_demo = MACImplementation()
mac_demo.demonstrate_mac()
