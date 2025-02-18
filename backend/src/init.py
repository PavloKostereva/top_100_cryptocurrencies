from src.config import settings

from src.http_client import CMCHTTPClient


cms_client=CMCHTTPClient(

    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMS_API_KEY,
)
