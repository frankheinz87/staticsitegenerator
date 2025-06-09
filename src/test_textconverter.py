import unittest

from textnode import TextNode,TextType
from textconverter import text_to_textnodes

class TestTextNode(unittest.TestCase):
    def test_text_to_testnode(self):
        text="This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [
                                                    TextNode("This is ", TextType.TEXT),
                                                    TextNode("text", TextType.BOLD),
                                                    TextNode(" with an ", TextType.TEXT),
                                                    TextNode("italic", TextType.ITALIC),
                                                    TextNode(" word and a ", TextType.TEXT),
                                                    TextNode("code block", TextType.CODE),
                                                    TextNode(" and an ", TextType.TEXT),
                                                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                                    TextNode(" and a ", TextType.TEXT),
                                                    TextNode("link", TextType.LINK, "https://boot.dev"),
                                                    ])

if __name__ == "__main__":
    unittest.main()
        