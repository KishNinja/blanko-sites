# feature.py
import main
# Что бы пользоватся функциями из других файлов, нужно сначала прописать название 
# файла с которого мы берем функцию.

# iphone16 = main.Iphone('Iphone 16', 'Black', 1200, 16, 256, 18.1)
# print(iphone16)
# print(iphone16.__norma_phone__())
guns1 = main.Guns(damage=25)
emeny1 = main.Enemy(name = 'robot', hp=100)

# round guns1 and emeny1.
round = guns1.__damage_fnc__(emeny1)

mersedes = main.Car(color='Black', number='AE 1243 VB', weight=1000, price='3500$')
# print(mersedes.__pricefnc__())
print(main.date_json)

with open('python_project/date.json', 'w') as file:
    main.json.dump(main.date_json, file, indent=2)