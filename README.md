# Summify

**Summify** is a web application designed to generate concise and coherent summaries of research papers, making complex academic content more accessible and easier to understand. The app is built using the T5 model and lexrank algorithm, and provides users with customizable options for summary length and input formats, such as text input, URLs, and PDF/Word documents.

## Features

- **Customizable Summary Length:** Users can choose the desired length of the summary.
- **Multiple Input Formats:** Supports direct text input, URLs, and document uploads (PDF/Word).
- **Advanced Metrics for Summary Quality:** Includes ROUGE scores, Flesch Reading Ease, and Gunning Fog Index to ensure readability and accuracy of the summaries.

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** Streamlit, HTML, CSS
- **NLP Models:** T5 (Text-to-Text Transfer Transformer)
- **Other Libraries:** Transformers, Pandas, Numpy

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/Shivam093/Summify-E.git
```

### Install the Required Libraries

Install the necessary dependencies using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Run the Application

You can run the application using Flask or Streamlit.

#### Running with Flask

```bash
flask run
```

#### Running with Streamlit

```bash
streamlit run app.py
```

## Usage

1. **Upload Your Document:** You can input a research paper by uploading a PDF/Word document, entering a URL, or pasting the text directly.
2. **Customize Summary Length:** Choose the desired length of your summary.
3. **Generate Summary:** Click the "Summarize" button to generate a summary.
4. **View Quality Metrics:** Review the generated summary along with ROUGE scores, Flesch Reading Ease, and Gunning Fog Index for readability and accuracy.

## Future Enhancements

- **Hybrid Models:** Investigate the combination of BART and T5 models for improved summarization.
- **Context-Aware Summarization:** Incorporate linguistic features and context-awareness to enhance the coherence of generated summaries.
- **Multi-Document Summarization:** Extend the application to handle summarization of multiple documents simultaneously.
- **Video-to-Text Summarization:** Explore summarization of video content into text format.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.

---
