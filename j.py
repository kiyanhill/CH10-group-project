import pickle
file = open("inventory.dat", "rb")
data = pickle.load(file)

while data != "":
    print(data)
    try:
        data = pickle.load(file)
    except:
        data = ""