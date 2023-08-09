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
    # Return a text of primary viewpoint
    pass

def secondary_function(text):
    # Return a text of secondary viewpoint
    pass

def resources(viewpoints):
    # Return a list of strings of additional resource links
    pass
    