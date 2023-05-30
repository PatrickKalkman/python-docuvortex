# Harnessing the Vortex: Building a Document-Based Q&A System Using OpenAI and Python

## Leveraging the Power of Large Language Models and the Langchain Framework for an Innovative Approach to Document Querying

![DocuVortex](/vortex.png "DocuVortex")


This project aims to implement a document-based question-answering system using the power of OpenAI's GPT-3.5 Turbo model, Python, and the Langchain Framework. It processes PDF documents, breaking them into ingestible chunks, and then stores these chunks into a Chroma DB vector database for querying. It complements a Medium article called [Howto Build a Document-Based Q&A System Using OpenAI and Python](https://medium.com/itnext/how-to-build-a-document-based-q-a-system-using-openai-and-python-17d1c3cc2081).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To install the project, you need to have [Python](https://www.python.org/downloads/) installed on your machine.

### Installing

The project uses [Poetry](https://python-poetry.org/) for managing dependencies. After cloning the repository, navigate to the project directory and install dependencies with the following commands:

```bash
poetry install
poetry shell
```

## Running the Application
Before you can run ingesting or querying you have to make sure that a .env file exists. This file should have a single line that read ```OPENAI_API_KEY=yourkey```

### Ingesting Documents
To ingest documents, place your PDF files in the 'docs' folder make sure that you are in the app folder and run the following command:

```bash
cd app
python ingest.py
```

### Querying Documents
To query the ingested documents, make sure that you are in the app folder, run the following command and follow the interactive prompts:

```bash
cd app
python query.py
```

### Running the Streamlit App
To visualize and interact with the system via the Streamlit app, run the following command:

```bash
streamlit run streamlit_app.py
```

### Authors
[Patrick Kalkman](https://github.com/PatrickKalkman)

### License
This project is licensed under the MIT license - see the LICENSE.md file for details

### Acknowledgments
- [Langchain Framework](https://python.langchain.com/en/latest/index.html)
- [OpenAI](https://openai.com/)
- [Chroma DB](https://www.trychroma.com/)
- [Streamlit](https://streamlit.io/)


