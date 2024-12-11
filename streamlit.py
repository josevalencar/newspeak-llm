import os
from pathlib import Path
import streamlit as st
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core import SimpleDirectoryReader
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()

st.write("Newspeak Translator Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter text to translate between English and Newspeak:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # response = query_engine.query("You're a chatbot and your task is to answer questions about Newspeak, accordingly with the given context. Answer: " + prompt)
        response = query_engine.query(prompt)
        st.markdown(str(response))

    st.session_state.messages.append({"role": "assistant", "content": str(response)})
