#   Web content scraper.
# This code is inspired by Nikolas Schriefer on github and his project 'Summarizer'

# --- GUIDE FOR TEAM MEMBERS ---

# This Python class (WebScrape) is designed to extract text content from web pages.
# Follow the below steps in your script to use it:

# 1. Import the WebScrape class from this script: `from scraper import WebScrape`
# 2. Create an instance: `my_scraper = WebScrape.WebScrape()`
# 3. Fetch a web page: `web_page = my_scraper.fetch_url('https://example.com')`
# 4. Extract the text content: `text_content = my_scraper.parse_html_content(web_page)`
# 5. Now, 'text_content' contains the text content of the web page. Use it as per your need.

# Note: Replace 'https://example.com' with the actual URL you want to scrape.


import requests
from random import choice
from bs4 import BeautifulSoup


class WebScrape:
    """Web content extraction tool."""

    # Potential User Agents
    BROWSERS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    ]

    def __init__(self):
        # Initialize with a random user agent
        self.browser = choice(self.BROWSERS)

    def rotate_agent(self):
        """Switches the browser to the next one in the list."""
        self.browser = choice(self.BROWSERS)

    def fetch_url(self, link) -> requests.Response:
        """Send GET request to the link with the current browser."""
        try:
            resp = requests.get(link, headers={"User-Agent": self.browser, "Connection": "close"})
            self.rotate_agent()
            return resp
        except Exception as exc:
            return exc

    def parse_html_content(self, resp: requests.Response) -> str:
        """Extract and return the text content from the HTML."""
        parsed_html = BeautifulSoup(resp.text, "html.parser")
        text_parts = [
            txt.text for txt in parsed_html.find_all(["h1", "h2", "h3", "p"]) if len(txt.text) > 5
        ]
        return "\n\n".join(text_parts)

