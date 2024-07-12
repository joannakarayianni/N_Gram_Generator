import nltk

def tokenize(text):
# Lower the characters, split individual tokens and return result as a list
    word_tokens = nltk.word_tokenize(text.lower())
    
    return word_tokens

def detokenize(tokens):
# Take separated tokens and merges them using a whitespace as a separator
    detokenized_text = ' '.join(tokens)
# Create sentences based on punctuation marks and capitalize first letter at each sentence after punctuation mark
    sentences = nltk.sent_tokenize(detokenized_text)
    detokenized_text = ' '.join(sentence.capitalize() for sentence in sentences)
    
    return detokenized_text

# Testing functions:
'''text = "I love sleeping, and kittens. But I don't care! This is Anne's party ..."
tokens = tokenize(text)
print("Tokenized Text:", tokens)
detokenized_text = detokenize(tokens)
print("Detokenized Text:", detokenized_text)'''

