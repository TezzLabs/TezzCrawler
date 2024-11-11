import os
import logging
from pathlib import Path

import typer
import requests
import markdownify
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()


def get_proxy():
    proxy = dict()  # TODO: Add proxy
    return proxy

@app.command("scrape-page", help="Scrape a single webpage")
def scrape_page(
    url: str = typer.Argument(..., help="The URL of the webpage to scrape"),
    use_proxy: bool = typer.Option(
        False, "--use-proxy", help="Use a proxy to scrape the page"
    ),
):
    proxy = get_proxy() if use_proxy else None
    response = requests.get(url, proxies=proxy)
    soup = BeautifulSoup(response.content, "html.parser")
    markdown = markdownify.markdownify(str(soup), heading_style="ATX")
    save_path = Path(__file__).parent / f"{url.split('/')[-2]}" / f"{url.split('/')[-1]}.md"
    save_path.parent.mkdir(exist_ok=True)
    save_path.write_text(markdown)


@app.command("convert-to-markdown", help="Convert a .html file to markdown")
def convert_to_markdown(
    html_file: str = typer.Argument(..., help="The path to the .html file to convert"),
):
    pass


@app.command("crawl-site", help="Crawl a site and convert all .html files to markdown")
def crawl_site(
    url: str = typer.Argument(..., help="The URL of the site to crawl"),
    use_proxy: bool = typer.Option(
        False, "--use-proxy", help="Use a proxy to crawl the site"
    ),
):
    pass


def not_valid_sitemap_url(sitemap_url: str) -> bool:
    return not sitemap_url.endswith(".xml")


@app.command("crawl-from-sitemap", help="Crawl a site from a sitemap.xml url")
def crawl_from_sitemap(
    sitemap_url: str = typer.Argument(..., help="The URL of the sitemap.xml file"),
    use_proxy: bool = typer.Option(
        False, "--use-proxy", help="Use a proxy to crawl the site"
    ),
):
    proxy = get_proxy() if use_proxy else None
    if not_valid_sitemap_url(sitemap_url):
        raise ValueError("Invalid sitemap URL")
    pass


if __name__ == "__main__":
    log_folder = Path(__file__).parent / "logs"
    log_folder.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s || %(name)s || %(levelname)s || %(message)s",
        handlers=[logging.FileHandler(log_folder / "app.log"), logging.StreamHandler()],
    )

    app()
