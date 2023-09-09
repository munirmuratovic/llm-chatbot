from typing import Union
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from gpt4all import GPT4All
from functools import lru_cache
from utils.functions import *
from utils.prompting import *
from models.llms import *

app = FastAPI()


@app.get("/")
def read_chat():
    model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
    output = model.generate("The capital of France is ", max_tokens=3)
    return {"output": output}


@app.post("/default")
def post_chat(request):
    model = chooseModel[request.model]
    model.chat_session(system_prompt=SYSTEM_PROMPT, prompt_template=PROMPT_TEMPLATE)
    result = model.generate(
        prompt=format_prompt(request.messages[-1].content),
        temp=0.1,
        streaming=True,
        max_tokens=100,
    )

    message = get_message_from_stream(result)
    response_object = create_response_object(message, request.model)

    return response_object


@app.post("/stream")
def post_chat(request):
    model = chooseModel[request.model]
    model.chat_session(system_prompt=SYSTEM_PROMPT, prompt_template=PROMPT_TEMPLATE)
    result = model.generate(
        prompt=format_prompt(request.messages[-1].content),
        temp=0.1,
        streaming=True,
        max_tokens=100,
    )

    wrapped_stream = wrap_messages_into_chunks(result)
    return StreamingResponse(wrapped_stream, media_type="text/plain")
