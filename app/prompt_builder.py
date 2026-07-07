# Prompt engineering logic
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from app.logger import logger
import time

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

    logger.info("=" * 60)
    logger.info("Invoking Azure OpenAI...")
    logger.info(f"Question Length : {len(question)} characters")
    logger.info(f"Context Length : {len(context)} characters")
    logger.info(f"Prompt Length : {len(prompt)} characters")

    start = time.time()
    response = llm.invoke(prompt)
    end = time.time()

    logger.info(f"Response Time : {end-start:.2f} sec")

    # Token Usage
    usage = response.response_metadata.get("token_usage", {})

    if usage:
        logger.info(f"Prompt Tokens : {usage.get('prompt_tokens')}")
        logger.info(f"Completion Tokens : {usage.get('completion_tokens')}")
        logger.info(f"Total Tokens : {usage.get('total_tokens')}")
    else:
        logger.warning("Token usage metadata not available.")

    logger.info("=" * 60)
    logger.info("Final Response")
    logger.info(response.content)
    logger.info("Azure OpenAI Response Completed")

    return {
        "answer": response.content,
        "performance_metrics": {
            "prompt_tokens": usage.get("prompt_tokens"),
            "completion_tokens": usage.get("completion_tokens"),
            "total_tokens": usage.get("total_tokens"),
            "llm_response_time": round(end - start, 2)
        }
    }