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

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
        
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
        
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    
    is_unordered = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered = False
            break
    if is_unordered:
        return BlockType.UNORDERED_LIST
    
    is_ordered = True
    counter = 1
    for line in lines:
        if not line.startswith(f'{counter}. '):
            is_ordered = False
            break
        else:
            counter += 1
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
        