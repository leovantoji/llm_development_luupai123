import os

import chainlit as cl
import openai


openai.api_key = os.environ["OPENAI_API_KEY"]


@cl.on_message
async def main(message: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "assistant",
                "content": "you are a helpful assistant using only rude language",
            },
            {
                "role": "user",
                "content": message,
            },
        ],
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    await cl.Message(content=response["choices"][0]["message"]["content"]).send()
