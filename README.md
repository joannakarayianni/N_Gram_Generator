# N-Gram Generator
Final project of the programming in python class.

I built a program that can learn statistical patterns from text and use those patterns to predict the likelihood of certain words following others. 

The program consists of three parts:
1. Corpus Handling (corpus.py): Reads text files, breaks them down into individual words (tokens), and optionally puts those words back together into a single piece of text.

2. Language Model Core (lm.py): Trains on the provided text data, learning how often sequences of words (n-grams) appear together. Then, it predicts the probability of the next word in a sequence and generates new text that statistically resembles the training data.

3. User Interface (main.py): Allows users to interact with the program. Users are able to create the language model, specifying the number of words to consider together (n), load text files for training, generate new text, and save the generated text to a file of their choice

# Run 
python3 ./scripts/main.py
