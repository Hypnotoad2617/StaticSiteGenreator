#from textnode import *
#from htmlnode import *
#from inline_markdown import *
import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"


def markdown_to_blocks(markdown):
    temp_blocks = markdown.split("\n\n")
    block_array = []
    for block in temp_blocks:
        if block == "":
            continue
        else:
            block_array.append(block.strip())
    return block_array




def block_to_block_type(block):

    if re.match(r"\#{1,6} ",block):
        return BlockType.HEADING
    
    length = len(block)
    if length >= 6:
        if block[0:3] == "```" and block[-3:] == "```":
            return BlockType.CODE
    
    lines = block.splitlines()
    quote_flag = True
    for line in lines:
        if not re.match(r">",line):
            quote_flag = False
            break
    if quote_flag:
        return BlockType.QUOTE

    unordered_flag = True
    for line in lines:
        if not re.match(r"- ",line):
            unordered_flag = False
            break
    if unordered_flag:
        return BlockType.ULIST
    

    ordered_flag = True
    n = 0
    for line in lines:
        n +=1
        if not re.match(fr"{n}. ",line):
            ordered_flag = False
            break
    if ordered_flag:
        return BlockType.OLIST

    return BlockType.PARAGRAPH