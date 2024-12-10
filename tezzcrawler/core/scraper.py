"""Core scraping functionality."""

import time
import random
from pathlib import Path
from typing import Optional, Dict

import requests
import markdownify
from bs4 import BeautifulSoup

from ..utils.headers import get_headers
from ..utils.proxy import create_proxy_config


class Scraper:
    """Base scraper class for handling web page scraping."""
    
    def __init__(
        self,
        proxy_url: Optional[str] = None,
        proxy_port: Optional[int] = None,
        proxy_username: Optional[str] = None,
        proxy_password: Optional[str] = None,
    ):
        """Initialize the scraper with optional proxy configuration.
        
        Args:
            proxy_url: Optional proxy URL
            proxy_port: Optional proxy port
            proxy_username: Optional proxy username
            proxy_password: Optional proxy password
        """
        self.headers = get_headers()
        self.proxy = create_proxy_config(
            proxy_url, proxy_port, proxy_username, proxy_password
        )
    
    def get_page(self, url: str) -> requests.Response:
        """Fetch a web page.
        
        Args:
            url: The URL to fetch
            
        Returns:
            requests.Response: The response from the server
        """
        return requests.get(url, proxies=self.proxy, headers=self.headers)
    
    def convert_to_markdown(self, html_content: str) -> str:
        """Convert HTML content to markdown.
        
        Args:
            html_content: The HTML content to convert
            
        Returns:
            str: The markdown version of the content
        """
        return markdownify.markdownify(html_content, heading_style="ATX")
    
    def save_content(self, content: str, output_path: Path) -> None:
        """Save content to a file.
        
        Args:
            content: The content to save
            output_path: The path where to save the content
        """
        output_path.parent.mkdir(exist_ok=True, parents=True)
        output_path.write_text(content)
    
    def scrape_page(self, url: str, output_dir: Path) -> None:
        """Scrape a single page and save its content.
        
        Args:
            url: The URL to scrape
            output_dir: Directory to save the scraped content
        """
        response = self.get_page(url)
        soup = BeautifulSoup(response.content, "html.parser")
        markdown = self.convert_to_markdown(str(soup))
        
        # Create a filename from the URL
        save_path = output_dir / f"{url.split('/')[-2]}" / f"{url.split('/')[-1]}.md"
        self.save_content(markdown, save_path)
