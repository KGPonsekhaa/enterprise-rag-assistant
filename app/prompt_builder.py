# Prompt engineering logic
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    temperature=0
)


def generate_response(context, question):

    prompt = f"""
    You are an enterprise AI assistant.
    Answer ONLY from the provided context.
    If answer is not available in context,
    say:
    'Answer not found in provided documents.'

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)
    return response.content