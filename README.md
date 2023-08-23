# Text Summarization App

This Streamlit web application allows you to input paragraphs of text and generate summaries for each individual paragraph using the LaMini-Flan-T5-248M model.

## Overview

This application provides an intuitive interface for users to input text containing multiple paragraphs. It then processes the input and generates concise summaries for each paragraph. The model used for summarization is LaMini-Flan-T5-248M, and the application utilizes the Transformers library for natural language processing.

## Features

- **Input Text:** Users can enter paragraphs of text directly into the provided text area.

- **Summarization:** Upon clicking the "Summarize" button, the application generates summaries for each paragraph using the T5 model.

- **Two-Column Display:** The interface displays the input paragraphs and their corresponding summaries side by side for easy comparison.

## Prerequisites

- Python 3.6+
- Streamlit
- Transformers library

You can install the required dependencies using the following command:
```bash
pip install streamlit transformers torch
```

<br>

**Note**: To run the application, you have two options:

1.  **Download LaMini-Flan-T5-248M**: You can download the LaMini-Flan-T5-248M model checkpoint from the Hugging Face model hub and place it in the appropriate directory. Update the checkpoint variable in the app.py file with the correct path to the model checkpoint.

2. **Use Hugging Face Pipeline**: If you don't want to download the model manually, the application uses the Hugging Face pipeline to fetch the model online. This requires an active internet connection during usage.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/Shoaib-Alauudin/Text-Summarization-Using-LLM.git

    cd Text-Summarization-Using-LLM
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4. Input your paragraphs in the provided text area and click the "Summarize" button to view the generated summaries.


## License
This project is licensed under the MIT License

## Acknowledgments
* The **LaMini-Flan-T5-248M** was fine tune by *Muhammad bin zaid University of Artificial Intelligence* on Top of **Text-To-Text Transfer Transformer (T5)**, which is a large language model develop by Google.

* This project was created as part of a [Streamlit](https://streamlit.io) tutorial to showcase text summarization capabilities.


Feel free to contribute, report issues, or suggest improvements by opening an issue or pull request!