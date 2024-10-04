import main

# Что бы пользоватся функциями из других файлов, нужно сначала прописать название 
# файла с которого мы берем функцию.

iphone16 = main.Iphone('Iphone 16', 'Black', 1200, 16, 256, 18.1)
print(iphone16)
print(iphone16.__norma_phone__())