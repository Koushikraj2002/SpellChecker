from spellchecker import SpellChecker  # Correct import

spell = SpellChecker()

# Take user input
user_input = input("Enter a sentence: ")

# Split the input into words and check each word
words = user_input.lower().split()
for word in words:
    # Check each word and print suggestions if it's misspelled
    correctword=spell.correction(word)
    if word == correctword or word == None:
        pass
    else:
        print(f"{word} is misspelled. Suggestions: {correctword}")
