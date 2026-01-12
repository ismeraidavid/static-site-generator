import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "p", "This is test text", None, {"href": "https://www.test.com"}
        )

        self.assertTrue(node.props_to_html() == ' href="https://www.test.com"')

    def test_empty_props(self):
        node = HTMLNode()
        node2 = HTMLNode("p", "This is test text", [node], None)

        self.assertTrue(node2.props_to_html() == "")

    def test_multiple_props(self):

        node3 = HTMLNode(
            "p",
            "This is test text",
            None,
            {"href": "https://www.test.com", "target": "_blank"},
        )

        self.assertTrue(
            node3.props_to_html() == ' href="https://www.test.com" target="_blank"'
        )


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "This is some test text")

        self.assertTrue(node.to_html() == "<p>This is some test text</p>")

    def test_no_value_error(self):
        node = LeafNode("a", None, None)

        self.assertRaises(ValueError)

    def test_no_tag(self):
        node = LeafNode(None, "This is some test text", None)

        self.assertTrue(node.to_html() == "This is some test text")

    def test_leaf_to_html_props(self):
        node = LeafNode(
            "a", "This is a link", {"href": "https://www.test.com", "target": "_blank"}
        )

        self.assertTrue(
            node.to_html()
            == '<a href="https://www.test.com" target="_blank">This is a link</a>'
        )


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child = LeafNode("b", "this is the child", None)
        parent = ParentNode("p", [child], None)

        self.assertEqual(parent.to_html(), "<p><b>this is the child</b></p>")

    def test_to_html_with_many_children(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            None,
        )

        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("i", "this is the grandchild", None)
        child = ParentNode("b", [grandchild], None)
        parent = ParentNode("p", [child], None)

        self.assertEqual(
            parent.to_html(), "<p><b><i>this is the grandchild</i></b></p>"
        )

    def test_to_html_with_props(self):
        child = LeafNode("a", "this is a link", {"href": "https://www.test.com"})
        parent = ParentNode("div", [child], {"class": "my-class"})

        self.assertEqual(
            parent.to_html(),
            '<div class="my-class"><a href="https://www.test.com">this is a link</a></div>',
        )

    def test_to_html_no_tag(self):
        child = LeafNode("b", "this is a child", None)
        parent = ParentNode(None, [child], None)

        self.assertRaises(ValueError)

    def test_to_htm_no_children(self):
        child = LeafNode("b", "this is a child", None)
        parent = ParentNode("div", None, None)

        self.assertRaises(ValueError)


if __name__ == "__main__":
    unittest.main()
