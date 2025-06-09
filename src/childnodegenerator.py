from textconverter import text_to_textnodes
from textnodeconverter import text_node_to_html_node

def text_to_children(text):
    TextNodes=text_to_textnodes(text)
    HTMLNodes=[]
    for node in TextNodes:
        HTMLNodes.append(text_node_to_html_node(node))
    return HTMLNodes
