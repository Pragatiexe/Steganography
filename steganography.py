from PIL import Image

def encode_message(img_path, message, output_path):
    img = Image.open(img_path)
    encoded = img.copy()
    width, height = img.size
    idx = 0

    message += chr(0)  
    binary_msg = ''.join(format(ord(i), '08b') for i in message)

    for row in range(height):
        for col in range(width):
            if idx < len(binary_msg):
                r, g, b = img.getpixel((col, row))
                r = (r & ~1) | int(binary_msg[idx])  
                encoded.putpixel((col, row), (r, g, b))
                idx += 1
            else:
                encoded.save(output_path)
                return True
    return False

def decode_message(img_path):
    img = Image.open(img_path)
    width, height = img.size
    binary_data = ""
    
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_data += str(r & 1)

    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""
    for ch in chars:
        if int(ch, 2) == 0:
            break
        message += chr(int(ch, 2))
    return message
