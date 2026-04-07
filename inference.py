import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run_agent(task):

    print("[START] AI Gold Detection Task")

    print("[STEP] scanning environment")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an AI system that analyzes metal scan results."},
            {"role": "user", "content": task}
        ]
    )

    result = response.choices[0].message.content

    print("[STEP] AI analysis complete")

    print("[END] Task finished")

    return result


if __name__ == "__main__":
    task = "Scan environment and determine if gold is present"
    output = run_agent(task)
    print(output)
