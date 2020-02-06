class LevelOrderTraversal:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def traversal(self, root):
        if root is None:
            return
        l = []
        l.append(root)
        while len(l) > 0:
            print(l[0].data)
            p = l.pop(0)
            if p.left is not None:
                l.append(p.left)
            if p.right is not None:
                l.append(p.right)
    
c1 = LevelOrderTraversal(6)
c1.left = LevelOrderTraversal(4)
c1.left.right = LevelOrderTraversal(5)
c1.right = LevelOrderTraversal(9)
c1.left.left = LevelOrderTraversal(1)
c1.right.right = LevelOrderTraversal(12)
c1.traversal(c1)