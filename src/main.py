from textnode import *
from htmlnode import *
from inline_markdown import *
import re

def main():
    test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    
    text_to_testnodes(test_text)
    
    #node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(node)

    #html_node =  HTMLNode("p","text text lol", None,{"class": "greeting", "href": "https://boot.dev"})
    #print(html_node.props_to_html())
    #print(html_node)
    
    #old_node = TextNode("Boot.dev logo **möp** chalala _habemus papam_ er heißt **leo**, cool", TextType.TEXT)
    #print(old_node)
    #nodes_after_bold = split_nodes_delimiter([old_node],"**", TextType.BOLD)
    #print(nodes_after_bold)
    #nodes_after_italic = split_nodes_delimiter(nodes_after_bold,"_", TextType.ITALIC)
    #print(nodes_after_italic)
    #nodes_after_code = split_nodes_delimiter(nodes_after_italic,"'", TextType.CODE)
    #print(nodes_after_code)
    
    '''my
    node_lnk = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
    )
    
    node_img = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    
    print("Test link node with link function:")
    test = split_nodes_link([node_lnk])
    print(test)

    print("Test image node with image function:")
    test2 = split_nodes_image([node_img])
    print(test2)

    print("test link node with image function:")
    test3 = split_nodes_image([node_lnk])
    print(test3)

    print("test image node with link function:")
    test4 = split_nodes_link([node_img])
    print(test4)
    
    test5 = split_nodes_link([node_img,node_lnk])
    print(test5)
    test6 = split_nodes_image(test5)
    print(test6)
    '''
    return

main()