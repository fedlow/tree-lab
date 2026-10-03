from binary_tree import BinaryTree
from avl_tree import AVLTree
from traversals import bfs, preorder, inorder, postorder


print("=== 1. BinaryTree ===")
bt = BinaryTree()
for v in [50, 30, 70, 20, 40, 60, 80]:
    bt.insert(v)
print(f"search(40)  = {bt.search(40)}")
print(f"search(45)  = {bt.search(45)}")
print(f"search(80)  = {bt.search(80)}")

print("\n=== 2. BFS ===")
print(f"BFS: {bfs(bt.root)}")

print("\n=== 3. DFS ===")
print(f"preorder:  {preorder(bt.root)}")
print(f"inorder:   {inorder(bt.root)}")
print(f"postorder: {postorder(bt.root)}")

print("\n=== 4. AVLTree: последовательная вставка 10..50 ===")
avl = AVLTree()
for v in [10, 20, 30, 40, 50, 25]:
    avl.insert(v)
    print(f"  после insert({v}): корень = {avl.root.value}, высота = {avl.root.height}")

print(f"\nInorder AVL: {inorder(avl.root)}  (должен быть отсортирован)")
print(f"BFS AVL:     {bfs(avl.root)}")