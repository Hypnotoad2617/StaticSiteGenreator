from textnode import *
from htmlnode import *

def main():
    #node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(node)

    html_node =  HTMLNode("p","text text lol", None,{"class": "greeting", "href": "https://boot.dev"})
    print(html_node.props_to_html())
    print(html_node)
    return

main()