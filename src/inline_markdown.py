from textnode import TextNode, TextType
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
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
        return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!\!)\[(.*?)\]\((.*?)\)"
    return findall(pattern, text)

        