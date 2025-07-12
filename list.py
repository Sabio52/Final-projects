first = ["Apple", "Banana", "Cherry", "Mango", "Blueberry"]

print("length of first:", len(first))
print("first fruit:", first[0])
print("last fruit:", first[-1])
first.append("Orange")
print("Updated list:", first)
first.remove("Banana")
print("After removing Banana:", first)
first.sort()
print("Sorted list:", first)
first.reverse()
print("Reversed list:", first)
print("multiplication of list:", first * 2)
first.pop(2)
print("After popping:", first)
first.clear()
print("After clearing the list:", first)

# next activity

info = {"name": "John", "age": 30, "city": "New York"}
print("details in info:", info)
info["country"] = "bangladesh"
print("After adding country:", info)
info["age"] = 31
print("After updating age:", info)
info.pop("city")
print("After removing city:", info)
info.clear()
print("After clearing info:", info)