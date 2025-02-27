# data_ingestion/competitor_tracking.py

import requests

def fetch_competitor_news(api_key, competitor, page_size=10):
    """
    Fetches news articles related to a competitor using NewsAPI's 'everything' endpoint.
    
    Parameters:
    - api_key: Your NewsAPI key.
    - competitor: The name (or keyword) of the competitor to search for.
    - page_size: Number of articles to return (default is 10).
    
    Returns:
    - JSON response from NewsAPI containing news articles.
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": competitor,
        "pageSize": page_size,
        "apiKey": api_key,
        "language": "en"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch competitor news: {response.status_code} - {response.text}")
