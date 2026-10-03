from binary_tree import BinaryTree, Node


class AVLTree(BinaryTree):
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node

        self._update_height(node)
        return self.rebalance(node)


    def left_rotate(self, z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        self._update_height(z)
        self._update_height(y)
        return y

    def right_rotate(self, z):
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3
        self._update_height(z)
        self._update_height(y)
        return y

    def rebalance(self, node):
        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node