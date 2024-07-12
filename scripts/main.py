""" Run program directly from this file"""
from scripts.corpus import tokenize, detokenize
from scripts.lm import LanguageModel

# First we want to create a LM with a user specified n:
def users_model():
  n = int(input("Hello! Welcome, please enter the value n for your desired N-Gram Language Model: "))
  return LanguageModel(n)


# Now we want to ask the user to load the test file of their choice and train the model:
def loading_training(LM):
   file_path = input("Please, enter the path for the file you would like to load and train: ")
   # Opening and reading the file 
   with open(file_path, 'r') as file:
      test_text = file.read()
      # Training the model using the tokenize function we initiated and the train method from the LanguageModel class
      tokenized_text = tokenize(test_text)
      LM.train([tokenized_text])


# We would also like to generate a text from the file the user chose and print it to their screen:
def generate_text(LM):
      # Applying the generate method from the LanguageModel class and the detokenize function, to create text sequences    
      generated_text = detokenize(LM.generate())
      print("Here is the generated text: ", generated_text)


# Also we want to generate a user-specified number of texts from the Language Model and write them to a file of the user's choice:
def text_to_file(LM):
    number_of_texts = int(input("Please, enter the number of texts you would like to generate: "))
    new_file_path = input("Now, please enter the path you would like to save your generated texts: ")
    with open(new_file_path, 'w') as file: # We wanted to use the write mode 
      for i in range (number_of_texts):
         generated_text = detokenize(LM.generate())
         if i != 0:
           file.write('\n')
           # Writing each generated text sequence and adding a newline to distinguish it from the others
         file.write(generated_text + "\n")
    print(str(number_of_texts), " texts generated and saved to ", new_file_path,  ".")

# Creating a final function with a loop that will enable us to create a type of user interface in the terminal
def main(): 
    print("Hello, This is the Language Model interface!")
    print("Proceed by choosing the first option from the menu and then follow along the steps in increasing order.")
# Starting by initializing the value None for our LM so that we can handle the if-else statements 
    LM = None
    while True:
        print("Menu:")
        print("1. Choose an n and create your Language Model.")
        print("2. Load texts from a file of your choice and train the Language Model.")
        print("3. Generate a text from the Language Model and print it to the terminal.")
        print("4. Specify a number of texts you would like and write them to a file of your choice.")
        print("5. Exit the program.")
# We wanted to make sure that the user will choose 1 first to generate a Language Model
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            LM = users_model()
        elif choice == '2':
            if LM is None:
                print("Please, first choose an n for your Language Model by pressing 1.")
            else:
                loading_training(LM)
        elif choice == '3':
            if LM is None:
                print("Please, first choose an n for your Language Model by pressing 1.")
            else:
                generate_text(LM)
        elif choice == '4':
            if LM is None:
                print("Please, first choose an n for your Language Model by pressing 1.")
            else:
                text_to_file(LM)
        elif choice == '5':
            print("You are now exiting the program. Thank you and goodbye!")
           # Loop stops when the user chooses 5
            break

if __name__ == "__main__":
    main()