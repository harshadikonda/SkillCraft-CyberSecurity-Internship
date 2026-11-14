from PIL import Image

# Open encrypted image
img = Image.open("encrypted.png")
pixels = img.load()

# Same encryption key
key = 50

# Decrypt image
for x in range(img.width):
    for y in range(img.height):
        r, g, b = pixels[x, y][:3]

        pixels[x, y] = (
            (r - key) % 256,
            (g - key) % 256,
            (b - key) % 256
        )

# Save decrypted image
img.save("decrypted.png")

print("Image decrypted successfully!")
print("Saved as decrypted.png")