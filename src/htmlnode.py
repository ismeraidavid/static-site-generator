class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list["HTMLNode"] = None,
        props: dict[str, str] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """Child classes must override this method to render themselves as HTML"""
        raise NotImplementedError("method to_html is not yet implemented")

    def props_to_html(self):
        """Return a formatted string representing the HTML attributes of the node"""

        if not self.props:
            return ""

        formatted_string = ""
        for prop, value in self.props.items():
            formatted_string += f' {prop}="{value}"'

        return formatted_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    """A LeafNode is a type of HTMLNode that represents a single HTML tag with no children"""

    def __init__(self, tag: str, value: str, props: dict[str, str] = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")

        # If there is no tag (e.g. it's None), the value should be returned as raw text
        if not self.tag:
            return self.value

        # If there is a value and a tag, we render an HTML tag

        formatted_string = (
            f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        )

        return formatted_string


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list["HTMLNode"], props: dict[str, str] = None
    ):
        super().__init__(tag=tag, children=children, props=props, value=None)

    def to_html(self):

        if not self.tag:
            raise ValueError("All parent nodes must have a tag")

        if not self.children:
            raise ValueError("All parent nodes must have childrens")

        childs_formatted_string = ""
        for child in self.children:
            childs_formatted_string += child.to_html()

        return (
            f"<{self.tag}{self.props_to_html()}>{childs_formatted_string}</{self.tag}>"
        )

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
