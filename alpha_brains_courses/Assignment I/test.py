import MaxSizeList

list_a = MaxSizeList(3)
list_b = MaxSizeList(1)

list_a.push("Hey")
list_a.push("Hi")
list_a.push("let's")
list_a.push("go")

list_b.push("Hey")
list_b.push("Hi")
list_b.push("let's")
list_b.push("go")

print(list_a.list())
print(list_a.list())