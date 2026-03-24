#assignment4
dict={"a":1,"b":2}
print("old dictionary:",dict)
dict["c"]=3
dict["a"]=10
dict.pop("c")
print(dict)
dict1={"c":3,"d":4}
dict.update(dict1)
print("using update function:",dict)
print("using slash function:",dict|dict1)
del dict["a"]
print(dict)
dict.clear()
print(dict)
