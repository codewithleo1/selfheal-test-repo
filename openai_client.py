import openai


def generate_text(prompt: str, max_tokens: int = 100) -> str:
    """Generate text — uses deprecated v0 OpenAI API."""
    response = openai.Completion.create(
        engine="text-davinci-003",  # deprecated engine
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


def get_embedding(text: str) -> list:
    """Get text embedding — uses deprecated endpoint."""
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002",  # deprecated model
    )
    return response["data"][0]["embedding"]
