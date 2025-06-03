import unittest

from htmlnode import HTMLNode,LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node=HTMLNode()
        node1=HTMLNode("p","Hello")
        node2=HTMLNode("p","Hello")
        node3=HTMLNode("p","Hello",[node],{"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node,node1)
        self.assertEqual(node1,node2)
        self.assertNotEqual(node2,node3)

    def test_props_to_html(self):
        node3=HTMLNode("p","Hello",[],{"href": "https://www.google.com", "target": "_blank"})
        print(node3.props_to_html())
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        

if __name__ == "__main__":
    unittest.main()