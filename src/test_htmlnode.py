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
        node1=LeafNode("a","Hello",{"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode(None, "Hello, world!")
        node3 = LeafNode("p", None)
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com" target="_blank">Hello</a>')
        self.assertEqual(node2.to_html(), "Hello, world!")
        with self.assertRaises(ValueError):
            node3.to_html()

        

if __name__ == "__main__":
    unittest.main()