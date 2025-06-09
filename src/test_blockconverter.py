import unittest

from blockconverter import block_to_block_type
from markdownblock import BlockType

class TestBlockConv(unittest.TestCase):
    def test_block_to_block_type(self):
        heading1="# Heading"
        heading2="## Heading"
        heading3="### Heading"
        heading4="#### Heading"
        heading5="##### Heading"
        heading6="###### Heading"

        code="```code block```"

        true_quote=">start of quote\n>middle of quote\n>end of quote"
        false_quote=">start of quote\nmiddle of quote\n>end of quote"

        true_unordered_list="- first list item\n- second list item\n- third list item"
        false_unordered_list="- first list item\nsecond list item\n third list item"

        true_ordered_list="1. first list item\n2. second list item\n3. third list item"
        false_ordered_list="2. first list item\n1.second list item\n3 third list item"

        self.assertEqual(block_to_block_type(heading1),[BlockType.HEADING,1])
        self.assertEqual(block_to_block_type(heading2),[BlockType.HEADING,2])
        self.assertEqual(block_to_block_type(heading3),[BlockType.HEADING,3])
        self.assertEqual(block_to_block_type(heading4),[BlockType.HEADING,4])
        self.assertEqual(block_to_block_type(heading5),[BlockType.HEADING,5])
        self.assertEqual(block_to_block_type(heading6),[BlockType.HEADING,6])

        self.assertEqual(block_to_block_type(code),[BlockType.CODE])

        self.assertEqual(block_to_block_type(true_quote),[BlockType.QUOTE])
        self.assertEqual(block_to_block_type(false_quote),[BlockType.PARAGRAPH])

        self.assertEqual(block_to_block_type(true_unordered_list),[BlockType.UNORDERED_LIST])
        self.assertEqual(block_to_block_type(false_unordered_list),[BlockType.PARAGRAPH])

        self.assertEqual(block_to_block_type(true_ordered_list),[BlockType.ORDERED_LIST])
        self.assertEqual(block_to_block_type(false_ordered_list),[BlockType.PARAGRAPH])



if __name__ == "__main__":
    unittest.main()