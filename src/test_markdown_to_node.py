from markdown_to_node import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest


class TestMarkdownToNode(unittest.TestCase):
    def test_bold(self):
        node1 = TextNode("This is text with a **bold** words", TextType.TEXT)
        new_nodes1 = split_nodes_delimiter([node1], "**", TextType.BOLD_TEXT)

        node2 = TextNode(
            "This is text with a **multiple** words in **bold** style",
            TextType.TEXT,
        )
        new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD_TEXT)

        self.assertEqual(
            new_nodes1,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" words", TextType.TEXT),
            ],
        )

        self.assertEqual(
            new_nodes2,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("multiple", TextType.BOLD_TEXT),
                TextNode(" words in ", TextType.TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" style", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
