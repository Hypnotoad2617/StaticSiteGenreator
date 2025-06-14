import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"



def main():

    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_page_recursive(dir_path_content, template_path, dir_path_public, basepath)


    print(f"using basepath: {basepath}")
main()
