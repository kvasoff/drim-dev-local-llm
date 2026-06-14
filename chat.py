import time
from openai import OpenAI

PROVIDERS = {
    "ollama": {
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "model": "qwen3:8b",
    },
    "lmstudio": {
        "base_url": "http://localhost:1234/v1",
        "api_key": "lm-studio",
        "model": "qwen/qwen3.5-9b",
    },
}


def ask(question, provider="lmstudio"):
    cfg = PROVIDERS[provider]
    client = OpenAI(base_url=cfg["base_url"], api_key=cfg["api_key"])

    start = time.time()

    response = client.chat.completions.create(
        model=cfg["model"],
        messages=[{"role": "user", "content": question}],
    )

    elapsed = time.time() - start

    answer = response.choices[0].message.content

    if response.usage and response.usage.completion_tokens:
        tps = response.usage.completion_tokens / elapsed
        print(f"\n Скорость: {tps:.1f} токенов/сек")

    return answer


while True:
    print(ask(input("Вы: ")), "\n")
