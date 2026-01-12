import unittest

from utils import extract_markdown_links, extract_markdown_images


class TestExtractFromMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is a text with an URL ![alt text](https://www.test.com/test.jpeg) and an image ![image alt text](https://www.images.test.com/image.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("alt text", "https://www.test.com/test.jpeg"),
                ("image alt text", "https://www.images.test.com/image.png"),
            ],
            matches,
        )

    def test_no_images(self):
        text = "This is just text without any images"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_links(self):
        text = "This is text with a link [to a web](https://www.test.com) and [to youtube](https://www.youtube.com/@test)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to a web", "https://www.test.com"),
                ("to youtube", "https://www.youtube.com/@test"),
            ],
            matches,
        )

        def test_no_links(self):
            text = "This is just text without any images"
            self.assertEqual(extract_markdown_links(text), [])
