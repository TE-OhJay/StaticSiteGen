import re



def extract_markdown_images(text):
    img_ptrn = re.compile("\!\[(\w.+?)\]\((.+?)\)")
    alt_url_list = list(map(tuple, img_ptrn.findall(text)))
    return alt_url_list

def extract_markdown_links(text):
    lnk_ptrn = re.compile("(?<!!)\[(.+?)\]\((.+?)\)")
    anchor_url_list = list(map(tuple, lnk_ptrn.findall(text)))
    return anchor_url_list