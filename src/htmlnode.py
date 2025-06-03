class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result=None
        if self.props==None:
            result=""
        else:
            result=""
            for item in self.props:
                result+=" "+item+"="+'"'+self.props[item]+'"'
        return result
    
    def __eq__(self, other):
        return (self.tag==other.tag and self.value==other.value and self.children==other.children and self.props==other.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value==None:
            raise ValueError
        elif self.tag==None:
            return self.value
        else:
            if self.props==None:
                return '<'+self.tag.lstrip('"').rstrip('"')+">"+self.value+"</"+self.tag.lstrip('"').rstrip('"')+'>'
            else:    
                return '<'+self.tag.lstrip('"').rstrip('"')+self.props_to_html()+">"+self.value+"</"+self.tag.lstrip('"').rstrip('"')+'>'