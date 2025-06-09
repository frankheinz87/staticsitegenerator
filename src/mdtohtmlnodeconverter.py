from blockgenerator import markdown_to_blocks
from blockconverter import block_to_block_type
from childnodegenerator import text_to_children
from textnodeconverter import text_node_to_html_node
from markdownblock import BlockType
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,TextType

def markdown_to_html_node(markdown):
    blocks=markdown_to_blocks(markdown)
    HTMLNodes=[]
    for block in blocks:
        block_type=block_to_block_type(block)
        if block_type==BlockType.CODE:
            Code=TextNode(block, TextType.CODE)
            HTMLNodes.append(ParentNode(block_type,text_node_to_html_node(Code)))
        else:
            HTMLNodes.append(ParentNode(block_type,text_to_children(block)))
    return ParentNode("div",HTMLNodes)