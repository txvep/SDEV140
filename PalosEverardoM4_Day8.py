"""
Use the provided input file 'cleantext.txt' that was output of today's demo to get a count of how many times a particular word occurs in the passage.
Read the file contents into a string variable and do a split into individual word list based on a blank space delimiter.
Reference P453 in section 8.3 for explanation of the split string method.

Once you have your string list created. 
You can sort it in preparation to count the words and how many times they have occurred in the passage.
Reference p375 in section 7.5 for coverage on list methods  including sorting.  
The result of the (ASCII) sort will group all like words together to enable a search and tally for your final analysis
 and display of each word that occurs and how many times it shows up.
"""


def main(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()

        words = text.split()
        words.sort()

        count = 0
        current_word = ""

        for word in words:
            if word == current_word:
                count += 1
            else:
                if current_word:
                    print(f"{current_word} : {count}")
                current_word = word
                count = 1

        if current_word:
            print(f"{current_word} : {count}")

    except FileNotFoundError:
        print(f"File not found: {filename}")


if __name__ == "__main__":
    main("cleantext.txt")
