import nltk
nltk.download('punkt') # Download the necessary tokenization models
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
def tokenize_words(text):
    words = word_tokenize(text)
    return words
# Example text
text = "NLTK is a leading platform for building Python programs to work with human language data."
# Tokenize words
words = tokenize_words(text)
# Print tokenized words
print(words)