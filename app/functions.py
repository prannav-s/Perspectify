import os
import openai
import re
from .WebScrape import WebScrape


# Function to generate prompt for the OpenAI API
def generate_prompt(text):
    return f"""You will summarize an article given the text from it. 
    
    At the end give sources for alternative news articles from different sources ONLY in the form of websites about the same event.
    Do this in the format: Alternative news sources: numbered list of sources
    Only recommend reputable sources. 
    Do not recommend any social medias. {text.capitalize()}"""
    

# Function to extract links from text using Redux
def extract_links_from_text(text):
    # Using regular expression to find URLs in the text
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return urls


# Remove alternative sources from text
def remove_alternative_sources_and_after(text):
    # Remove all text after the sentence starting with "Alternative news sources: "
    modified_text = text.split("Alternative news sources: ")[0]
    return modified_text    