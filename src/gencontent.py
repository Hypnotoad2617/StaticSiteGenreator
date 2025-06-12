import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/',f'href="{basepath}')
    template = template.replace('src="/',f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):   
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content,item)
        if os.path.isfile(item_path):
            #path points to a file
            new_dest_file = os.path.join(dest_dir_path,item).replace(".md",".html")
            print(f"file found: using {item_path} to generate {new_dest_file}")
            generate_page(item_path,template_path,new_dest_file, basepath)
        else:
            # path point to a folder
            new_dest_path = os.path.join(dest_dir_path,item)
            generate_page_recursive(item_path, template_path,new_dest_path, basepath)