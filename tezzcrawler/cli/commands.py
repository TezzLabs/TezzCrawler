"""Command-line interface for TezzCrawler."""

from pathlib import Path
from typing import Optional

import typer

from ..core.scraper import Scraper
from ..core.crawler import Crawler


app = typer.Typer()


@app.command("scrape-page", help="Scrape a single webpage")
def scrape_page(
    url: str = typer.Argument(..., help="The URL of the webpage to scrape"),
    proxy_url: Optional[str] = typer.Option(
        None, "--proxy-url", help="The URL of the proxy to use"
    ),
    proxy_port: Optional[int] = typer.Option(
        None, "--proxy-port", help="The port of the proxy to use"
    ),
    proxy_username: Optional[str] = typer.Option(
        None, "--proxy-username", help="The username of the proxy to use"
    ),
    proxy_password: Optional[str] = typer.Option(
        None, "--proxy-password", help="The password of the proxy to use"
    ),
    output: Path = typer.Option(
        ..., "--output", help="The output directory to save the scraped content"
    ),
) -> None:
    """Scrape a single webpage and save its content as markdown.
    
    Args:
        url: The URL to scrape
        proxy_url: Optional proxy URL
        proxy_port: Optional proxy port
        proxy_username: Optional proxy username
        proxy_password: Optional proxy password
        output: Output directory for saving content
    """
    scraper = Scraper(proxy_url, proxy_port, proxy_username, proxy_password)
    scraper.scrape_page(url, output)


@app.command("crawl-from-sitemap", help="Crawl a site from a sitemap.xml url")
def crawl_from_sitemap(
    sitemap_url: str = typer.Argument(..., help="The URL of the sitemap.xml file"),
    proxy_url: Optional[str] = typer.Option(
        None, "--proxy-url", help="The URL of the proxy to use"
    ),
    proxy_port: Optional[int] = typer.Option(
        None, "--proxy-port", help="The port of the proxy to use"
    ),
    proxy_username: Optional[str] = typer.Option(
        None, "--proxy-username", help="The username of the proxy to use"
    ),
    proxy_password: Optional[str] = typer.Option(
        None, "--proxy-password", help="The password of the proxy to use"
    ),
    output: Path = typer.Option(
        ..., "--output", help="The output directory to save the scraped content"
    ),
) -> None:
    """Crawl a website using its sitemap.xml and save all pages as markdown.
    
    Args:
        sitemap_url: URL of the sitemap.xml file
        proxy_url: Optional proxy URL
        proxy_port: Optional proxy port
        proxy_username: Optional proxy username
        proxy_password: Optional proxy password
        output: Output directory for saving content
    """
    crawler = Crawler(proxy_url, proxy_port, proxy_username, proxy_password)
    crawler.crawl_sitemap(sitemap_url, output)
