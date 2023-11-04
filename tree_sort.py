class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def add(self, item):
        if self.item > item:
            if self.left is None:
                self.left = Node(item)
            else:
                self.left.add(item)
        else:
            if self.right is None:
                self.right = Node(item)
            else:
                self.right.add(item)

    def sorted(self):
        return [] if self.left is None else self.left.sorted() + [self.item] + [] if self.right is None else self.right.sorted()

def tree_sort(arr):
    if len(arr) == 0:
        return []
    root = Node(arr[0])
    for i in arr[1:]:
        root.add(i)
    return root.sorted()
