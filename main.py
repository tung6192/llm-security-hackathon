from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="",  # leave your key here
    api_version="",
    azure_endpoint=""
)

deployment_name = "gpt-35-turbo"

# Please only use this one if you absolutely need it. It's slower and more expensive.
# deployment_name = "gpt-4"
# deployment_name = "gpt-4-32k"

# For embeddings only, but small private models may perform better and cheaper
# https://huggingface.co/spaces/mteb/leaderboard
# deployment_name = "text-embedding-ada-002"


print(client.chat.completions.create(
    model=deployment_name,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": "how are you?",
        },
    ],
))