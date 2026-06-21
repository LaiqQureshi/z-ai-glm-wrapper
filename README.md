# Z AI GLM 5.2 Universal Wrapper

A simple, easy-to-use Python wrapper for interacting with Z AI's GLM 5.2 model. 
It handles the complicated internet requests for you so you can just focus on your prompts!

## How to Install

Make sure you have Python installed on your computer. Then, download this code.

## How to Use

Here is a quick example of how to use this wrapper in your own Python code:

```python
from glm_wrapper import ZAIClient

# 1. Put your actual Z AI API key here
client = ZAIClient(api_key="your_api_key_here")

# 2. Ask the AI a question!
response = client.chat("Explain quantum computing in one simple sentence.")

# 3. Print the answer
print(response)
