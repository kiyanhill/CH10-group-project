import pickle

file = open("inventory.dat", "rb")

loaded = pickle.load(file)
print(loaded)