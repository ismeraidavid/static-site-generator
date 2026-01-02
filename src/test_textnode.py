import unittest

from textnode import TextNode, TextType


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
        node = TextNode("Rasengan es lo mejor", TextType.IMAGES)
        node2 = TextNode("Chidori es lo mejor", TextType.IMAGES)

        self.assertNotEqual(node, node2)

    def test_noteq_texttype_no_url(self):
        node = TextNode("Rasengan es lo mejor", TextType.IMAGES)
        node2 = TextNode("Rasengan es lo mejor", TextType.LINKS)

        self.assertNotEqual(node, node2)

    def test_noteq_urls(self):
        node = TextNode("Rasengan es lo mejor", TextType.IMAGES, "www.inventado.com")
        node2 = TextNode("Rasengan es lo mejor", TextType.IMAGES, "www.inventado2.com")

        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("Rasengan es lo mejor", TextType.IMAGES, None)
        node2 = TextNode("Rasengan es lo mejor", TextType.IMAGES)

        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
