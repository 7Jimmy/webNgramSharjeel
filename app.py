import streamlit as st
from nltk import ngrams
from nltk.tokenize import word_tokenize
# app.py

def main():
    st.title("N-gram Extractor")

    # Get user input
    text_input = st.text_area("Enter your text:")

    # Choose n for n-grams
    n_value = st.slider("Select n for n-grams:", min_value=2, max_value=5)

    if st.button("Extract N-grams"):
        # Process the text and extract n-grams
        n_grams = extract_ngrams(text_input, n_value)

        # Display the results
        st.write(f"{n_value}-grams:")
        st.write(n_grams)


def extract_ngrams(text, n):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Generate n-grams using NLTK
    n_grams = list(ngrams(tokens, n))

    # Convert n-grams to strings for display
    n_grams_str = [' '.join(gram) for gram in n_grams]

    return n_grams_str


if __name__ == "__main__":
    main()

import nltk

nltk.download('punkt')

