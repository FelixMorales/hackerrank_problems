# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?isFullScreen=true

from typing import List


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left: Node = None  
        self.right: Node = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

v1_path = []
v2_path = []

def lca(root, v1, v2):
    if not root:
        return
    
    r = helper(node=root, current_path=[root], v1=v1, v2=v2)

    return r

def helper(node: Node, current_path: List, v1: int, v2: int):

    global v1_path, v2_path
    
    result = None
    if node:
        if node.info == v1:
            v1_path = current_path.copy()
            if len(v2_path) > 0:
                return get_lowest_ancestor()
                
        elif node.info == v2:
            v2_path = current_path.copy()
            if len(v1_path) > 0:
                return get_lowest_ancestor()
                
        if node.left:
            result = helper(node=node.left, current_path=current_path+[node.left], v1=v1, v2=v2)
        
        if node.right and not result:
            result = helper(node=node.right, current_path=current_path+[node.right], v1=v1, v2=v2)

    return result

def get_lowest_ancestor():
    global v1_path, v2_path

    for i in range(len(v1_path)-1, -1, -1):
        for j in range(len(v2_path)-1, -1, -1):
            if v1_path[i].info == v2_path[j].info:
                return v1_path[i]



    

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)