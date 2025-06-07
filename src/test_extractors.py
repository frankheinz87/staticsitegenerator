import unittest

from extractors import extract_markdown_images,extract_markdown_links

class TestTextNode(unittest.TestCase):
    def test_text(self):
        text_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_images(text_image),[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        self.assertEqual(extract_markdown_links(text_link),[("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
        self.assertEqual(extract_markdown_links(text_image),[])
        self.assertEqual(extract_markdown_images(text_link),[])



if __name__ == "__main__":
    unittest.main()