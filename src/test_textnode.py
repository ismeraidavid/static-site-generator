import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(
            "Itachi es en verdad el creador de la serie", TextType.BOLD_TEXT
        )
        node2 = TextNode(
            "Itachi es en verdad el creador de la serie", TextType.BOLD_TEXT
        )

        self.assertEqual(node, node2)

    def test_noteq_text_no_url(self):
        node = TextNode("Rasengan es lo mejor", TextType.IMAGE)
        node2 = TextNode("Chidori es lo mejor", TextType.IMAGE)

        self.assertNotEqual(node, node2)

    def test_noteq_texttype_no_url(self):
        node = TextNode("Rasengan es lo mejor", TextType.IMAGE)
        node2 = TextNode("Rasengan es lo mejor", TextType.LINK)

        self.assertNotEqual(node, node2)

    def test_noteq_urls(self):
        node = TextNode("Rasengan es lo mejor", TextType.IMAGE, "www.inventado.com")
        node2 = TextNode("Rasengan es lo mejor", TextType.IMAGE, "www.inventado2.com")

        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("Rasengan es lo mejor", TextType.IMAGE, None)
        node2 = TextNode("Rasengan es lo mejor", TextType.IMAGE)

        self.assertEqual(node, node2)


class TestTextNodeToHTML(unittest.TestCase):
    # def test_invalid_text_type(self):
    #     text_node = TextNode("This is an unordered", "unordered_list", None)

    #     with self.assertRaises(AttributeError):
    #         text_node_to_html_node(text_node)

    def test_bold(self):
        node = TextNode("bold", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold")

    def test_code(self):
        node = TextNode("code", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "code")

    def test_image(self):
        node = TextNode("image", TextType.IMAGE, url="https://www.test.com")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "https://www.test.com", "alt": "image"}
        )

    def test_italic(self):
        node = TextNode("italic", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic")

    def test_link(self):
        node = TextNode("link", TextType.LINK, url="https://www.test.com")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link")
        self.assertEqual(html_node.props, {"href": "https://www.test.com"})

    def test_text(self):
        node = TextNode("text", TextType.TEXT)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "text")


if __name__ == "__main__":
    unittest.main()
