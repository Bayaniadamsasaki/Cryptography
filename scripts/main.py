"""
Program Utama - Demonstrasi MAC dan USAC
"""

def print_header():
    print("\n" + "=" * 80)
    print("KRIPTOGRAFI HASH - MESSAGE AUTHENTICATION CODE & UNCONDITIONAL SECURE AUTHENTICATION CODE")
    print("=" * 80)
    print("\nProgram ini mendemonstrasikan konsep dan implementasi:")
    print("1. Message Authentication Code (MAC)")
    print("2. Unconditional Secure Authentication Code (USAC)")
    print("-" * 80)

if __name__ == "__main__":
    print_header()
    
    print("\nMenjalankan demonstrasi MAC...")
    from mac_implementation import MACImplementation
    mac_demo = MACImplementation()
    mac_demo.demonstrate_mac()
    
    print("\nMenjalankan demonstrasi USAC...")
    from usac_implementation import USACImplementation
    usac_demo = USACImplementation()
    usac_demo.demonstrate_usac()
    
    print("\nMenjalankan demonstrasi edukatif...")
    from educational_demo import educational_demonstration
    educational_demonstration()
    
    print("\n" + "=" * 80)
    print("PROGRAM SELESAI")
    print("=" * 80)
