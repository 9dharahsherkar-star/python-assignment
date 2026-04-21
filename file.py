#create file
f=open("data.txt","w")
f.write("hello\n")
print("file created successfully!!")
f.close()

#read file
f=open("data.txt")
print(f.read())
f.close()

#append
f=open("data.txt","a")
f.write("how are you?")
print("content appended successfully!!")
f=open("data.txt")
print(f.read())
f.close()

f=open("data.txt","r")
print(f.read())


f=open("data.txt","w")
f.write("mit adt university")
f=open("data.txt","r")
print(f.read())
f.close()
