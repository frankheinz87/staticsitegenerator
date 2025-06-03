import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.CODE)
        node5 = TextNode("This is a different text node", TextType.BOLD)
        node6 = TextNode("This is a text node", TextType.BOLD,url=None)
        node7 = TextNode("This is a text node", TextType.BOLD,url="www.boot.dev")
        self.assertEqual(node, node2) #same same
        self.assertNotEqual(node,node3) #text_type different
        self.assertNotEqual(node,node4) #text_type different
        self.assertNotEqual(node,node5) #text different
        self.assertEqual(node, node6) #url present but None
        self.assertNotEqual(node, node7) #url present


if __name__ == "__main__":
    unittest.main()