# TezzCrawler

A powerful web crawler that converts web pages to markdown format, making them ready for LLM consumption.

## Features

- Single page scraping with markdown conversion
- Full website crawling using sitemap.xml
- Proxy support for web scraping
- Simple CLI interface
- Easy to use as a Python package

## Installation

```bash
pip install TezzCrawler
```

## Usage

### Command Line Interface

1. Scrape a single page:
```bash
tezzcrawler scrape-page https://example.com --output ./output
```

2. Crawl from sitemap:
```bash
tezzcrawler crawl-from-sitemap https://example.com/sitemap.xml --output ./output
```

3. Using with proxy:
```bash
tezzcrawler scrape-page https://example.com \
    --proxy-url proxy.example.com \
    --proxy-port 8080 \
    --proxy-username user \
    --proxy-password pass \
    --output ./output
```

### Python Package

```python
from tezzcrawler import Scraper, Crawler
from pathlib import Path

# Scrape a single page
scraper = Scraper()
scraper.scrape_page("https://example.com", Path("./output"))

# Crawl from sitemap
crawler = Crawler()
crawler.crawl_sitemap("https://example.com/sitemap.xml", Path("./output"))

# With proxy configuration
scraper = Scraper(
    proxy_url="proxy.example.com",
    proxy_port=8080,
    proxy_username="user",
    proxy_password="pass"
)
```

## Development

1. Clone the repository:
```bash
git clone https://github.com/TezzLabs/TezzCrawler.git
cd TezzCrawler
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## License

MIT License - see LICENSE file for details.

