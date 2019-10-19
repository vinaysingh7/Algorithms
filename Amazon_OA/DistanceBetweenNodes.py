class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def create_bst(nums):
    root = TreeNode(nums[0])
    for num in nums[1:]:
        node = root
        while node:
            if num < node.val:
                if not node.left: 
                    node.left = TreeNode(num)
                node = node.left
            else:
                if not node.right: 
                    node.right = TreeNode(num)
                node = node.right
    return root

def get_distance(root, val1, val2):
    arr1, arr2 = [], []
    
    def traverse(root, val, path):
        if not root: return path.clear()
        path += root.val,
        if root.val == val:
            return path
        if val < root.val:
            return traverse(root.left, val, path)
        else:
            return traverse(root.right, val, path)
    
    traverse(root, val1, arr1)
    traverse(root, val2, arr2)
    if not arr1 or not arr2: return -1
    i = 0
    while i < len(arr1) and i < len(arr2):
        if arr1[i] == arr2[i]:
            i += 1
        else:
            i -= 1
            break
    print(i, arr1, arr2)
    return (len(arr1)-1 - i) + (len(arr2)-1 - i)


root = create_bst([2, 1, 3,4])
print(get_distance(root, 1,3))

                
