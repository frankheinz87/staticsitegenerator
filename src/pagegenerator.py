from mdtohtmlnodeconverter import markdown_to_html_node
from titleextractor import extract_title
import os


def generate_page(from_path, template_path, dest_path,basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        read_data=f.read()
    with open(template_path) as t:
        template_data=t.read()
    
    node=markdown_to_html_node(read_data)
    html=node.to_html()
    title=extract_title(read_data)
    final_data=template_data.replace("{{ Title }}",title).replace("{{ Content }}", html).replace('href="/',f'href="{basepath}').replace('src="/',f'src="{basepath}')

    #creating target file
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path,"w") as final:
        final.write(final_data)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath="/"):
    content_list=os.listdir(dir_path_content)

    if content_list==[]:
        print("nothing to generate")
        return
    for item in content_list:
        content_path=os.path.join(dir_path_content,item)
        dest_path=os.path.join(dest_dir_path,item)
        if os.path.isfile(content_path):
            html_dest_path=dest_path.rstrip(".md")+".html"
            generate_page(content_path,template_path,html_dest_path,basepath)                  
        else:
            generate_pages_recursive(content_path,template_path,dest_path,basepath)
    