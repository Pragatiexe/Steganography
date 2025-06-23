from steganography import encode_message, decode_message

def main():
    while True:
        print("\n--- Steganography Menu ---")
        print("1. Encode message")
        print("2. Decode message")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            path = input("Enter image path (e.g., input_image.png): ")
            msg = input("Enter secret message: ")
            out = input("Enter output image name (e.g., output_image.png): ")
            if encode_message(path, msg, out):
                print("✅ Message encoded successfully!")
            else:
                print("❌ Encoding failed.")
        elif choice == '2':
            path = input("Enter image path to decode (e.g., output_image.png): ")
            print("🔓 Decoded message:", decode_message(path))
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
