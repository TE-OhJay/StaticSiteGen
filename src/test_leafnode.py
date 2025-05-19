import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_no_tag(self):
        node = LeafNode("Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_with_tag(self):
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("Click here", "a", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

    def test_leaf_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode(None, "p").to_html()

    def test_leaf_repr(self):
        node = LeafNode("Hello, world!", "p", {"class": "greeting"})
        self.assertEqual(repr(node), 'LeafNode(tag = p, value = Hello, world!, props = {\'class\': \'greeting\'})')

if __name__ == "__main__":
    unittest.main()
