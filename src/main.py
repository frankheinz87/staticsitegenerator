from textnode import TextNode,TextType
from htmlnode import HTMLNode

def main():
    Hello=TextNode("Hello World", TextType.LINK, "https://www.boot.dev" )
    Hello2=HTMLNode("p","Hello",[],{"href": "https://www.google.com", "target": "_blank"})
    print(Hello)
    print(Hello2)


main()
