from typing import Union
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from gpt4all import GPT4All
from functools import lru_cache
from utils.functions import *
from utils.prompting import *
from models.llms import *

app = FastAPI()


@app.post("/default")
def post_chat(request):
    model = chooseModel["llama2"]
    model.chat_session(system_prompt=SYSTEM_PROMPT, prompt_template=PROMPT_TEMPLATE)
    result = model.generate(
        prompt=format_prompt(request),
        temp=0.1,
        streaming=False,
        max_tokens=400,
    )

    return result


@app.post("/stream")
def post_chat(request):
    model = chooseModel["llama2"]
    model.chat_session(system_prompt=SYSTEM_PROMPT, prompt_template=PROMPT_TEMPLATE)
    result = model.generate(
        prompt=format_prompt(request),
        temp=0.1,
        streaming=True,
        max_tokens=100,
    )

    wrapped_stream = wrap_messages_into_chunks(result)
    return StreamingResponse(wrapped_stream, media_type="text/plain")
