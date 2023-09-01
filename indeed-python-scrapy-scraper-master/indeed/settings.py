
BOT_NAME = 'indeed'

SPIDER_MODULES = ['indeed.spiders']
NEWSPIDER_MODULE = 'indeed.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

## ScrapeOps API Key
SCRAPEOPS_API_KEY = '08f8ddd0-35bf-4470-9347-caee6b6accd3' ## Get Free API KEY here: https://scrapeops.io/app/register/main

## Enable ScrapeOps Proxy
SCRAPEOPS_PROXY_ENABLED = True

SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}

# Add In The ScrapeOps Monitoring Extension
EXTENSIONS = {
'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
}



DOWNLOADER_MIDDLEWARES = {

    ## ScrapeOps Monitor
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    
    ## Proxy Middleware
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    # 'indeed.middlewares.ScrapeOpsProxyMiddleware': 725,
}

# Max Concurrency On ScrapeOps Proxy Free Plan is 1 thread
CONCURRENT_REQUESTS = 1

DOWNLOAD_DELAY = 2  # minimum download delay 
AUTOTHROTTLE_ENABLED = True