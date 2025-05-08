import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_diff(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.wikipedia.de")
        self.assertNotEqual(node, node2)


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

def test_bold(self):
    node = TextNode("This is bold text", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is bold text")
    self.assertEqual(html_node.props, {})

def test_italic(self):
    node = TextNode("This is italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "This is italic text")
    self.assertEqual(html_node.props, {})

def test_code(self):
    node = TextNode("print('Hello, world!')", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "print('Hello, world!')")
    self.assertEqual(html_node.props, {})

def test_link(self):
    node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "Boot.dev")
    self.assertEqual(html_node.props, {"href": "https://boot.dev"})

def test_image(self):
    node = TextNode("Boot.dev logo", TextType.IMAGE, "https://boot.dev/logo.png")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")

if __name__ == "__main__":
    unittest.main()