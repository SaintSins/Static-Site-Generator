from enum import Enum
from typing import List,Dict
from src.textnode import TextNode, TextType

class EscapeMarker(Enum):
    # The Core Inline
    ASTERISK = "@@@ESCAST@@@"      # For \*
    UNDERSCORE = "@@@ESCUND@@@"    # For \_
    BACKTICK = "@@@ESCTICK@@@"     # For \`
    
    # The Link/Image Breakers
    L_BRACKET = "@@@ESCLBRACK@@@"  # For \[
    R_BRACKET = "@@@ESCRBRACK@@@"  # For \]
    L_PAREN = "@@@ESCLPAREN@@@"    # For \(
    R_PAREN = "@@@ESCRPAREN@@@"    # For \)

    #The Block Breakers
    HASH_HEADING = "@@@ESCHASHHEAD@@@" # For \#
    GREATER_THAN_QUOTES = "@@@ESCGTQ@@@" # For \>
    MINUS_LIST = "@@@ESCMINUSLIST@@@" # For \-
    DOT_OL ="@@@ESCDOTOL" #For \.

    #The Inception Character
    BACKSLASH = "@@@ESCBACKSLASH@@@" # For \\

escape_map = {
    r"\*": EscapeMarker.ASTERISK.value,
    r"\_": EscapeMarker.UNDERSCORE.value,
    r"\`": EscapeMarker.BACKTICK.value,
    r"\[": EscapeMarker.L_BRACKET.value,
    r"\]": EscapeMarker.R_BRACKET.value,
    r"\(": EscapeMarker.L_PAREN.value,
    r"\)": EscapeMarker.R_PAREN.value,
    r"\#": EscapeMarker.HASH_HEADING.value,
    r"\>": EscapeMarker.GREATER_THAN_QUOTES.value,
    r"\-": EscapeMarker.MINUS_LIST.value,
    r"\.": EscapeMarker.DOT_OL.value,
    r"\\": EscapeMarker.BACKSLASH.value
}

def hide_escape_chars (text: str, escape_map: Dict[str, str]) -> str:
    for key,value in escape_map.items():
        text = text.replace(key, value)
    return text

def restore_chars (nodes: List[TextNode],escape_map: Dict[str,str]) -> List[TextNode]:
    cleaned_nodes = []
    for node in nodes:
        if node.text_type == TextType.TEXT:
            current_text = node.text
            for key,value in escape_map.items():
                litertal_char = key[1:]
                current_text = current_text.replace(value,litertal_char)
            cleaned_nodes.append(TextNode(current_text, TextType.TEXT, node.url))
        else:
            cleaned_nodes.append(node)
    return cleaned_nodes