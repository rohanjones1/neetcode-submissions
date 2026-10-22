"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}
        
        def dfs(n):
            if n in mapping:
                return

            newNode = Node(n.val, None)
            mapping[n] = newNode

            for nbr in n.neighbors:
                dfs(nbr)
            for nbr in n.neighbors:
                mapping[n].neighbors.append(mapping[nbr])

            return
        if not node:
            return None
        
        dfs(node)

        return mapping[node]
        
            


