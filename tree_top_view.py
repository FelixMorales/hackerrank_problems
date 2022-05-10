# https://www.hackerrank.com/challenges/tree-top-view/problem?isFullScreen=true

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
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

top_left_view = 0
top_right_view = 0

values = {}

def topView(root: Node):
    if not root:
        return
    
    global values, top_right_view


    calculate_top_right_view(node=root.right, view_point=1)

    values[0] = root.info

    if root.left:
        helper(node=root.left, view_point=-1, direction='left')

    top_right_view = 0

    if root.right:
        helper(node=root.right, view_point=1, direction='right')
    
    values = sorted(values.items())

    result = ''
    for i in range(len(values)):
        result += f'{values[i][1]} '
    
    print(result)

def calculate_top_right_view(node: Node, view_point: int):

    global top_right_view

    if view_point > top_right_view:
        top_right_view = max(view_point, top_right_view)

    if node.right:
        calculate_top_right_view(node=node.right, view_point=view_point+1)
    
    if node.left:
        calculate_top_right_view(node=node.left, view_point=view_point-1)

def helper(node: Node, view_point: int, direction: str):

    global top_left_view, top_right_view, values

    if view_point > top_right_view:
        values[view_point] = node.info
        top_right_view = max(top_right_view, view_point)
    
    if view_point < top_left_view:
        values[view_point] = node.info
        top_left_view = min(view_point, top_left_view)

    if direction == 'left':
        if node.left:
            helper(node=node.left, view_point=view_point-1, direction='left')
            
        if node.right:
            helper(node=node.right, view_point=view_point+1, direction='right')
    
    else:
        if node.right:
            helper(node=node.right, view_point=view_point+1, direction='right')
            
        if node.left:
            helper(node=node.left, view_point=view_point-1, direction='left')


    

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)