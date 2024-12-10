"""Core crawler functionality."""

import time
import random
from pathlib import Path
from typing import Optional, List

from bs4 import BeautifulSoup

from .scraper import Scraper


class Crawler(Scraper):
    """Crawler class for handling sitemap-based crawling."""
    
    def is_valid_sitemap_url(self, url: str) -> bool:
        """Check if a URL is a valid sitemap URL.
        
        Args:
            url: The URL to check
            
        Returns:
            bool: True if the URL is a valid sitemap URL
        """
        return url.endswith(".xml")
    
    def extract_urls_from_sitemap(self, sitemap_content: str) -> List[str]:
        """Extract URLs from a sitemap.
        
        Args:
            sitemap_content: The content of the sitemap
            
        Returns:
            List[str]: List of URLs found in the sitemap
        """
        soup = BeautifulSoup(sitemap_content, "xml")
        return [loc.text for loc in soup.find_all("loc")]
    
    def crawl_sitemap(self, sitemap_url: str, output_dir: Path) -> None:
        """Crawl a sitemap and all its nested sitemaps.
        
        Args:
            sitemap_url: The URL of the sitemap
            output_dir: Directory to save the scraped content
            
        Raises:
            ValueError: If the sitemap URL is invalid
        """
        if not self.is_valid_sitemap_url(sitemap_url):
            raise ValueError(f"Invalid sitemap URL: {sitemap_url}")
        
        response = self.get_page(sitemap_url)
        urls = self.extract_urls_from_sitemap(response.content)
        
        for url in urls:
            if self.is_valid_sitemap_url(url):
                # Recursively process nested sitemaps
                self.crawl_sitemap(url, output_dir)
            else:
                # Process individual pages
                self.scrape_page(url, output_dir)
                print(f"Completed scraping: {url}")
                # Add random delay to avoid overwhelming the server
                time.sleep(random.uniform(1, 3))
