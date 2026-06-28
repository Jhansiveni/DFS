# DFS Traversal code
class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]
def dfs(root):
    if not root:
        return
    print(root.value,end=" ")

    for child in root.children:
        dfs(child)
