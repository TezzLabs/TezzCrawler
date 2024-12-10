"""TezzCrawler - A web crawler for converting web pages to markdown.

This package provides functionality to:
1. Scrape single web pages and convert them to markdown
2. Crawl entire websites using their sitemap.xml
3. Support proxy configuration for web scraping
"""

from .cli.commands import app
from .core.scraper import Scraper
from .core.crawler import Crawler

__version__ = "0.2.0"
__all__ = ["app", "Scraper", "Crawler"]