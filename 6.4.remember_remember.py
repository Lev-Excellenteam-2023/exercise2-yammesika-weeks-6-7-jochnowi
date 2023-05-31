from PIL import Image


def decode_message(image_path):

    image = Image.open(image_path)
    width, height = image.size

    black_pixels = []

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel == 1:
                black_pixels.append(y)

    encrypted = ''.join(chr(p) for p in black_pixels)

    return encrypted


message = decode_message("code.png")
print(message)

