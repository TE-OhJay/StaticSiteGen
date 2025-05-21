import unittest
from textnode import TextNode, TextType
from markdown_extraction import split_nodes_image, split_nodes_link  


class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_image(self):
        node = TextNode(
            "Here is an image ![cat](https://example.com/cat.jpg) and another ![dog](https://example.com/dog.jpg)",
            TextType.TEXT,
        )
        expected = [
            TextNode("Here is an image ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "https://example.com/cat.jpg"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("dog", TextType.IMAGE, "https://example.com/dog.jpg"),
        ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_no_links(self):
        node = TextNode("No links here!", TextType.TEXT)
        expected = [node]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_no_images(self):
        node = TextNode("Just normal text", TextType.TEXT)
        expected = [node]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_mixed_content(self):
        node = TextNode(
            "Check this link [Google](https://google.com) and this image ![logo](https://example.com/logo.png)",
            TextType.TEXT,
        )
        expected_links = [
            TextNode("Check this link ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" and this image ![logo](https://example.com/logo.png)", TextType.TEXT),
        ]
        expected_images = [
            TextNode("Check this link [Google](https://google.com) and this image ", TextType.TEXT),
            TextNode("logo", TextType.IMAGE, "https://example.com/logo.png"),
        ]
        self.assertEqual(split_nodes_link([node]), expected_links)
        self.assertEqual(split_nodes_image([node]), expected_images)

if __name__ == "__main__":
    unittest.main()