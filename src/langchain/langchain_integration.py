import os

import chainlit as cl
import openai
from langchain import LLMChain
from langchain import OpenAI
from langchain import PromptTemplate


openai.api_key = os.environ["OPENAI_API_KEY"]


template = """
    Question: {question}

    Answer: Let's think step by step.
    """

print(template.format(question="What's 1234?"))


@cl.on_chat_start
def start():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(
        prompt=prompt,
        llm=OpenAI(temperature=1, streaming=True),
        verbose=True,
    )
    cl.user_session.set(key="llm_chain", value=llm_chain)


@cl.on_message
async def main(message: str):
    llm_chain = cl.user_session.get(key="llm_chain")
    result = await llm_chain.acall(
        message, callbacks=[cl.AsyncLangchainCallbackHandler()]
    )
    await cl.Message(content=result["text"]).send()
