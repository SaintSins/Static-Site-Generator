from src.markdown_blocks import markdown_to_html_node
from src.markdown_blocks import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        html_template = f.read()

    html_content = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    final_html = html_template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    dest_dir_path = os.path.dirname(dest_path)
    os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(final_html)
