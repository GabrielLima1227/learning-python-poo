class MaxSizeList:
    def __init__(self, max_size: int, initial_list: list = None) -> None:
        self.max_size = max_size
        self._list_data = initial_list if initial_list is not None else []

    @property
    def list(self):
        return self._list_data

    def push(self, item) -> None:
        if len(self._list_data) < self.max_size:
            self._list_data.append(item)

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

print(list_a.list)
print(list_b.list)