# Harnessing the Vortex: Building a Document-Based Q&A System Using OpenAI and Python

## Leveraging the Power of Large Language Models and the Langchain Framework for an Innovative Approach to Document Querying

This project aims to implement a document-based question-answering system using the power of OpenAI's GPT-3.5 Turbo model, Python, and the Langchain Framework. It processes PDF documents, breaking them into ingestible chunks, and then stores these chunks into a Chroma DB vector database for querying. It complements a Medium article called ().

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To install the project, you need to have [Python](https://www.python.org/downloads/) installed on your machine.

### Installing

The project uses [Poetry](https://python-poetry.org/) for managing dependencies. After cloning the repository, navigate to the project directory and install dependencies with the following commands:

```bash
poetry shell
poetry install
```

### Running the Application
Ingesting Documents
To ingest documents, place your PDF files in the 'docs' folder and run the following command:

```bash
Copy code
python ingest.py
```

### Querying Documents
To query the ingested documents, run the following command and follow the interactive prompts:

```
bash
Copy code
python query.py
```

### Running the Streamlit App
To visualize and interact with the system via the Streamlit app, run the following command:

```bash
Copy code
streamlit run streamlit_app.py
```

### Authors
[Patrick Kalkman](Your GitHub link)

### License
This project is licensed under the MIT license - see the LICENSE.md file for details

### Acknowledgments
- Langchain Framework
- OpenAI
- Chroma DB
- Streamlit


