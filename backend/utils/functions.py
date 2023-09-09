import datetime
import json


def create_new_chunk(content_chunk: str, model: str) -> str:
    new_chunk = {
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "content": content_chunk,
    }

    return json.dumps(new_chunk).encode("utf-8") + b"\n"


def wrap_messages_into_chunks(stream, model: str):
    for message in stream:
        new_message = create_new_chunk(message, model)
        yield f"data: {new_message.decode('utf-8')}\n"


def get_message_from_stream(stream):
    res = ""
    for message in stream:
        res += message
    return res


def create_response_object(message: str, model: str):
    return {
        "message": message,
        "model": model,
    }
