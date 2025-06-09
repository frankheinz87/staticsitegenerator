from textnode import TextNode,TextType
from htmlnode import HTMLNode,ParentNode,LeafNode

def main():
    Hello=TextNode("Hello World", TextType.LINK, "https://www.boot.dev" )
    Hello2=HTMLNode("p","Hello",[],{"href": "https://www.google.com", "target": "_blank"})

main()