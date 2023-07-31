import openai
import schedule
import time

# Initialize OpenAI's GPT-4 with your API key
openai.api_key = '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'

# Function to generate posts
def generate_post():
    profile = """
    Emily Robertson is a zealous individual with a wide array of interests. Apart from her love for number crunching and analyzing market trends, she finds solace in playing the violin and has a keen interest in hiking and photography. She loves to travel and explore different cultures, which broadens her perspective about various global business environments. Also, she enjoys reading books on entrepreneurship, finance, and business innovations.

    Emily dreams of revolutionizing the corporate world with innovative and sustainable solutions. She also envisions herself as a successful entrepreneur, leading a company that works at the intersection of technology and sustainability. Emily dreams of contributing towards creating an equitable business environment where everyone gets an opportunity to flourish.

    Emily aspires to begin her career as a financial analyst in a leading multinational corporation, thereby getting a better understanding of the global market and its dynamics. In the long term, she envisions herself founding a startup, providing sustainable solutions to pressing environmental issues through innovative business strategies.

    Emily strongly believes in the power of hard work, integrity, and perseverance. She values social responsibility and sustainability, emphasizing the role of businesses in building a greener future. She believes in leading by example and thinks that a great leader can inspire others to reach their full potential.

    Emily's passion lies in understanding and solving complex business problems. Her drive comes from the impact that business strategies can have on society at large. Emily is passionate about incorporating sustainability into business models and strives to make a significant impact on the corporate world and society.

    Emily's primary motivators are intellectual growth, challenge, and the potential to make a difference. She is driven by the chance to learn something new every day and to challenge herself in different ways. She draws inspiration from the prospect of contributing to society positively through her business skills and acumen.

    Emily is deeply inspired by Indra Nooyi, former CEO of PepsiCo, for her transformational leadership and emphasis on sustainability and corporate responsibility. She often refers to Nooyi's mantra of "Performance with Purpose," which aligns closely with Emily's personal and professional aspirations.
    """
    prompt = profile + "\n\nBased on this profile, write a LinkedIn post that Emily might write, related to business, that could inspire, educate, or inform others in her network."
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
