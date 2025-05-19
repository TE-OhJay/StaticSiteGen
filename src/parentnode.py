from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, children = children, props = props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("All parents need a tag")
        if self.children == None:
            raise ValueError("All parents have children")
        else:
            return f"<{self.tag}{self.props_to_html() if self.props else ''}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
        
    def __repr__(self):
        return f"ParentNode(tag = {self.tag}, children = {self.children}, props = {self.props})"