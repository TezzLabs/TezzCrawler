# TezzCrawler

A CLI tool to crawl a site and convert all .html files to markdown. Use this when you want to feed an entire site to a LLM model.

## Usage

Install Python dependencies:
```
pip install -r requirements.txt
```

Run the CLI:
```
python main.py crawl-from-sitemap https://www.example.com/sitemap.xml
```

To scrape a single page and convert it to markdown:
```
python main.py scrape-page https://www.example.com/page.html
```


### Using a Proxy

The code by default will not use a proxy. The code is designed around [Webshare](https://www.webshare.io/?referral_code=jgg1tzyv4izf) proxy services. You can sign up for a free account and get 10 IP addresses to use for free.

Once you have an account, create a `.env` file and add your API key:
```
WEBSHARE_API_KEY=your_api_key_here
```

Then, use the `--use-proxy` flag to enable the proxy:
```
python main.py crawl-from-sitemap https://www.example.com/sitemap.xml --use-proxy
```


