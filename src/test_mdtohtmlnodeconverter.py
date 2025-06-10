import unittest
from mdtohtmlnodeconverter import markdown_to_html_node

class TestMDConverter(unittest.TestCase):
    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_heading(self):
        md = """
        ### This is a Level 3 heading
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a Level 3 heading</h3></div>",
        )

    def test_unordered_list(self):
        md = """
        - first item
        - second item
        - third item
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>first item</li><li>second item</li><li>third item</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
        1. first item
        2. second item
        3. third item
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first item</li><li>second item</li><li>third item</li></ol></div>",
        )

    def test_blockquote(self):
        md = """
        > This is a
        > blockquote block

        > this is another
        > blockquote block
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><blockquote>this is another blockquote block</blockquote></div>",
        )

if __name__ == "__main__":
    unittest.main()