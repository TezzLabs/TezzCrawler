import time
import random
from pathlib import Path

import typer
import requests
import markdownify
from bs4 import BeautifulSoup
from rich.progress import track

from tezzcrawler.webshare import WebshareAPI


app = typer.Typer()


def get_proxy(webshare_api: str):
    api = WebshareAPI(webshare_api)
    proxy_details = api.get_proxy()
    proxy = {
        "http": f"http://{proxy_details}",
        # "https": f"https://{proxy_details}",
    }
    return proxy


def get_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers",
    }


@app.command("scrape-page", help="Scrape a single webpage")
def scrape_page(
    url: str = typer.Argument(..., help="The URL of the webpage to scrape"),
    webshare_api: str = typer.Option(
        None, "--webshare-api", help="Webshare API key to use a proxy"
    ),
    output: Path = typer.Option(
        ..., "--output", help="The output directory to save the scraped content"
    ),
):
    proxy = get_proxy(webshare_api) if webshare_api else None
    headers = get_headers()
    response = requests.get(url, proxies=proxy, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    markdown = markdownify.markdownify(str(soup), heading_style="ATX")
    save_path = output / f"{url.split('/')[-2]}" / f"{url.split('/')[-1]}.md"
    save_path.parent.mkdir(exist_ok=True, parents=True)
    save_path.write_text(markdown)


def not_valid_sitemap_url(sitemap_url: str) -> bool:
    return not sitemap_url.endswith(".xml")


@app.command("crawl-from-sitemap", help="Crawl a site from a sitemap.xml url")
def crawl_from_sitemap(
    sitemap_url: str = typer.Argument(..., help="The URL of the sitemap.xml file"),
    webshare_api: str = typer.Option(
        None, "--webshare-api", help="Webshare API key to use a proxy"
    ),
    output: Path = typer.Option(
        ..., "--output", help="The output directory to save the scraped content"
    ),
):
    if not_valid_sitemap_url(sitemap_url):
        raise ValueError("Invalid sitemap URL")
    proxy = get_proxy(webshare_api) if webshare_api else None
    headers = get_headers()
    response = requests.get(sitemap_url, proxies=proxy, headers=headers)
    soup = BeautifulSoup(response.content, "xml")
    urls = [loc.text for loc in soup.find_all("loc")]
    for url in track(urls, description="Scraping pages"):
        response = requests.get(url, proxies=proxy, headers=headers)
        page_soup = BeautifulSoup(response.content, "html.parser")
        markdown = markdownify.markdownify(str(page_soup), heading_style="ATX")
        save_path = (
            output / f"{url.split('/')[2]}" / f"{'-'.join(url.split('/')[3:])}.md"
        )
        save_path.parent.mkdir(exist_ok=True, parents=True)
        save_path.write_text(markdown)
        time.sleep(random.uniform(1, 3))


if __name__ == "__main__":
    app()
