from PIL import Image  # you can import it by running 'pip install Pillow'

print('Enter .jpg file name:')
name = input()
file = Image.open(name)
name = name.replace(".jpg", ".png")
file.save(name)
