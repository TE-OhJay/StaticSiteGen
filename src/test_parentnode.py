import unittest
from parentnode import ParentNode
from leafnode import LeafNode



class TestParentNode(unittest.TestCase):

    def test_to_html_with_single_child(self):
        child_node = LeafNode("child text", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child text</span></div>")

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("First", "p")
        child2 = LeafNode("Second", "p")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><p>First</p><p>Second</p></div>")

    def test_to_html_with_nested_parent(self):
        grandchild = LeafNode("Bold text", "b")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span><b>Bold text</b></span></div>")
        
    def test_to_html_multiple_nested_parents(self):
        grandchild = LeafNode("Deep content", "em")
        child1 = ParentNode("section", [grandchild])
        child2 = ParentNode("article", [child1])
        parent = ParentNode("div", [child2])

        self.assertEqual(
            parent.to_html(),
            "<div><article><section><em>Deep content</em></section></article></div>"
        )


    def test_to_html_with_props(self):
        child = LeafNode("Click here", "a", {"href": "https://example.com"})
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><a href="https://example.com">Click here</a></div>')

    def test_to_html_no_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_to_html_no_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("text", "p")]).to_html()

    def test_repr(self):
        child = LeafNode("Hello", "span")
        parent = ParentNode("div", [child], {"id": "main"})
        self.assertEqual(repr(parent), "ParentNode(tag = div, children = [LeafNode(tag = span, value = Hello, props = None)], props = {'id': 'main'})")

if __name__ == "__main__":
    unittest.main()
