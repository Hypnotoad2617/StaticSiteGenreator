from textnode import *
from htmlnode import *
from inline_markdown import *
from markdown_blocks import *
from markdown2html import *
import re

def main():
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    blocks = markdown_to_blocks(md)
    block1 = blocks[0]

    #print(text_to_textnodes(block1))

    test = markdown_to_html_node(md)
    print(test)

    '''
    paragraph block to multiple text nodes, textnodes into html
    text_to_textnodes(text)
    '''
    # create a text_to_children(): function

    return




main()