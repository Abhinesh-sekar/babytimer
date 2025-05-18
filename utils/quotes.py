# utils/quotes.py - Motivational quotes utilities

import requests

ZEN_QUOTES_URL = "https://zenquotes.io/api/random"

def get_random_quote():
    """
    Return a random motivational quote using the ZenQuotes.io public API.
    Falls back to a default quote if the API call fails.
    """
    try:
        response = requests.get(ZEN_QUOTES_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"{data[0]['q']} - {data[0]['a']}"
        else:
            return "Keep pushing forward, your efforts will pay off!"
    except Exception:
        return "Keep pushing forward, your efforts will pay off!"
