# -*- coding: utf-8 -*-
class BinaryT:
    def __init__(self, value):
        self.value = value
        self.children = []

    def addR(self, value1, value2):
        if len(self.children) == 2:
            return
        if value1.value < value2.value:
            self.children.append(value1)
            self.children.append(value2)
            print(value1.value , value2.value)
            return
        if value1.value > value2.value:
            self.children.append(value2)
            self.children.append(value1)
            print(value2.value , value1.value)
            return
    def delete(self, value):
        newChild = [i for i in self.children if i.value != value.value]
        self.children = newChild

    def math(self):
        info = [self]
        while len(info) > 0:
            current = info.pop()
            print(current.value)
            info += current.children
root = BinaryT(2)
root1 = BinaryT(3)
root2 = BinaryT(1)
root3 = BinaryT(4)
root4 = BinaryT(5)
root5 = BinaryT(6)
root6 = BinaryT(7)
root.addR(root1, root2)
root1.addR(root3, root4)
root2.addR(root5, root6)

root.math()
