from textnode import TextNode,TextType
from nodesplitter import split_nodes_delimiter,split_nodes_image,split_nodes_link

def text_to_textnodes(text):
    old_nodes=[TextNode(text,TextType.TEXT)]
    step_bold=split_nodes_delimiter(old_nodes,"**",TextType.BOLD)
    step_italic=split_nodes_delimiter(step_bold,"_",TextType.ITALIC)
    step_code=split_nodes_delimiter(step_italic,"`",TextType.CODE)
    step_image=split_nodes_image(step_code)
    step_link=split_nodes_link(step_image)
    return step_link