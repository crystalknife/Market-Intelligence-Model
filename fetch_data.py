# data_ingestion/fetch_data.py

import requests

def fetch_news_data(api_key, country='us'):
    """
    Fetches top business news headlines using NewsAPI.
    """
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Returns a dictionary of news data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    API_KEY = "Your API key"  # Replace with your actual NewsAPI key
    try:
        news_data = fetch_news_data(API_KEY)
        print(news_data)
    except Exception as e:
        print(e)
