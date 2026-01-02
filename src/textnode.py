from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINKS = "links"
    IMAGES = "images"


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
