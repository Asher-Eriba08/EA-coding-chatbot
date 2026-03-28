EA Chatbot

EA Chatbot is a simple AI-powered chatbot built using Streamlit that interacts with a local LLM via Ollama. Users can chat in real-time, and the bot responds with concise, helpful answers.

Features
Real-time chat interface with user and AI messages clearly distinguished
Local LLM integration via Ollama (deepseek-r1:1.5b model)
Handles connection errors and long response times gracefully
Clear and simple responses — no unnecessary explanations

Technologies Used
Python
Streamlit
Requests library for API calls
Ollama LLM

Setup Instructions
1.Clone the repository:
git clone https://github.com/Asher-Eriba08/EA-coding-chatbot
cd EA-coding-chatbot

2.Install Python dependencies:
pip install streamlit requests

3.Install Ollama
Download and install Ollama from https://ollama.com
Make sure it is running locally.

4.Install the DeepSeek model:
ollama pull deepseek-r1:1.5b
This downloads the model locally so the chatbot can use it.

5.Run the chatbot:
streamlit run ai.py

Usage
Type your message in the input box and press Send.
Click Clear chat to reset the conversation.

Notes
Responses are limited to 250 tokens for concise answers.
Adjust the temperature parameter in callOLLAMA() for more creative responses.
