import os
import openai
from .WebScrape import WebScrape

openai.api_key = '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'

# Function to make the summary
def summary(text):
    prompt =  """You will summarize an article given the text from it, and remove any bias from the summary in the process. 
    You will then give a rating based on how biased the original article was from one to ten, with ten being the most biased.""".format(
        text.capitalize()
    )
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.6,
        ).choices[0].text
    return response

def primary_function(text):
    pass

def secondary_function(text):
    pass

def resources(viewpoints):
    # I think it would be easier if the input for this function would just be a list of 
    # like phrases of the viewpoints so as to make it easier to render links from ChatGPT
    pass
    