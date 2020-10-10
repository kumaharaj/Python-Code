import os
print(os.getcwd())
os.chdir("C:\\Users\\km892448\Documents\\New folder")
print(os.getcwd())
os.mkdir("C:\\Users\\km892448\Documents\\New folder\\new1")
os.mkdir("C:\\Users\\km892448\Documents\\New folder\\new2")
os.rmdir("C:\\Users\\km892448\Documents\\New folder\\new2")
os.remove("C:\\Users\\km892448\Documents\\New folder\\file.txt")
print(os.path.join("C:\\Users\\km892448\Documents", "C:\\Users\\km892448\Documents\\New folder\\new1"))
print(os.path.split("C:\\Users\\km892448\Documents\\New folder\\new1"))
print(os.path.exists("C:\\Users\\km892448\Documents\\New folder\\new1"))
print(os.path.exists("C:\\Users\\km892448\Documents\\New folder\\new2"))

