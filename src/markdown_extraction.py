import re
from textnode import TextNode, TextType
from split_node_delimiter import split_nodes_delimiter

def extract_markdown_images(text):
    img_ptrn = re.compile(r"!\[(\w.+?)\]\((.+?)\)")

    alt_url_list = list(map(tuple, img_ptrn.findall(text)))
    return alt_url_list

def extract_markdown_links(text):
    lnk_ptrn = re.compile(r"(?<!!)\[(.+?)\]\((.+?)\)")

    anchor_url_list = list(map(tuple, lnk_ptrn.findall(text)))
    return anchor_url_list


def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        temp_text = node.text
        for alt_text, url in images:
            parts = temp_text.split(f'![{alt_text}]({url})', 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            temp_text = parts[1] if len(parts) > 1 else ""

        if temp_text:
            new_nodes.append(TextNode(temp_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        temp_text = node.text
        for anchor_text, url in links:
            parts = temp_text.split(f'[{anchor_text}]({url})', 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            temp_text = parts[1] if len(parts) > 1 else ""

        if temp_text:
            new_nodes.append(TextNode(temp_text, TextType.TEXT))

    return new_nodes


def text_to_textnode(text):
    new_text_node = TextNode(text = text, text_type = TextType.TEXT)
    delimiters_types = [("_", TextType.ITALIC), ("**", TextType.BOLD), ("`", TextType.CODE)]
    
    generated_list = [new_text_node]
    for delimiter, text_type in delimiters_types:
        generated_list = split_nodes_delimiter(generated_list, delimiter, text_type)
        
    generated_list = split_nodes_image(generated_list)
    generated_list = split_nodes_link(generated_list)
    
    return generated_list