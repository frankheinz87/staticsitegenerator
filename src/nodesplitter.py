
from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes=[]
    for node in old_nodes:
        split_node=node.split(delimiter)
        if len(split_node)%2==0:
            raise Exception("closing delimiter missing")
        for i in range(0,len(split_node)):
            if i%2==0:
                new_nodes.append(TextNode(split_node[i],TextType.NORMAL))
            else:
                new_nodes.append(TextNode(split_node[i],text_type))
    
    return new_nodes