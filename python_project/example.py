import weiron

guns1 = weiron.Guns(damage=25)
emeny1 = weiron.Enemy(name = 'robot', hp=100)

# round guns1 and emeny1.
round = guns1.__damage_fnc__(emeny1)
print(round)