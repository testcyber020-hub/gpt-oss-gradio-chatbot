
import os
import gradio as gr

from openai import OpenAI
from dotenv import load_dotenv


# 1. Load environment variables
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError(
        "OPENROUTER_API_KEY haijapatikana kwenye .env file"
    )


# 2. Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


# 3. Define system prompt
SYSTEM_PROMPT = """
You are an AI tutor specializing in LLM Engineering.

Teach beginners using simple English.
Give practical Python examples.
Avoid unnecessary complexity.
Explain technical concepts step by step.
"""


# 4. Define chatbot function with Streaming
def chat(message, history):

    # Build conversation messages
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Add previous conversation history
    messages.extend(history)

    # Add current user message
    messages.append({
        "role": "user",
        "content": message
    })

    try:
        # 5. Send streaming request to GPT-OSS 120B
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            temperature=0.3,
            top_p=0.9,
            max_tokens=1000,
            stream=True
        )

        # 6. Receive and display tokens progressively
        answer = ""

        for chunk in response:

            if not chunk.choices:
                continue

            content = chunk.choices[0].delta.content

            if content:
                answer += content

                # Send updated response to Gradio
                yield answer

    except Exception as e:
        yield f"Error: {str(e)}"


# 7. Create Gradio Chat Interface
demo = gr.ChatInterface(
    fn=chat,

    title="LLM Engineering Tutor AI",

    description=(
        "Chat with an AI tutor powered by "
        "GPT-OSS 120B through OpenRouter API."
    ),

    chatbot=gr.Chatbot(
        height=500,
        placeholder="Ask me anything about LLM Engineering..."
    ),

    textbox=gr.Textbox(
        placeholder="Type your question here...",
        container=False
    )
)


# 8. Launch application
if __name__ == "__main__":
    demo.launch()
