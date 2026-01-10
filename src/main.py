from textnode import TextNode, TextType


def main():
    testnode = TextNode(
        "This is some text to try", TextType.BOLD_TEXT.value, "https://www.test.com"
    )
    print(testnode)


if __name__ == "__main__":
    main()
