import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node=HTMLNode()
        node1=HTMLNode("p","Hello")
        node2=HTMLNode("p","Hello")
        node3=HTMLNode("p","Hello",[node],{"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node,node1)
        self.assertEqual(node1,node2)
        self.assertNotEqual(node2,node3)
        print(node3.props_to_html())

        

if __name__ == "__main__":
    unittest.main()