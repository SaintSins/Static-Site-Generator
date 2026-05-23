from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def markdown_to_blocks(markdown):
    raw_blocks = markdown.split('\n\n')
    cleaned_blocks = []
    for block in raw_blocks:
        stripped_block = block.strip()
        if stripped_block == "":
            continue
        cleaned_blocks.append(stripped_block)
    return cleaned_blocks