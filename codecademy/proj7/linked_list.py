"""

Linked Lists:

1.Are comprised of nodes
2.The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
3.Can be unidirectional or bidirectional
4.Are a basic data structure, and form the basis for many other data structures
5.Have a single head node, which serves as the first node in the list
6.Require some maintenance in order to add or remove nodes
7.The methods we used are an example and depend on the exact use case and/or programming language being used

- Defining a Node class to hold the values and links between nodes
- Implementing a LinkedList class to handle external operations on the list like adding and removing nodes
"""

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.value != None:
        string_list += str(current_node.value) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.next_node = next_node.get_next_node()
          current_node = None
        else:
          current_node = next_node
