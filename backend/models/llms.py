from functools import lru_cache
from gpt4all import GPT4All


@lru_cache
def get_llama2_model():
    return GPT4All("llama-2-7b-chat.ggmlv3.q4_0.bin")


chooseModel = {
    "llama2": get_llama2_model(),
}
