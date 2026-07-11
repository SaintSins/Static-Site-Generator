from src.markdown_blocks import markdown_to_html_node
from src.markdown_blocks import extract_title
import os

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        html_template = f.read()

    html_content = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    final_html = html_template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str) -> None:
    dir_contents = os.listdir(dir_path_content)
    for content in dir_contents:
        content_path = os.path.join(dir_path_content,content)
        if not os.path.isfile(content_path):
            generate_pages_recursive(content_path,template_path,os.path.join(dest_dir_path,content), basepath)
        else:
            if content.endswith(".md"):
                html_filename = content.replace(".md", ".html")
                dest_file_path = os.path.join(dest_dir_path, html_filename)
                generate_page(content_path, template_path, dest_file_path, basepath)

