from collections import deque


def bfs(root):
    if root is None:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result


def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]