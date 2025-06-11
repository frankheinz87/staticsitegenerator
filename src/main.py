from textnode import TextNode,TextType
from htmlnode import HTMLNode,ParentNode,LeafNode
from pagegenerator import generate_page
from fileprep import empty_destdir,file_preparation
import os
import shutil

def main():
    file_preparation("static","public")
    generate_page("content/index.md","template.html","public/index.html")

main()