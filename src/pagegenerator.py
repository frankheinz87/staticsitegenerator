from mdtohtmlnodeconverter import markdown_to_html_node
from titleextractor import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        read_data=f.read()
    with open(template_path) as t:
        template_data=t.read()
    
    Node=markdown_to_html_node(read_data)
    String=Node.to_html()
    Title=extract_title(read_data)
    final_data=template_data.replace("{{ Title }}",Title).replace("{{ Content }}", String)
    #creating target file
    #os.makedirs(dest_path)
    with open(dest_path,"x") as final:
        final.write(final_data)
    