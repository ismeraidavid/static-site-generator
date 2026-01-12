import re


def extract_markdown_images(text):
    """
    Takes raw markdown text an returns a list of tuples. Each tuple contains
    the alt text and the URL of any markdown images.

    Example:

    text = "This is a text with an URL ![alt text](https://www.test.com/test.jpeg) and an image ![image alt text](https://www.images.test.com/image.png)
    print(extract_markdown_images(text))
    [("alt text", "https://www.test.com/test.jpeg"), ("image alt text", "https://www.images.test.com/image.png")]
    """

    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches


def extract_markdown_links(text):
    """
    Takes raw markdown text an returns a list of tuples. Each tuple contains the anchor text and the URL in the link.

    Example:

    text = "This is text with a link [to a web](https://www.test.com) and [to youtube](https://www.youtube.com/@test)"
    print(extract_markdown_links(text))
    [("to a web", "https://www.test.com"), ("to youtube", "https://www.youtube.com/@test")]
    """

    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches
