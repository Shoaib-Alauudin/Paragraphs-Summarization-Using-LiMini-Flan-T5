import streamlit as st 
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import pipeline
import torch

#model and tokenizer loading
checkpoint = "LaMini-Flan-T5-248M"
tokenizer = T5Tokenizer.from_pretrained(checkpoint)
base_model = T5ForConditionalGeneration.from_pretrained(checkpoint, device_map='auto', torch_dtype=torch.float32)


def paragraph_summarization(input_text):
    paragraphs = input_text.split('\n\n')  # Split text into paragraphs
    summary_pipeline = pipeline(
        'summarization',
        model=base_model,
        tokenizer=tokenizer,
        max_length=300,  # Adjust max_length as needed for paragraph summaries
        min_length=30)   # Adjust min_length as needed

    summaries = []
    for paragraph in paragraphs:
        if len(paragraph.strip()) > 0:
            summary = summary_pipeline(paragraph)[0]['summary_text']
            summaries.append(summary)
    
    return summaries


#streamlit code 
st.set_page_config(layout="wide")

def main():
    st.title("Paragraph Summarization App")

    # user input text
    input_text = st.text_area("Enter your paragraphs here:", "", )

    if st.button("Summarize"):
        col1, col2 = st.columns(2)

        with col1:
            st.info("Written paragraphs")
            st.write(input_text)
            #pdf_viewer = displayPDF(filePath)

        with col2:
            st.info("Summarized paragraphs")
            summaries = paragraph_summarization(input_text)
            for i, summary in enumerate(summaries):
                st.success(f"Summary for Paragraph {i+1}: {summary}")



if __name__ == "__main__":
    main()