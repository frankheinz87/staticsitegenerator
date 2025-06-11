from mdtohtmlnodeconverter import markdown_to_html_node
from titleextractor import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        read_data=f.read()
    with open(template_path) as t:
        template_data=t.read()
    
    node=markdown_to_html_node(read_data)
    html=node.to_html()
    title=extract_title(read_data)
    final_data=template_data.replace("{{ Title }}",title).replace("{{ Content }}", html)
    #creating target file
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path,"w") as final:
        final.write(final_data)
    