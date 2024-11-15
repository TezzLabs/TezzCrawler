# TezzCrawler

TezzCrawler is a command-line tool for crawling entire websites and converting HTML files to Markdown. It’s designed for developers who need to feed structured content from a website into a language model or process it for other analytical tasks.

## Features
- **Site-wide Crawling**: Crawl all pages listed in a sitemap.
- **Single-page Scraping**: Scrape and convert individual pages.
- **Markdown Conversion**: Convert HTML pages to Markdown for easy ingestion by LLMs.
- **Proxy Support**: Crawl sites using a proxy for added flexibility and access.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries listed in `requirements.txt`

### Installation

Clone the repository and install Python dependencies:
```bash
git clone <repository_url>
cd TezzCrawler
pip install -r requirements.txt
```

### Usage

#### 1. Crawl an Entire Site from a Sitemap
```bash
python main.py crawl-from-sitemap https://www.example.com/sitemap.xml
```

#### 2. Scrape and Convert a Single Page
```bash
python main.py scrape-page https://www.example.com/page.html
```

#### 3. Using a Proxy

TezzCrawler supports proxy crawling through [Webshare.io](https://www.webshare.io/?referral_code=jgg1tzyv4izf). Create a free account to obtain up to 10 free IP addresses.

1. **Configure Proxy**: Add your Webshare API key to a `.env` file in the project directory:
   ```bash
   WEBSHARE_API_KEY=your_api_key_here
   ```

2. **Enable Proxy**: Use the `--use-proxy` flag in your command to activate proxy usage:
   ```bash
   python main.py crawl-from-sitemap https://www.example.com/sitemap.xml --use-proxy
   ```
