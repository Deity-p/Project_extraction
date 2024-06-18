# Web Scraping Script with Text File Output
This Python script utilizes BeautifulSoup and requests libraries to scrape text 
content from a specified webpage. The scraped content is then saved into a local 
text file (article.txt).

## Getting Started
    To use this script, follow the instructions below.
### Prerequisites
    Make sure you have Python installed on your system. You can download it from
    python.org.
### Installation
    Clone this repository or download the Python script (webscraper.py) directly.
Install the required libraries using pip:

    pip install beautifulsoup4 
    pip install requests

### How to Use
1. Input Requirements:

    user_url: The URL of the webpage you want to scrape.
    html_tag: The HTML tag containing the content you want to scrape (e.g., div, p).
    html_class: The class name of the HTML tag (optional).
2. Running the Script:
    Open a terminal or command prompt.
    Navigate to the directory where webscraper.py is located.
    Run the script by typing:

        python webscraper.py

    Follow the prompts to enter the user_url, html_tag, and html_class.
3. Output:
    The scraped text content will be saved to a file named article.txt in the same
    directory.

## Functions Explained
### main()
    Initiates the script by getting user inputs (user_url, html_tag, html_class), 
    scraping the webpage (pharse_data()), and saving the content to article.txt 
    (save_as_text()).
### get_html_data()
    Prompts the user to input the user_url, html_tag, and html_class.
### pharse_data(user_url, html_tag, html_class)
    Uses requests to fetch the HTML content from user_url.
    Parses the HTML using BeautifulSoup to find the content specified by html_tag 
    and optionally html_class.
    Returns the found content (article) or None if there are errors.
### save_as_text(article)
    Receives the article object containing parsed HTML content.
    Extracts text from <p> tags within article, cleans up the text, and saves it 
    to article.txt.

## Error Handling
    The script handles common errors such as invalid URLs (RequestException) and 
    parsing issues (Exception) during web scraping.

## Notes
    Ensure the article.txt file is not open in another application while running 
    the 
    script to prevent file access errors.
    Customize HTML parsing and text cleaning methods within pharse_data() and 
    save_as_text() based on specific webpage structures and content requirements.