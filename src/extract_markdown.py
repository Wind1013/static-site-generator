import re


def extract_markdown_images(text):
    matches = re.findall("!\[(.*?)]\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall("\[(.*?)]\]\((.*?)\)", text)
    return matches
