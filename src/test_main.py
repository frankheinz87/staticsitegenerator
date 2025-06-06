import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,TextType
from main import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node_Bold = TextNode("This is a bold text node", TextType.BOLD)
        node_Italic = TextNode("This is an italic text node", TextType.ITALIC)
        node_Code = TextNode("This is a code text node", TextType.CODE)
        node_Link= TextNode("This is a link text node", TextType.LINK,"https://www.boot.dev")
        node_Image= TextNode("This is an image text node", TextType.IMAGE,"https://www.boot.dev")
        node_Error= TextNode("This is an error text node", "Fancy")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(text_node_to_html_node(node),LeafNode(None,"This is a text node"))
        self.assertEqual(text_node_to_html_node(node_Bold),LeafNode("b","This is a bold text node"))
        self.assertEqual(text_node_to_html_node(node_Italic),LeafNode("i","This is an italic text node"))
        self.assertEqual(text_node_to_html_node(node_Code),LeafNode("code","This is a code text node"))
        self.assertEqual(text_node_to_html_node(node_Link),LeafNode("a","This is a link text node",{"href":"https://www.boot.dev"}))
        self.assertEqual(text_node_to_html_node(node_Image),LeafNode("img","",{"src":"https://www.boot.dev","alt":"This is an image text node"}))
        with self.assertRaises(Exception):
            text_node_to_html_node(node_Error)


if __name__ == "__main__":
    unittest.main()