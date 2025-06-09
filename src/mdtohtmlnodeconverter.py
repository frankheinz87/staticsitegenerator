from blockgenerator import markdown_to_blocks
from blockconverter import block_to_block_type
from childnodegenerator import text_to_children
from textnodeconverter import text_node_to_html_node
from blocktypetotagconverter import block_type_to_tag
from markdownblock import BlockType
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,TextType

import re

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
        elif block_type[0]==BlockType.HEADING:
            HTMLNodes.append(ParentNode(block_type_to_tag(block_type),text_to_children(block.lstrip("#").strip())))
        elif block_type[0] == BlockType.UNORDERED_LIST:
            # Split into individual list items
            lines = block.split('\n')
            list_items = []
            for line in lines:
                # Remove the "- " prefix and create <li> node
                item_text = line.lstrip('- ').strip()
                li_node = ParentNode("li", text_to_children(item_text))
                list_items.append(li_node)
            
            HTMLNodes.append(ParentNode(block_type_to_tag(block_type), list_items))
        elif block_type[0] == BlockType.ORDERED_LIST:
            # Split into individual list items
            lines = block.split('\n')
            list_items = []
            for line in lines:
                # Remove pattern like "1. " or "23. " from the start
                item_text = re.sub(r'^\d+\.\s*', '', line)
                li_node = ParentNode("li", text_to_children(item_text))
                list_items.append(li_node)
            
            HTMLNodes.append(ParentNode(block_type_to_tag(block_type), list_items))
        elif block_type[0]==BlockType.QUOTE:
            lines = block.split("\n")
            quote_text=" ".join(line.lstrip("> ") for line in lines)
            HTMLNodes.append(ParentNode(block_type_to_tag(block_type), text_to_children(quote_text)))
        else:
            HTMLNodes.append(ParentNode(block_type_to_tag(block_type),text_to_children(block)))
    return ParentNode("div",HTMLNodes)