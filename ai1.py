
import streamlit as st
from datetime import datetime
import requests
import json
from calllm import callOLLAMA
from prompt import prompt

st.set_page_config(
    page_title="Chatbot"
)

if "messages" not in st.session_state:
    st.session_state.messages =[]
    st.session_state.messages.append(
           {
               "role":"assistant",
               "content":"Hey,how can i help you? "
           }
        )
    
if "is_typing" not in st.session_state:
    st.session_state.is_typing=False

st.title("EA Chatbot") 
st.markdown("Welcome to this session")
st.subheader("Chat here! ")
#to distinguish user and ai text
for message in st.session_state.messages:
    if message["role"]=="user":
        st.info(message["content"])
    else:
        st.success(message["content"])

if st.session_state.is_typing:
    st.markdown("Bot is typing")
    st.warning("Typing....")


st.markdown("---")
st.subheader("Your message")

with st.form(key="chat_form",clear_on_submit=True):
    user_input=st.text_input(
        "Type your message",
        placeholder="Ask me anything"
    )
    send_button=st.form_submit_button("send message",type="primary")


col1 ,col2=st.columns([1,1])
with col1:
    clear_button=st.button("Clear chat")

if send_button and user_input.strip():
    #store user message variable seperate
    st.session_state.messages.append(
        {
           "role":"user",
           "content":user_input.strip()
        }
    )
    #store full message with prompt to pass to llm
    st.session_state.full_user_message=f"{prompt}<|>{user_input.strip()}"
    st.session_state.is_typing=True
    st.rerun()

if st.session_state.is_typing:
    full_user_message=st.session_state.full_user_message
    bot_response=callOLLAMA(full_user_message)
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":bot_response
        }
    )
    st.session_state.is_typing=False
    st.rerun()