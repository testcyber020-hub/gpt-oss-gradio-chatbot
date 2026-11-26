# GPT-OSS 120B Streaming Chatbot

An interactive AI chatbot built with **Python, Gradio, OpenRouter API, and GPT-OSS 120B**. This project demonstrates how to integrate an open-weight Large Language Model (LLM) into a conversational application using the OpenAI Python SDK and real-time streaming responses.

The chatbot is designed as an LLM Engineering learning project, focusing on API integration, prompt engineering, conversation history, and streaming inference.

## Project Overview

This application allows users to interact with GPT-OSS 120B through a simple web-based chat interface powered by Gradio.

Instead of waiting for the entire response to be generated, the application uses streaming to display generated text progressively as it arrives from the model.

## Features

- **LLM Integration:** Connects GPT-OSS 120B through OpenRouter API.
- **Streaming Responses:** Displays model responses progressively using Python generators and `yield`.
- **Conversation History:** Maintains previous messages to provide conversational context.
- **System Prompt:** Uses custom instructions to guide the AI as an LLM Engineering tutor.
- **Model Parameters:** Configurable temperature, top-p, and maximum output tokens.
- **Interactive UI:** Provides a user-friendly chatbot interface using Gradio.
- **Environment Variables:** Uses `.env` to securely manage API credentials.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Gradio | Chat interface |
| OpenRouter | LLM API provider |
| GPT-OSS 120B | Language model |
| OpenAI Python SDK | API communication |
| python-dotenv | Environment variable management |

## Application Architecture

The application follows a simple request-response workflow:

```text
        User
         |
         v
   Gradio Chat Interface
         |
         v
    Python Function
         |
         v
  Conversation History
         |
         v
    OpenRouter API
         |
         v
     GPT-OSS 120B
         |
         v
   Streaming Chunks
         |
         v
    Gradio Interface
         |
         v
       User
```

## Project Structure

```text
gpt-oss-gradio-chatbot/
│
├── app.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd gpt-oss-gradio-chatbot
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a Virtual Environment

Using Python:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key

Create a `.env` file in the project root directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Get your API key from [OpenRouter](https://openrouter.ai/keys).

**Important:** Never upload your actual `.env` file or API key to GitHub.

### 5. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:7860
```

## Understanding Streaming Responses

This project uses the streaming capability of the OpenAI-compatible API.

The following parameter enables streaming:

```python
stream=True
```

The application receives response chunks progressively:

```python
for chunk in response:

    if not chunk.choices:
        continue

    content = chunk.choices[0].delta.content

    if content:
        answer += content
        yield answer
```

The `yield` statement allows Gradio to display the growing response without waiting for the complete model output.

This demonstrates an important concept in LLM application development: streaming inference and incremental response delivery.

## Model Configuration

The application uses the following model configuration:

```python
model="openai/gpt-oss-120b"
temperature=0.3
top_p=0.9
max_tokens=1000
stream=True
```

These parameters control model selection, response generation behavior, output length, and response delivery.

## Learning Objectives

This project explores practical LLM Engineering concepts:

1. Understanding OpenAI-compatible API integration.
2. Connecting open-weight language models through OpenRouter.
3. Implementing system prompts.
4. Managing conversational context.
5. Understanding streaming responses.
6. Building interactive AI applications with Gradio.
7. Managing API credentials using environment variables.

## Future Improvements

Planned enhancements include:

- [ ] Add model selection.
- [ ] Add adjustable temperature and top-p controls.
- [ ] Display token usage and API cost.
- [ ] Measure response latency and time to first token (TTFT).
- [ ] Add conversation export.
- [ ] Improve error handling and API status feedback.
- [ ] Deploy the application online.

## Author

**Boniphace Boaz**

Aspiring LLM Engineer | AI Engineering Learner

Interested in Large Language Models, AI applications, open-source models, and Agentic AI.

---

*Built as part of my practical journey into LLM Engineering.*

