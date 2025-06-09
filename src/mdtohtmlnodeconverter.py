from blockgenerator import markdown_to_blocks
from blockconverter import block_to_block_type
from childnodegenerator import text_to_children
from textnodeconverter import text_node_to_html_node
from blocktypetotagconverter import block_type_to_tag
from markdownblock import BlockType
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,TextType

def markdown_to_html_node(markdown):
    blocks=markdown_to_blocks(markdown)
    HTMLNodes=[]
    for block in blocks:
        block_type=block_to_block_type(block)
        if block_type[0]==BlockType.CODE:
            lines=block.splitlines()
            new_lines = [line for line in lines if line.strip() != "```"]
            final_lines="\n".join(new_lines)+"\n"
            Code=TextNode(final_lines, TextType.CODE)
            HTMLNodes.append(ParentNode(block_type_to_tag(block_type),[text_node_to_html_node(Code)]))
        elif block_type[0]==BlockType.PARAGRAPH:
            new_block=block.replace("\n"," ")
            HTMLNodes.append(ParentNode(block_type_to_tag(block_type),text_to_children(new_block)))
        else:
            HTMLNodes.append(ParentNode(block_type_to_tag(block_type),text_to_children(block)))
    return ParentNode("div",HTMLNodes)