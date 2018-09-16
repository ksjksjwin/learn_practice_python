"""
1.Nodes are the fundamental building block of many computer science data structures. They form the basis for linked lists, stacks, queues, trees, and more.

An individual node contains data and links to other nodes. Each data structure adds additional constraints or behavior to these features to create the desired structure.

2. The link or links within the node are sometimes referred to as pointers. This is because they "point" to another node.

Typically, data structures implement nodes with one or more links. If these links are null, it denotes that you have reached the end of the particular node or link path you were previously following.

3. If you inadvertently remove the single link to a node, that node's data and any linked nodes could be "lost" to your application. When this happens to a node, it is considered an orphaned node.

Summary: 

- Contain data, which can be a variety of data types
- Contain links to other nodes. If a node has no links, or they are all null, you have reached the end of the path you were following.
- Can be orphaned if there are no existing links to them

"""

class Node:
  def __init__(self,value,link_node = None):
    self.value = value
    self.link_node = link_node
    
  def get_value(self):
    return self.value
  
  def get_link_node(self):
    return self.link_node
