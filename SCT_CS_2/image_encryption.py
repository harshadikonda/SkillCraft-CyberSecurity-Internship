from PIL import Image

# Open original image
img = Image.open("original.png")
pixels = img.load()

# Encryption key
key = 50

# Encrypt image
for x in range(img.width):
    for y in range(img.height):
        r, g, b = pixels[x, y][:3]

        pixels[x, y] = (
            (r + key) % 256,
            (g + key) % 256,
            (b + key) % 256
        )

# Save encrypted image
img.save("encrypted.png")

print("Image encrypted successfully!")
print("Saved as encrypted.png")