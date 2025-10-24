import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

def chunk_sentence(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    # Define grammar for chunking
    grammar = r"""
    NP: {<DT|JJ|NN.*>+} # Chunk sequences of DT, JJ, NN
    PP: {<IN><NP>} # Chunk prepositions followed by NP
    VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
    CLAUSE: {<NP><VP>} # Chunk NP, VP pairs
    """
    parser = RegexpParser(grammar)
    chunked_sentence = parser.parse(tagged_words)
    return chunked_sentence

sentence = "The quick brown fox jumps over the lazy dog"
chunked_sentence = chunk_sentence(sentence)
print(chunked_sentence)