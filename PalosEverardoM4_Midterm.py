"""
1. The complete sentence, with only the first letter of the first word capitalized (if it wasn't already), 
spaces between each word, and a period at the end.

2. The count of the number of words in the sentence.

Hint: end input on a blank line or on input of the word "done".

For instance, if the input is: 
the

cat

ran 

home

quickly

Your program should output:

The cat ran home quickly.
""" 

words = []

while True:
    line: str = input().strip()

    if line == "" or line.lower() == "done":
        break

    words.append(line)

if words: 
    sentence = " ".join(words)
    sentence = sentence[0].upper() + sentence[1:] + "."
    print(sentence)

    count = len(words)
    if count == 1:
        print(f"There is {count} word in the sentence.")
    else:
        print(f"There are {count} words in the sentence.")
else:
    print(".")
    print("There are 0 words in the sentence.")
