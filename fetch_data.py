import requests

def fetch_articles(topic, api_key):
    """
    Fetches the latest news articles based on the given topic from News API.

    Parameters:
    topic (str): The topic to search for in the news.
    api_key (str): The API key for accessing News API.

    Returns:
    list: A list of dictionaries containing article information, or an empty list if an error occurs.
    """
    url = f"https://newsapi.org/v2/top-headlines?q={topic}&apiKey={api_key}&language=en&pageSize=5"
    
    try:
        response = requests.get(url)
        
        # Check if the request was successful (HTTP 200)
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            return articles
        else:
            # If there was an issue, print the error message
            print(f"Error fetching news: {response.status_code} - {response.text}")
            return []
    
    except requests.exceptions.RequestException as e:
        # Handle any exception that might occur during the request
        print(f"An error occurred while fetching articles: {e}")
        return []