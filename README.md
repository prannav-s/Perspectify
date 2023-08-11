# Project: Perspectify

## Overview

Perspectify is a tool designed to make the consumption and understanding of online articles easier and more efficient. The application utilizes advanced natural language processing techniques to summarize articles, provide different perspectives on the topic, and detect possible biases. This project is designed to help readers get the most out of their online reading experience by reducing the time and effort required to comprehend complex articles, and by offering a multi-faceted view on the subject matter.

## Features

1. **Article Summarization:** Our tool can condense lengthy articles into shorter versions, retaining key points and insights for quick understanding.

2. **Perspective Analysis:** We provide various possible viewpoints on the article's topic, giving the reader a comprehensive understanding of the subject.

3. **Bias Detection:** The tool can identify potential biases in the articles, promoting critical thinking and balanced perspectives.

## Usage

1. **Web Scraper:** To fetch and extract content from the web, we've implemented a robust web scraper. For detailed usage, check the comments in the `WebScrape.py` file.

2. **Article Analyzer:** The summarization, perspective analysis, and bias detection are performed by the Article Analyzer. Detailed instructions are provided in the `functions.py` file.

## Getting Started

Run the following commands on your local machine:

```
git clone https://github.com/PrannavS/Perspectify.git
pipenv django
pip shell
```

After cloning the repository, create a .env file in the main directory and set the value of OPENAI_API_KEY to your secret API KEY. You can acquire this key from your OpenAI account at https://platform.openai.com/account/api-keys.

```
set OPENAI_API_KEY = 'YOUR-API-KEY' in .env file
```

Once you have the configurations set up, perform the following commands to run the program:

```
cd ../Perspectify
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

This will then start a development at your localhost, <http://127.0.0.1:8000/> by default.

## Contributions

We welcome contributions from everyone. Feel free to create an issue or make a pull request.

## License

This project is licensed under the terms of the MIT license.

For the full license, see [LICENSE](LICENSE)

## Acknowledgements

We would like to express our gratitude to OpenAI for their API which helped us in developing this application.
(Insert Here)

## DEMO ##
<https://drive.google.com/file/d/1LK5fLRHWn9T7JHuNOGGJfxs8cImb6ZBK/view?resourcekey>
