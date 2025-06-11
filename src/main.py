from textnode import TextNode,TextType
from htmlnode import HTMLNode,ParentNode,LeafNode
from pagegenerator import generate_page,generate_pages_recursive
from fileprep import empty_destdir,file_preparation
import os
import shutil
import sys

if len(sys.argv)>1:
    basepath=str(sys.argv[1])
else:
    basepath="/"

def main():
    file_preparation("static","docs")
    #generate_page("content/index.md","template.html","public/index.html")
    generate_pages_recursive("content","template.html","docs",basepath)

main()