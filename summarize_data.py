import openai
import os

# Summarize a single article
def summarize_article(article_text, api_key, max_tokens=100):
    openai.api_key = os.getenv("open_ai_key")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the article."},
                {"role": "user", "content": f"Article: {article_text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating summary: {e}"

# Test the function if run directly
if __name__ == "__main__":
    test_article = "OpenAI has introduced new advancements in AI technology to help automate tasks like summarizing text."
    OPENAI_API_KEY = "your-openai-api-key-here"  # Replace with your OpenAI key for testing
    print(summarize_article(test_article, OPENAI_API_KEY))
