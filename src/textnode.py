from enum import Enum
from htmlnode import LeafNode, ParentNode


class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                (self.text == other.text)
                and (self.text_type == other.text_type)
                and (self.url == other.url)
            )
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type not in TextType:
        raise AttributeError("Invalid text type for the text node")

    if text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", text_node.text, None)

    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text, None)

    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(
            "img", value="", props={"src": text_node.url, "alt": text_node.text}
        )

    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", text_node.text, None)

    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, props={"href": text_node.url})

    else:
        return LeafNode(tag=None, value=text_node.text)
