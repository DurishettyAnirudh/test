import nltk
nltk.download('punkt')  # Download the necessary tokenization models
nltk.download('punkt_tab') # Download the punkt_tab resource
from nltk.tokenize import sent_tokenize


def tokenize_sentences(text):
        """Return a list of sentences for the given text."""
        sentences = sent_tokenize(text)
        return sentences


# Example text (kept as a single logical string using implicit concatenation)
text = (
        "NLTK is a leading platform for building Python programs to work with human language data. It "
        "provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a "
        "suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic "
        "reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum."
)


# Tokenize sentences
sentences = tokenize_sentences(text)


# Print tokenized sentences
for i, sentence in enumerate(sentences):
        print(f"Sentence {i+1}: {sentence}")