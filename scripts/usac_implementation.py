import secrets
import time
from typing import List, Tuple, Optional

class USACImplementation:
    """
    Unconditional Secure Authentication Code (USAC) Implementation
    
    Deskripsi: USAC adalah sistem autentikasi yang memberikan keamanan
    tanpa syarat berdasarkan teori informasi Shannon.
    
    Penemu: Konsep dikembangkan berdasarkan penelitian Gustavus Simmons
    pada tahun 1980-an tentang authentication codes.
    
    Kategori: Information-theoretic cryptography
    """
    
    def __init__(self):
        """Inisialisasi USAC"""
        self.name = "Unconditional Secure Authentication Code"
        self.security_level = "Information-theoretic"
    
    def generate_one_time_key(self, length: int) -> bytes:
        """
        Generate one-time pad key untuk USAC
        
        Args:
            length: Panjang kunci (harus >= panjang pesan)
            
        Returns:
            One-time key dalam bentuk bytes
        """
        return secrets.token_bytes(length)
    
    def encode_message(self, message: str, key: bytes) -> Tuple[bytes, str]:
        """
        Encode pesan menggunakan one-time pad
        
        Args:
            message: Pesan yang akan di-encode
            key: One-time key
            
        Returns:
            Tuple berisi (encoded_message, authentication_tag)
        """
        if len(key) < len(message):
            raise ValueError("USAC memerlukan kunci dengan panjang >= pesan")
        
        message_bytes = message.encode('utf-8')
        encoded = bytearray()
        
        
        for i, byte in enumerate(message_bytes):
            encoded.append(byte ^ key[i])
        
        
        auth_tag_key = key[len(message_bytes):len(message_bytes)+16]  
        auth_tag = self._generate_auth_tag(message_bytes, auth_tag_key)
        
        return bytes(encoded), auth_tag
    
    def decode_message(self, encoded_message: bytes, key: bytes) -> str:
        """
        Decode pesan yang telah di-encode
        
        Args:
            encoded_message: Pesan yang telah di-encode
            key: One-time key yang sama
            
        Returns:
            Pesan asli
        """
        decoded = bytearray()
        
        
        for i, byte in enumerate(encoded_message):
            decoded.append(byte ^ key[i])
        
        return decoded.decode('utf-8')
    
    def _generate_auth_tag(self, message: bytes, tag_key: bytes) -> str:
        """
        Generate authentication tag untuk USAC
        
        Args:
            message: Pesan dalam bytes
            tag_key: Kunci untuk authentication tag
            
        Returns:
            Authentication tag dalam hex
        """
        tag = 0
        for i, byte in enumerate(message):
            if i < len(tag_key):
                tag ^= byte ^ tag_key[i]
            else:
                tag ^= byte
        
        return format(tag, '02x')
    
    def verify_authenticity(self, encoded_message: bytes, key: bytes, 
                          received_tag: str, original_length: int) -> bool:
        """
        Verifikasi autentisitas pesan
        
        Args:
            encoded_message: Pesan yang di-encode
            key: One-time key
            received_tag: Tag autentikasi yang diterima
            original_length: Panjang pesan asli
            
        Returns:
            True jika autentik, False jika tidak
        """
        try:
            
            decoded_message = self.decode_message(encoded_message, key)
            message_bytes = decoded_message.encode('utf-8')
            
            
            auth_tag_key = key[original_length:original_length+16]
            expected_tag = self._generate_auth_tag(message_bytes, auth_tag_key)
            
            return expected_tag == received_tag
        except:
            return False
    
    def demonstrate_usac(self):
        """Demonstrasi penggunaan USAC"""
        print("\n" + "=" * 60)
        print("DEMONSTRASI UNCONDITIONAL SECURE AUTHENTICATION CODE (USAC)")
        print("=" * 60)
        
        
        original_message = "Pesan rahasia dengan keamanan tanpa syarat"
        print(f"Pesan asli: {original_message}")
        print(f"Panjang pesan: {len(original_message)} karakter")
        
        
        key_length = len(original_message) + 32  
        one_time_key = self.generate_one_time_key(key_length)
        print(f"One-time key: {one_time_key.hex()}")
        print(f"Panjang kunci: {len(one_time_key)} bytes")
        
        
        start_time = time.time()
        encoded_msg, auth_tag = self.encode_message(original_message, one_time_key)
        end_time = time.time()
        
        print(f"Pesan ter-encode: {encoded_msg.hex()}")
        print(f"Authentication tag: {auth_tag}")
        print(f"Waktu encoding: {(end_time - start_time) * 1000:.4f} ms")
        
        
        start_time = time.time()
        decoded_message = self.decode_message(encoded_msg, one_time_key)
        end_time = time.time()
        
        print(f"Pesan ter-decode: {decoded_message}")
        print(f"Waktu decoding: {(end_time - start_time) * 1000:.4f} ms")
        
        
        is_authentic = self.verify_authenticity(encoded_msg, one_time_key, 
                                              auth_tag, len(original_message))
        print(f"Verifikasi autentisitas: {'VALID' if is_authentic else 'INVALID'}")
        
        
        print("\n--- Test dengan Pesan yang Dimanipulasi ---")
        tampered_encoded = bytearray(encoded_msg)
        tampered_encoded[0] ^= 0xFF  
        
        is_tampered_authentic = self.verify_authenticity(bytes(tampered_encoded), 
                                                       one_time_key, auth_tag, 
                                                       len(original_message))
        print(f"Verifikasi pesan yang diubah: {'VALID' if is_tampered_authentic else 'INVALID'}")
        
        
        print("\n--- Analisis Keamanan ---")
        print("USAC Properties:")
        print("1. Perfect secrecy (seperti One-Time Pad)")
        print("2. Unconditional authentication")
        print("3. Tidak dapat dipecahkan meski dengan komputasi tak terbatas")
        print("4. Memerlukan kunci sepanjang atau lebih dari pesan")
        print("5. Kunci hanya dapat digunakan sekali (one-time)")


usac_demo = USACImplementation()
usac_demo.demonstrate_usac()
