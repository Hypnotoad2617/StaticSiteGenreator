from textnode import *

def is_odd(number):
    return number % 2 != 0

def is_even(number):
    return number % 2 == 0

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        section = old_node.text.split(delimiter)
        if is_even(len(section)):
               raise ValueError(f"Invalid markdown! No closing {delimiter} found!")
        for i in range(len(section)):
            if section[i] == "":
                continue
            if is_even(i):
                split_nodes.append(TextNode(section[i],TextType.TEXT))
            else:
                split_nodes.append(TextNode(section[i], text_type))
        new_nodes.extend(split_nodes)                       
    return new_nodes     




    
   # If an "old node" is not a TextType.TEXT type, just add it to the new list as-is, we only attempt to split "text" type objects (not bold, italic, etc).
    #If a matching closing delimiter is not found, just raise an exception with a helpful error message, that's invalid Markdown syntax.
    #The .split() string method was useful
    #The .extend() list method was useful. extend attaches a list after another, changeing the initial list a.extend(b) 
