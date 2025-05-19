import unittest
from markdown_extraction import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):

    def test_extract_single_image(self):
        text = "Here is an image ![Alt Text](https://example.com/image.jpg)"
        self.assertEqual(extract_markdown_images(text), [("Alt Text", "https://example.com/image.jpg")])

    def test_extract_multiple_images(self):
        text = "![First Image](https://example.com/first.jpg) and ![Second](https://example.com/second.jpg)"
        expected = [("First Image", "https://example.com/first.jpg"), ("Second", "https://example.com/second.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_image_with_no_alt_text(self):
        text = "![](https://example.com/image.jpg)"
        self.assertEqual(extract_markdown_images(text), [])  # This regex doesn't match empty alt text

    def test_extract_image_with_special_chars_in_alt(self):
        text = "![Image *bold* text](https://example.com/image.jpg)"
        self.assertEqual(extract_markdown_images(text), [("Image *bold* text", "https://example.com/image.jpg")])

    def test_extract_single_link(self):
        text = "Click [here](https://example.com)"
        self.assertEqual(extract_markdown_links(text), [("here", "https://example.com")])

    def test_extract_multiple_links(self):
        text = "[Google](https://google.com) and [Bing](https://bing.com)"
        expected = [("Google", "https://google.com"), ("Bing", "https://bing.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_link_with_special_chars(self):
        text = "[Bold Link **text**](https://example.com)"
        self.assertEqual(extract_markdown_links(text), [("Bold Link **text**", "https://example.com")])

#    def test_extract_link_with_nested_parentheses(self):
#        text = "[Example](https://example.com/path?query=(nested))"
#        self.assertEqual(extract_markdown_links(text), [("Example", "https://example.com/path?query=(nested)")])

    def test_ignore_image_links_in_link_extraction(self):
        text = "[Normal Link](https://example.com) and ![Image](https://example.com/image.jpg)"
        self.assertEqual(extract_markdown_links(text), [("Normal Link", "https://example.com")])

    def test_extract_nothing_from_plain_text(self):
        text = "This is just plain text with no links or images."
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])

if __name__ == "__main__":
    unittest.main()