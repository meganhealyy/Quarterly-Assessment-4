
import openai

def summarize_article(articles, open_ai_key):
    """
    Summarizes a list of articles using OpenAI's GPT-3.5 API.

    Parameters:
    articles (list): A list of articles to summarize.
    open_ai_key (str): The API key for OpenAI.

    Returns:
    list: A list of summaries or an empty list if an error occurs.
    """
    # Set the OpenAI API key
    openai.api_key = open_ai_key

    summaries = []
    for article in articles:
        title = article.get("title", "No title")
        description = article.get("description", "No description available")

        # Prepare the prompt for GPT-3.5
        prompt = f"Summarize the following article: \n\nTitle: {title}\nDescription: {description}"

        try:
            # Call the OpenAI API to get a summary using a newer model (gpt-3.5-turbo)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use the newer model
                messages=[{"role": "system", "content": "You are a helpful assistant."},
                          {"role": "user", "content": prompt}],
                max_tokens=150,  # You can adjust the token limit based on your needs
                temperature=0.7,
            )

            # Extract the summary from the response
            summary = response['choices'][0]['message']['content'].strip()
            summaries.append(summary)

        except openai.error.OpenAIError as e:
            # If there's an error with the OpenAI API request, print the error and append a default message
            print(f"Error summarizing article: {e}")
            summaries.append("Error summarizing the article")

    return summaries
