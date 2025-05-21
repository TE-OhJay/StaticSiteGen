import unittest
from textnode import TextNode, TextType
from markdown_extraction import text_to_textnode  

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnode(text), expected)

    def test_no_special_formatting(self):
        text = "Just some plain text"
        expected = [TextNode("Just some plain text", TextType.TEXT)]
        self.assertEqual(text_to_textnode(text), expected)

    def test_bold_only(self):
        text = "This is **bold** text"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnode(text), expected)

    def test_italic_only(self):
        text = "An _italic_ word"
        expected = [
            TextNode("An ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnode(text), expected)

    def test_code_only(self):
        text = "Some `code` snippet"
        expected = [
            TextNode("Some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" snippet", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnode(text), expected)

    def test_image_only(self):
        text = "An image ![test](https://example.com/image.jpg)"
        expected = [
            TextNode("An image ", TextType.TEXT),
            TextNode("test", TextType.IMAGE, "https://example.com/image.jpg"),
        ]
        self.assertEqual(text_to_textnode(text), expected)

    def test_link_only(self):
        text = "Visit [Google](https://google.com)"
        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
        ]
        self.assertEqual(text_to_textnode(text), expected)

if __name__ == "__main__":
    unittest.main()