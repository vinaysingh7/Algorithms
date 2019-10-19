from collections import deque
def solution(arr):
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.right = None
            self.left = None 
    print("here")
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if not node:
            continue
        print(arr[i])
        if i < len(arr) and arr[i] != -1:
            node.left = TreeNode(arr[i])
            print("left", node.val, node.left.val)
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] != -1:
            node.right = TreeNode(arr[i])
            print("right", node.val, node.right.val)
            q.append(node.right)
        i += 1
solution([3,6,2,9,-1,10])
   
        
        
        

 
