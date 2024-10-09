# feature.py
import main
import json
# Что бы пользоватся функциями из других файлов, нужно сначала прописать название 
# файла с которого мы берем функцию.

# iphone16 = main.Iphone('Iphone 16', 'Black', 1200, 16, 256, 18.1)
# print(iphone16)
# print(iphone16.__norma_phone__())
guns1 = main.Guns(damage=25)
emeny1 = main.Enemy(name = 'robot', hp=100)

# round guns1 and emeny1.
round = guns1.__damage_fnc__(emeny1)


# print(main.json.dumps(main.oxxxymiron_json, indent=2))
with open('python_project/date.json', 'w',  encoding='utf-8') as file:
    main.json.dump(main.oxxxymiron_json, file, ensure_ascii=False, indent=2)