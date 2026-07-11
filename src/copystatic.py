import os
import shutil

source = "static"
dest = "docs"

if os.path.exists(dest):
    shutil.rmtree(dest)

def copy_files_recursive(source: str, dest: str) -> None:
    if not os.path.exists(dest):
        os.mkdir(dest)
    source_contents = os.listdir(source)
    for content in source_contents:
        source_path = os.path.join(source,content)
        dest_path = os.path.join(dest,content)
        if os.path.isfile(source_path):
            shutil.copy(source_path,dest_path)
            print(f'Copying from {source_path} to {dest_path}')
        else:
            copy_files_recursive(source_path, dest_path)

