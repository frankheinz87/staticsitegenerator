import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,TextType
from nodesplitter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = "This is text with a **bolded phrase** in the middle"
        node1 = "This is text with a first **bolded phrase** and a second ** phrase** including an ending"
        print(split_nodes_delimiter([node],"**",TextType.BOLD))
        print(split_nodes_delimiter([node1],"**",TextType.BOLD))
        


if __name__ == "__main__":
    unittest.main()