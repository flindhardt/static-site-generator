import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag='a', props={'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag='p', value='Hello, world!')
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=Hello, world!, children=[], props={})")

    def test_children_and_value(self):
        child_node = HTMLNode(tag='span', value='Text inside span')
        parent_node = HTMLNode(tag='div', children=[child_node])
        self.assertEqual(parent_node.children[0].value, 'Text inside span')

if __name__ == '__main__':
    unittest.main()