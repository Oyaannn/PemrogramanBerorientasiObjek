class TicketSoldOutError(Exception):
    """Exception raised when tickets are sold out."""
    def __init__(self, message="Tiket sudah habis."):
        self.message = message
        super().__init__(self.message)

class InvalidTicketQuantityError(Exception):
    """Exception raised for invalid ticket quantity."""
    def __init__(self, quantity, message="Jumlah tiket tidak valid."):
        self.quantity = quantity
        self.message = message
        super().__init__(self.message)

class PaymentFailedError(Exception):
    """Exception raised when payment fails."""
    def __init__(self, message="Pembayaran gagal. Silakan coba lagi."):
        self.message = message
        super().__init__(self.message)

class TicketBookingSystem:
    def __init__(self, available_tickets):
        self.available_tickets = available_tickets

    def book_tickets(self, quantity):
        if quantity <= 0:
            raise InvalidTicketQuantityError(quantity)
        if quantity > self.available_tickets:
            raise TicketSoldOutError()
        
        # Simulasi proses pembayaran
        if not self.process_payment(quantity):
            raise PaymentFailedError()

        self.available_tickets -= quantity
        print(f"{quantity} tiket berhasil dipesan. Tiket yang tersisa: {self.available_tickets}")

    def process_payment(self, quantity):
        # Simulasi pembayaran yang mungkin gagal
        import random
        return random.choice([True, False])  # 50% kemungkinan berhasil

if __name__ == "__main__":
    booking_system = TicketBookingSystem(5)  # Tersedia 5 tiket

    print("==============Selamat datang di Sistem Pemesanan Tiket!==============")
    print(f"Tiket yang tersedia saat ini: {booking_system.available_tickets}")

    while True:
        try:
            user_input = input("Masukkan jumlah tiket yang ingin dipesan (atau ketik 'exit' untuk keluar): ")
            if user_input.lower() == 'exit':
                print("Terima kasih telah menggunakan Sistem Pemesanan Tiket.")
                break

            quantity = int(user_input)
            booking_system.book_tickets(quantity)

            if booking_system.available_tickets == 0:
                print("Tiket sudah habis. Pemesanan ditutup.")
                break

        except ValueError:
            print("Input tidak valid. Harap masukkan angka bulat positif.")
        except TicketSoldOutError as e:
            print(f"Kesalahan: {e}")
        except InvalidTicketQuantityError as e:
            print(f"Kesalahan: {e.message} Jumlah yang diminta: {e.quantity}")
        except PaymentFailedError as e:
            print(f"Kesalahan: {e}")