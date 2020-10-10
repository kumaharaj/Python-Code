
import os
print(os.getcwd())
os.chdir("/home/kmahraj/Documents/Newfolder")
print(os.getcwd())
os.mkdir("/home/kmahraj/Documents/Newfolder/new1")
os.mkdir("/home/kmahraj/Documents/Newfolder/new2")
os.rmdir("/home/kmahraj/Documents/Newfolder/new2")
os.remove("/home/kmahraj/Documents/Newfolder/file.txt")
print(os.path.join("/home/kmahraj/Documents", "/home/kmahraj/Documents/Newfolder/new1"))
print(os.path.split("/home/kmahraj/Documents/Newfolder/new1"))
print(os.path.exists("/home/kmahraj/Documents/Newfolder/new1"))
print(os.path.exists("/home/kmahraj/Documents/Newfolder/new2"))
print(os.path.exists("/home/kmahraj/Documents/Newfolder/new3"))
