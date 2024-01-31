class Node:
    def __init__(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child

    def height(self):
        return self.calheight(self)

    def calheight(self,node):
        if node is None:
            return 0
        else:
            print("left")
            left = self.calheight(node.left_child)
            print("right")
            right= self.calheight(node.right_child)

            return max(left,right)+1


if __name__ == "__main__":
    leaf1 = Node(None, None)
    leaf2 = Node(None, None)
    node = Node(leaf1, None)
    root = Node(node, leaf2)

    print(root.height())