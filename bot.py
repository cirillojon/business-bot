import openai
import schedule
import time
import itertools

openai.api_key = 'sk-'

# Topics for posts
topics = ["sustainable business practices", "leadership", "entrepreneurship", "financial analysis", 
          "global market trends", "innovative business strategies", "corporate responsibility", 
          "technology in business", "business ethics", "diversity and inclusion in the workplace", 
          "business and the environment", "data-driven decision making", "strategic planning", 
          "risk management", "product development", "branding strategies", "customer relationship management", 
          "organizational culture", "business law", "e-commerce trends", "sales strategies", 
          "digital marketing", "business innovation", "negotiation skills", "networking strategies"]
topics_cycle = itertools.cycle(topics)


# Function to generate posts
def generate_post():
    profile = """"""
     # Get next topic from the cycle
    topic = next(topics_cycle)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Function to write message to a text file
def write_message():
    message = generate_post()

    # Write the message to a text file
    with open('linkedin_posts.txt', 'a') as file:
        file.write(message + '\n\n')

# Schedule the task
schedule.every(10).seconds.do(write_message)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)