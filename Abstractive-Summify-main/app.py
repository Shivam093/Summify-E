import streamlit as st
from PyPDF2 import PdfReader
from transformers import BartForConditionalGeneration, BartTokenizer, pipeline
import docx

# model_name = "facebook/bart-large-cnn"  # Example model name
# custom_max_position_embeddings = 2048  # Example value
# tokenizer = BartTokenizer.from_pretrained(model_name)
# model = BartForConditionalGeneration.from_pretrained(
#     model_name,
#     max_position_embeddings=custom_max_position_embeddings,
# )

# summarizer = pipeline("summarization", model=model, tokenizer= tokenizer)
st.set_page_config(layout="wide")
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

@st.cache_resource
def text_summary(text, maxlength=None):
    #create summary instance
    length= int(0.07*len(text))
    result = summarizer(text,max_length=250, min_length=length, do_sample=False)
    return result

def extract_text_from_pdf(file_path):
    text=""
    # Open the PDF file using PyPDF2
    if file_path.endswith('.pdf'):
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            # page = reader.pages[0]
            # text = page.extract_text()
            for page in reader.pages:
                text += page.extract_text()
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text +"\n"
    return text

choice = st.sidebar.selectbox("Select your choice", ["Summarize Text", "Summarize Document"])

if choice == "Summarize Text":
    st.subheader("Summarize Text using T5 (Text to Text Transer Transformer)")
    input_text = st.text_area("Enter your text here")
    if input_text is not None:
        if st.button("Summarize Text"):
            col1, col2 = st.columns([1,1])
            with col1:
                st.markdown("**Your Input Text**")
                st.info(input_text)
            with col2:
                st.markdown("**Summary Result**")
                result = text_summary(input_text)
                st.success(result)

elif choice == "Summarize Document":
    st.subheader("Summarize Document using T5 (Text to Text Transer Transformer)")
    input_file = st.file_uploader("Upload your document here", type=['pdf', 'docx'])
    if input_file is not None:
        if input_file.name.endswith('.pdf'):
            file_type = 'pdf'
            with open("doc_file.pdf", "wb") as f:
                f.write(input_file.getbuffer())
            extracted_text = extract_text_from_pdf("doc_file.pdf")
        elif input_file.name.endswith('.docx'):
            file_type = 'docx'
            with open("doc_file.docx", "wb") as f:
                f.write(input_file.getbuffer())
            extracted_text = extract_text_from_pdf("doc_file.docx")
        col1, col2 = st.columns([1,1])
        with col1:
            st.info("File uploaded successfully")
            st.markdown("**Extracted Text is Below:**")
            st.info(extracted_text)
        with col2:
            st.markdown("**Summary Result**")
            doc_summary = text_summary(extracted_text)
            st.success(doc_summary)
                
