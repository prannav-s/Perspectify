import os

import openai
from flask import Flask, repipdirect, render_template, request, url_for

app = Flask(__name__)
app.debug = True
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["text"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(text),
            temperature=0.6,
        )
        return repipdirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(text):
    return """You will summarize an article given the text from it, and remove any bias from the summary in the process. 
    You will then give a rating based on how biased the original article was from one to ten, with ten being the most biased.""".format(
        text.capitalize()
    )
