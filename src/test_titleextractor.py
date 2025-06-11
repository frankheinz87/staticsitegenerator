import unittest

from titleextractor import extract_title

class TestTextNode(unittest.TestCase):
    def test_exract_title(self):
        md = """
        # This is a level 1 heading
        ## This is a Level 2 heading
        ### This is a Level 3 heading
        """
        title=extract_title(md)
        self.assertEqual(
            title,
            "This is a level 1 heading"
        )
    
    def test_exract_title_exception(self):
        md = """
        
        ## This is a Level 2 heading
        ### This is a Level 3 heading
        """
        
        with self.assertRaises(Exception):
            extract_title(md)
        
                                                    

if __name__ == "__main__":
    unittest.main()