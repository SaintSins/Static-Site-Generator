class HTMLNode:

    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Nothing is implemented in child classes.")
    
    def props_to_html(self):
        if not self.props:
            return ""
        empty_str = ""
        for key,value in self.props.items():
            empty_str += f' {key}="{value}"'
        return empty_str
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):

    def __init__(self, value, tag = None, props = None):
        super().__init__(tag = tag, value = value, children = None, props = props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

    