import requests
import openai
from bs4 import BeautifulSoup

# Function to search for an article
def search_article(query):
    # Replace spaces in the query with '+' for the Google search URL
    query = query.replace(' ', '+')
    
    # Perform a Google search
    response = requests.get(f'https://www.google.com/search?q={query}')

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first search result and return its URL
    for result in soup.find_all('a'):
        url = result.get('href')
        if 'url?q=' in url and 'google.com' not in url:
            return url.split('url?q=')[1].split('&')[0]
            
    return None

# Then in your generate_post() function, use this function to generate a link:
def generate_post_with_link():
    prompt = "Provide a topic for a business-related article."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )
    topic = response.choices[0].text.strip()
    link = search_article(topic)
    return f"Check out this interesting article on {topic}: {link}"
