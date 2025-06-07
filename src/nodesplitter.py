
from textnode import TextNode,TextType
from extractors import extract_markdown_links,extract_markdown_images

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
            continue
        split_node=node.text.split(delimiter)
        if len(split_node)%2==0:
            raise Exception("closing delimiter missing")
        for i in range(0,len(split_node)):
            if split_node[i]:
                if i%2==0:
                    new_nodes.append(TextNode(split_node[i],TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_node[i],text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
            continue
        images=extract_markdown_images(node.text)
        if images==None or images==[]:
            new_nodes.append(node)
            continue
        for image in images:
            split_node=node.text.split(f"![{image[0]}]({image[1]})",1)
            
            
            if split_node[0]!="":
                new_nodes.append(TextNode(split_node[0],TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
            if split_node[1]!="":
                node=TextNode(split_node[1],TextType.TEXT)
            
        if split_node[1]!="":
            new_nodes.append(TextNode(split_node[1],TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
            continue
        links=extract_markdown_links(node.text)
        if links==None or links==[]:
            new_nodes.append(node)
            continue
        for link in links:
            split_node=node.text.split(f"[{link[0]}]({link[1]})",1)

            if split_node[0]!="":
                new_nodes.append(TextNode(split_node[0],TextType.TEXT))
            new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
            if split_node[1]!="":
                node=TextNode(split_node[1],TextType.TEXT)
            
        if split_node[1]!="":
            new_nodes.append(TextNode(split_node[1],TextType.TEXT))
    return new_nodes