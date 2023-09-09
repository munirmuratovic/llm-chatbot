B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

DEFAULT_SYSTEM_PROMPT = """
You are helpful, respectful and honest assistant.
"""

SYSTEM_PROMPT = B_SYS + DEFAULT_SYSTEM_PROMPT + E_SYS
PROMPT_TEMPLATE = "[INST] {0} [/INST]"

def format_prompt(instruction: str):
    prompt_template = B_INST + SYSTEM_PROMPT + instruction + E_INST
    return prompt_template
