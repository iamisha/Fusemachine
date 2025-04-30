mylist = ["apple", "banana", "cherry"]
print(mylist)

# empty list
mylist2 = list()
print(mylist2)

# list can contain different datatypes
mylist3 = [2, True, "RL", 3.14, (6,7,8)]
print(mylist3)

#accessing an element in list
item = mylist[-2] # [-1] to access the last item, [-2] to second last item
print(item)

# forloop to iterate through a list
for i in mylist:
    print(i)

# check if an item is inside the loop
if "cherry" in mylist:
    print("yes")
else:
    print("No")

# check the number of elements inside list
print(len(mylist))

# append item in list
mylist.append("lemon")
print(mylist)

# insert itam at specific index
mylist.insert(0, "blueberry")
print(mylist)

# remove an element in list
item = mylist.pop()
print(item)
print(mylist)

# remove a specific element in list
item = mylist.remove("apple")
print(mylist)

# reverse the list
mylist.reverse()
print(mylist)


# remove all elements 
mylist.clear()
print(mylist)
