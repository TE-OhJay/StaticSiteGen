from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props = None):
        super().__init__(tag = tag, value = value, props = props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html() if self.props else ''}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode(tag = {self.tag}, value = {self.value}, props = {self.props})"