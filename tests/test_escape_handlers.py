import unittest
from src.textnode import TextNode, TextType
from src.escape_handlers import escape_map, hide_escape_chars, restore_chars

class TestEscapeHandlers(unittest.TestCase):
    
    def test_hide_single_asterisk(self) -> None:
        raw_text = "This is a literal \\* asterisk"
        result = hide_escape_chars(raw_text, escape_map)
        self.assertIn("@@@ESCAST@@@", result)
        self.assertNotIn("\\*", result)

    def test_restore_single_asterisk(self) -> None:
        nodes = [TextNode("A literal @@@ESCAST@@@ character", TextType.TEXT)]
        result_nodes = restore_chars(nodes, escape_map)
        self.assertEqual(result_nodes[0].text, "A literal * character")

    def test_non_text_nodes_are_ignored(self) -> None:
        nodes = [TextNode("Bold @@@ESCAST@@@ stay untouched", TextType.BOLD)]
        result_nodes = restore_chars(nodes, escape_map)
        self.assertEqual(result_nodes[0].text, "Bold @@@ESCAST@@@ stay untouched")
    
    def test_multiple_escapes_in_one_string(self) -> None:
        raw_text = r"Click \*here\* or \_there\_"
        hidden_text = hide_escape_chars(raw_text, escape_map)
        nodes = [TextNode(hidden_text, TextType.TEXT)]
        restored_nodes = restore_chars(nodes, escape_map)
        self.assertEqual(restored_nodes[0].text, "Click *here* or _there_")

    def test_mixed_escaped_and_formatting(self) -> None:
        nodes = [
            TextNode("Bold text", TextType.BOLD),
            TextNode(f" with a literal {escape_map[r'\*']} asterisk", TextType.TEXT)
        ]
        restored_nodes = restore_chars(nodes, escape_map)
        self.assertEqual(restored_nodes[0].text, "Bold text")
        self.assertEqual(restored_nodes[0].text_type, TextType.BOLD)
        self.assertEqual(restored_nodes[1].text, " with a literal * asterisk")

    def test_escaped_backslash(self) -> None:
        raw_text = r"\\"
        hidden_text = hide_escape_chars(raw_text, escape_map)
        nodes = [TextNode(hidden_text, TextType.TEXT)]
        restored_nodes = restore_chars(nodes, escape_map)
        self.assertEqual(restored_nodes[0].text, "\\")

if __name__ == "__main__":
    unittest.main()