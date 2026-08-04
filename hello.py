import os

folder = "."

for filename in os.listdir(folder):
    path = os.path.join(folder,filename)
    size = os.path.getsize(path)
    print(filename, size, "bytes")
