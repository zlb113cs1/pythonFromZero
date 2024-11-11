import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def fetch_webpage(url):
    """Fetches the HTML content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def extract_links(html_content):
    """Extracts and returns all the hyperlinks from the given HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def analyze_text(html_content):
    """Analyzes the text content of the webpage and returns the word frequency."""
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    return word_count.most_common(10)

def main():
    url = input("Enter the URL of the webpage to scrape: ")
    html_content = fetch_webpage(url)
    
    if html_content:
        print("\nTop 10 Most Common Words:")
        common_words = analyze_text(html_content)
        for word, count in common_words:
            print(f"{word}: {count}")
        
        print("\nExtracted Links:")
        links = extract_links(html_content)
        for link in links[:10]:  # Display the first 10 links
            print(link)
        print(f"\nTotal links found: {len(links)}")

if __name__ == "__main__":
    main()
