import unittest
from textnode import TextNode, TextType
from split_node_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_text_with_single_delimiter(self):
        node = TextNode("Here is `inline code` example", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("inline code", TextType.CODE),
            TextNode(" example", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_text_with_multiple_delimiters(self):
        node = TextNode("This is **bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_text_with_unmatched_delimiter(self):
        node = TextNode("Here is `broken code", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_text_type_preserved(self):
        node = TextNode("This should stay bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])

    def test_mixed_text_and_non_text_nodes(self):
        nodes = [
            TextNode("Normal text with `code block` inside", TextType.TEXT),
            TextNode("This should remain bold", TextType.BOLD),
            TextNode("Another _italic_ example", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        expected = [
            TextNode("Normal text with ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" inside", TextType.TEXT),
            TextNode("This should remain bold", TextType.BOLD),
            TextNode("Another ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" example", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()
