# Time: O(n) 
# Space: O(h)

# Do a inorder traversal adding elements in an array
# After all the root nodes are added check if array is sorted if yes return true else return false
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        self.helper(root,inorder)
        print(inorder)
        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True
    
    def helper(self,root,inorder):
        # base case
        if root == None:
            return

        # logic
        self.helper(root.left,inorder)
        inorder.append(root.val)
        self.helper(root.right,inorder)


# Time: O(n)
# Space: O(1)

# Instead of having an extra array we can do it in place having a previous and a current pointer (The current is the root.val at a particualr point)
# BST is generated in a order where every previous element is < than the next element in the inorder traversal
# so in inorder we check if the previous element is >= the current one if yes we change that flaf to false and then return it
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        self.flag = True
        self.helper(root)
        return self.flag
        
    
    def helper(self,root):
        # base case
        if root == None:
            return

        # logic
        self.helper(root.left)

        if self.prev != None and self.prev >=root.val:
            self.flag = False
        self.prev = root.val

        self.helper(root.right)