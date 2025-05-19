import unittest
from textnode import TextNode, TextType, text_node_to_html
from leafnode import LeafNode

class TestTextToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_node_text(self):
        node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.to_html(), "Hello, world!")

    def test_text_node_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_text_node_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_text_node_code(self):
        node = TextNode("print('Hello')", TextType.CODE)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.to_html(), "<code>print('Hello')</code>")

    def test_text_node_link(self):
        node = TextNode("Visit here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.to_html(), '<a href="https://example.com">Visit here</a>')

    def test_text_node_image(self):
        node = TextNode("An image", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.to_html(), '<img src="https://example.com/image.jpg" alt="An image"></img>')

    def test_text_node_invalid_type(self):
        node = TextNode("Invalid", "not_a_real_type")
        with self.assertRaises(Exception):
            text_node_to_html(node)


if __name__ == "__main__":
    unittest.main()
