import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_typeError_without_textType(self):
        with self.assertRaises(TypeError):
            TextNode("This is a text node")
            
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node), "TextNode('This is a text node', <TextType.BOLD: 'bold'>, None)")
        
    def test_not_eq_when_TextType_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_when_url_different(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://linux.die.net")
        self.assertNotEqual(node, node2)
    
    def test_not_eq_when_url_None(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()