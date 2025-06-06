import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,TextType
from nodesplitter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node_Bold = TextNode("This is text with a **bolded phrase** in the middle",TextType.TEXT)
        node_Bold2 = TextNode("This is text with a first **bolded phrase** and a second **bolded phrase** including an ending",TextType.TEXT)
        node_Italic = TextNode("This is text with an *italic phrase* in the middle",TextType.TEXT)
        node_Code = TextNode("This is text with a `code block` in the middle",TextType.TEXT)
        node_Bold_Start = TextNode("**Bolded phrase** at the beginning",TextType.TEXT)
        node_Bold_End = TextNode("in the end a **bolded phrase**",TextType.TEXT)
        node_Bold_Start_End =TextNode("**Bolded phrase** at the beginning and in the end **bolded phrase**",TextType.TEXT)
        node_Bold_Exception =TextNode("in the end a **bolded phrase",TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node_Bold],"**",TextType.BOLD),[
                                                                                TextNode("This is text with a ", TextType.TEXT),
                                                                                TextNode("bolded phrase", TextType.BOLD),
                                                                                TextNode(" in the middle", TextType.TEXT),
                                                                                ])
        self.assertEqual(split_nodes_delimiter([node_Bold2],"**",TextType.BOLD),[
                                                                                TextNode("This is text with a first ", TextType.TEXT),
                                                                                TextNode("bolded phrase", TextType.BOLD),
                                                                                TextNode(" and a second ", TextType.TEXT),
                                                                                TextNode("bolded phrase", TextType.BOLD),
                                                                                TextNode(" including an ending", TextType.TEXT)
                                                                                ])
        self.assertEqual(split_nodes_delimiter([node_Italic],"*",TextType.ITALIC),[
                                                                                TextNode("This is text with an ", TextType.TEXT),
                                                                                TextNode("italic phrase", TextType.ITALIC),
                                                                                TextNode(" in the middle", TextType.TEXT),
                                                                                ])
        self.assertEqual(split_nodes_delimiter([node_Code],"`",TextType.CODE),[
                                                                                TextNode("This is text with a ", TextType.TEXT),
                                                                                TextNode("code block", TextType.CODE),
                                                                                TextNode(" in the middle", TextType.TEXT),
                                                                                ])
        self.assertEqual(split_nodes_delimiter([node_Bold_Start],"**",TextType.BOLD),[
                                                                                TextNode("Bolded phrase", TextType.BOLD),
                                                                                TextNode(" at the beginning", TextType.TEXT),
                                                                                ])
        self.assertEqual(split_nodes_delimiter([node_Bold_End],"**",TextType.BOLD),[
                                                                                TextNode("in the end a ", TextType.TEXT),
                                                                                TextNode("bolded phrase", TextType.BOLD),
                                                                                ])
        self.assertEqual(split_nodes_delimiter([node_Bold_Start_End],"**",TextType.BOLD),[
                                                                                TextNode("Bolded phrase", TextType.BOLD),
                                                                                TextNode(" at the beginning and in the end ", TextType.TEXT),
                                                                                TextNode("bolded phrase", TextType.BOLD),
                                                                                ])
        self.assertEqual(split_nodes_delimiter([node_Bold_Start,node_Bold_End],"**",TextType.BOLD),[
                                                                                TextNode("Bolded phrase", TextType.BOLD),
                                                                                TextNode(" at the beginning", TextType.TEXT),
                                                                                TextNode("in the end a ", TextType.TEXT),
                                                                                TextNode("bolded phrase", TextType.BOLD),
                                                                                ])
        print(split_nodes_delimiter([node_Bold_Start,node_Bold_End],"**",TextType.BOLD))
        with self.assertRaises(Exception):
            split_nodes_delimiter([node_Bold_Exception],"**",TextType.BOLD)
        


if __name__ == "__main__":
    unittest.main()