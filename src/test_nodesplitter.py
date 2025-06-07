import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,TextType
from nodesplitter import split_nodes_delimiter,split_nodes_image,split_nodes_link

class TestTextNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
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
        
        with self.assertRaises(Exception):
            split_nodes_delimiter([node_Bold_Exception],"**",TextType.BOLD)

    

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node1 = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and an ending",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        new_nodes1 = split_nodes_image([node1])
        new_nodes2 = split_nodes_image([node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes1,
        )

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and an ending", TextType.TEXT)
            ],
            new_nodes2,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        node1 = TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and an ending",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        new_nodes1 = split_nodes_link([node1])
        new_nodes2 = split_nodes_link([node2])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
        self.assertListEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes1,
        )
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
                TextNode(" and an ending", TextType.TEXT),
            ],
            new_nodes2,
        )


if __name__ == "__main__":
    unittest.main()