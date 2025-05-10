import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse
import os
import time
import re

class WebHarvesterPro:
    def __init__(self, base_url, max_depth=2, max_threads=5):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited = set()
        self.results = {}
        self.max_threads = max_threads
        self.output_dir = "webharvester_output"
        os.makedirs(self.output_dir, exist_ok=True)

    def fetch(self, url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")
        return None

    def extract_links(self, html, current_url):
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(current_url, href)
            if self.base_url in full_url:
                links.add(full_url.split('#')[0])
        return links

    def extract_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text(separator='\n', strip=True)

    def save_to_file(self, url, content):
        domain = urlparse(url).netloc.replace('.', '_')
        filename = re.sub(r'\W+', '_', urlparse(url).path)
        if not filename:
            filename = "root"
        file_path = os.path.join(self.output_dir, f"{domain}_{filename}.txt")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def crawl_page(self, url, depth):
        if url in self.visited or depth > self.max_depth:
            return
        print(f"[CRAWLING] {url} at depth {depth}")
        self.visited.add(url)
        html = self.fetch(url)
        if html:
            text = self.extract_text(html)
            self.results[url] = text
            self.save_to_file(url, text)
            links = self.extract_links(html, url)
            return [(link, depth + 1) for link in links]
        return []

    def start(self):
        print(f"Starting crawl on {self.base_url} with depth {self.max_depth} and {self.max_threads} threads")
        tasks = [(self.base_url, 0)]
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_url = {}
            while tasks:
                new_tasks = []
                for url, depth in tasks:
                    future = executor.submit(self.crawl_page, url, depth)
                    future_to_url[future] = (url, depth)

                tasks.clear()
                for future in as_completed(future_to_url):
                    result = future.result()
                    if result:
                        tasks.extend(result)

        print(f"Crawling complete. {len(self.results)} pages saved in '{self.output_dir}'.")


if __name__ == "__main__":
    start_time = time.time()
    harvester = WebHarvesterPro("https://example.com", max_depth=2, max_threads=5)
    harvester.start()
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
