# Newspeak LLM

![Newspeak LLM](static/image.png)

Newspeak LLM is a simple chatbot application designed to translate between English (Oldspeak) and Newspeak, the fictional language introduced in George Orwell's *1984*, using RAG (Retrieval-Augmented Generation). This project uses llama-index tools to process and analyze text in the context of Newspeak principles and offers a conversational interface through CLI and Streamlit.


## Features

- **Translation Between English and Newspeak**: Facilitates translation with contextual accuracy.
- **Conversational Interface**: Offers both a CLI-based and a Streamlit-based chatbot interface for interaction.
- **Document Processing**: Reads and indexes documents for dynamic query responses.
- **Persistent Storage**: Uses vector stores and indexed storage for efficient data retrieval.

## Project Structure

```plaintext
📂 newspeak-llm
├── 📂 __pycache__
├── 📂 data
│   └── newspeak.pdf  # Document containing Newspeak principles
├── 📂 static
│   └── image.pnf  # Image used for the README.md
├── 📂 storage
│   ├── default__vector_store.json
│   ├── docstore.json
│   ├── graph_store.json
│   ├── image__vector_store.json
│   └── index_store.json
├── 📂 venv           # Python virtual environment
├── .env              # Environment variables (e.g., OpenAI API Key)
├── .gitignore        # Git ignore file
├── cli.py            # CLI-based chatbot script
├── requirements.txt  # Python dependencies
└── streamlit.py      # Streamlit-based chatbot web app
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd Newspeak-LLM
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set OpenAI API Key**:
   Create a `.env` file in the root directory with the following content:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### CLI Interface
Run the chatbot in the terminal:
```bash
python cli.py
```
Interact with the chatbot to translate phrases between English and Newspeak.

### Streamlit Interface
Launch the web application:
```bash
streamlit run streamlit.py
```
Open the Streamlit app in your browser and interact via the chat interface.

### Processing New Documents
Place additional documents in the `data` directory. The system will automatically process and index them.

## Example Interactions

**CLI Interaction**:
```plaintext
Welcome to the Newspeak Translator Chatbot! Type 'exit' or 'quit' to end the conversation.

User: Translate "freedom is slavery."
Agent: In Newspeak: "crimethink doubleplusungood."
```

**Streamlit Interaction**:
Input a phrase and receive a translation directly on the web app.

## Project Context

This project leverages principles from George Orwell’s *1984*, specifically the concept of Newspeak, to highlight the nuances of language manipulation. The `newspeak.pdf` file included in the `data` directory serves as a reference for the implementation.

## Dependencies

The dependencies are managed in `requirements.txt`. Notable libraries include:
- **OpenAI**: GPT-4-based natural language model.
- **Streamlit**: Interactive UI for chatbot interaction.
- **LlamaIndex**: Document processing and vector-based indexing.
- **dotenv**: For managing environment variables.

## Contribution

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit changes and open a pull request.

Ensure your code adheres to the following:
- Clear documentation.
- Proper testing for new features.
- Compatibility with the existing project structure.
