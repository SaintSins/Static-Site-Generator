from src.textnode import TextNode, TextType
from re import findall

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        splited_node = node.text.split(delimiter)
        if len(splited_node)%2 == 0: #Length of the splitted node will be in odd number if closing delimeter is present
            raise Exception("Invalid markdown, formatted section not closed.")
        for i, part in enumerate(splited_node):
            if i % 2 == 0:
                if part != "":
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                if part != "":
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!\!)\[(.*?)\]\((.*?)\)"
    return findall(pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_img = extract_markdown_images(node.text)
        if not extracted_img:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for img_alt, img_link in extracted_img:
            markdown_str = f'![{img_alt}]({img_link})'
            splited_node_img = remaining_text.split(markdown_str,1)
            if splited_node_img[0] != "":
                new_nodes.append(TextNode(splited_node_img[0], TextType.TEXT))
            new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_link))
            remaining_text = splited_node_img[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_link = extract_markdown_links(node.text)
        if not extracted_link:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for link_text, link_url in extracted_link:
            markdown_str = f'[{link_text}]({link_url})'
            splited_node_link = remaining_text.split(markdown_str,1)
            if splited_node_link[0] != "":
                new_nodes.append(TextNode(splited_node_link[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            remaining_text = splited_node_link[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "__", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes