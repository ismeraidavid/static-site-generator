from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type: TextType):
    """
    Example: TextNode("This is text with a **bolded phrase** in the middle", "**")

    Expected output:

    [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bolded phrase", TextType.BOLD),
    TextNode(" in the middle", TextType.TEXT),
    ]

    """
    new_nodes = []

    for (
        old_node
    ) in (
        old_nodes
    ):  # old_nodes is a list of TextNodes, we need to check for every one of them
        if old_node.text_type != TextType.TEXT:  # We only want to split text nodes
            new_nodes.append(old_node)
            continue  # Next iteration

        # Now we split the text of each node using the delimiter provided. To obtain a list of words
        splitted_old_node = old_node.text.split(delimiter)

        # If the split list has an even number of words, it means the delimiter wasn't closed correctly
        # If the format is correct, we will always have an odd number of words
        if len(splitted_old_node) % 2 == 0:
            raise ValueError("Invalid Markdown syntax, formatted section not closed")

        for (
            word
        ) in (
            splitted_old_node
        ):  # If the last or first character of a word is a space, then these are not the words inside the delimiter
            if (word[0] == " ") or (word[-1] == " "):
                new_nodes.append(TextNode(word, TextType.TEXT, None))
            else:
                new_nodes.append(TextNode(word, text_type, None))

    return new_nodes
