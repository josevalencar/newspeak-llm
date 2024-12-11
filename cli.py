import os
import openai
from pathlib import Path

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import FunctionTool
from llama_index.core import SimpleDirectoryReader
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# query_engine_tool = QueryEngineTool(
#     query_engine=index.as_query_engine(),
#     metadata=ToolMetadata(
#         name="newspeak_index",
#         description="Your task is to translate english phrases to newspeak, or newspeak to english accordingly to the given context."
#     ),
# )

# agent = OpenAIAgent.from_tools(
#     tools=[query_engine_tool],
#     llm=OpenAI(model="gpt-4"),
#     verbose=False
# )

query_engine=index.as_query_engine()

print("Welcome to the Newspeak Translator Chatbot! Type 'exit' or 'quit' to end the conversation.\n")

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye!")
        break
    # response = agent.chat(user_input)
    response = query_engine.query(user_input)
    print(f"Agent: {response}")
