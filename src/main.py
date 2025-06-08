from textnode import TextNode,TextType
from htmlnode import HTMLNode,ParentNode,LeafNode
from nodesplitter import split_nodes_delimiter,split_nodes_image,split_nodes_link

def main():
    Hello=TextNode("Hello World", TextType.LINK, "https://www.boot.dev" )
    Hello2=HTMLNode("p","Hello",[],{"href": "https://www.google.com", "target": "_blank"})
    #print(Hello)
    #print(Hello2)

def text_to_textnodes(text):
    old_nodes=[TextNode(text,TextType.TEXT)]
    step_bold=split_nodes_delimiter(old_nodes,"**",TextType.BOLD)
    step_italic=split_nodes_delimiter(step_bold,"_",TextType.ITALIC)
    step_code=split_nodes_delimiter(step_italic,"`",TextType.CODE)
    step_image=split_nodes_image(step_code)
    step_link=split_nodes_link(step_image)
    return step_link

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("invalid text type")
    else:
        if text_node.text_type==TextType.TEXT:
            return LeafNode(None,text_node.text)
        elif text_node.text_type==TextType.BOLD:
            return LeafNode("b",text_node.text)
        elif text_node.text_type==TextType.ITALIC:
            return LeafNode("i",text_node.text)
        elif text_node.text_type==TextType.CODE:
            return LeafNode("code",text_node.text)
        elif text_node.text_type==TextType.LINK:
            return LeafNode("a",text_node.text,{"href":text_node.url})
        elif text_node.text_type==TextType.IMAGE:
            return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})

main()