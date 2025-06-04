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
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value==None:
            raise ValueError
        elif self.tag==None:
            return self.value
        else:
            if self.props==None:
                return '<'+self.tag+">"+self.value+"</"+self.tag+'>'
            else:    
                return '<'+self.tag+self.props_to_html()+">"+self.value+"</"+self.tag+'>'

class ParentNode(HTMLNode):
    def __init__(self, tag , children , props = None):
        super().__init__(tag, value=None, children=children, props=None)

    def to_html(self):
        if self.tag==None:
            raise ValueError
        elif self.children==None:
            raise ValueError
        else:
            if self.props==None:
                result='<'+self.tag+">"
            else:
                result='<'+self.tag+self.props_to_html()+">"
            for child in self.children:
                result+=child.to_html()
            return result+"</"+self.tag+'>'