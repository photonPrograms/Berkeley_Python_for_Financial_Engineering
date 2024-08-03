import time

# ==== Part 1 =====
def memorize_3s(func):
    result_cache = dict()

    # start the timer
    start_time = time.time()
    
    def f(n):
        nonlocal result_cache, start_time
        # check if we should invalidate the cache
        if time.time() - start_time > 3:
            result_cache = dict()
            start_time = time.time()
        
        if n not in result_cache:
            result_cache[n] = func(n)
        return result_cache[n]
    return f

@memorize_3s
def identity(x):
    print('this function is called')
    return x


identity(1) # there should be a print
identity(1) # there should no print
time.sleep(3)
identity(1) # there should be a print


# ==== Part 2 =====

# this is the definition of the binary tree
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.val = key

# this is saying that the function takes one argument, which is type = Node
# and returns a list of string
def pre_order_recursion(root: Node) -> list[str]:
    if root == None:
        return []
    return [root.val] + pre_order_recursion(root.left) + pre_order_recursion(root.right)

def pre_order_iteration(root: Node) -> list[str]:
    if root == None:
        return []
    result, stack = [], [root]
    while len(stack) > 0:
        curr_node = stack.pop()
        result.append(curr_node.val)
        if curr_node.right != None:
            stack.append(curr_node.right)
        if curr_node.left != None:
            stack.append(curr_node.left)
    return result

def in_order_recursion(root: Node) -> list[str]:
    if root == None:
        return []
    return in_order_recursion(root.left) + [root.val] + in_order_recursion(root.right)

def in_order_iteration(root: Node) -> list[str]:
    curr_node, stack, result = root, [], []
    while True:
        if curr_node != None:
            stack.append(curr_node)
            curr_node = curr_node.left
        elif len(stack) > 0:
            curr_node = stack.pop()
            result.append(curr_node.val)
            curr_node = curr_node.right
        else:
            break
    return result

def post_order_recursion(root: Node) -> list[str]:
    if root == None:
        return []
    return post_order_recursion(root.left) + post_order_recursion(root.right) + [root.val]

def post_order_iteration(root: Node) -> list[str]:
    result, stack = [], [root]
    while len(stack) > 0:
        curr_node = stack.pop()
        if curr_node != None:
            result.append(curr_node.val)
            stack += [curr_node.left, curr_node.right]
    return result[::-1]

# ====== test case below ======
# this is the initiation of the testing object.
# DO NOT MODIFY THIS
root = Node('F', 
    left=Node(
        'B',
        left=Node('A'),
        right=Node('D', left=Node('C'), right=Node('E')),
    ), 
    right=Node('G', right=Node('I', left=Node('H')))
)

assert pre_order_recursion(root) == pre_order_iteration(root) == ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
assert in_order_recursion(root) == in_order_iteration(root) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
assert post_order_recursion(root) == post_order_iteration(root) == ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']