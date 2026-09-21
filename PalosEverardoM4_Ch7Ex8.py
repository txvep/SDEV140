"""
If you have downloaded the source code you will find a file in the Chapter 07 folder named popular_names.txt.
This file contains a list of the 400 most popular names given to children born in the United States
from the year 2000 through 2009. Write a program that reads the contents of file into a list.
The user should be able to enter a name and the program will display a message indicating
whether the name was among the most popular.
"""

def load_names(filename):
    names: list[str] = []

    try:
        with open(filename, "r") as file:
            for line in file:
                name = line.strip()
                if name and not name.startswith("#"):
                    names.append(name)
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return []

    return names


def main() -> None:
    filename = "popular_names.txt"

    names = load_names(filename)

    if not names:
        print("No names were loaded.")
        return

    print(f"Loaded {len(names)} popular names.\n")

    name: str = input("Enter a name to check if it is popular: ").strip().title()

    if name in names:
        print(f"{name} is among the most popular names.")
    else:
        print(f"{name} is not among the most popular names.")


if __name__ == "__main__":
    main()
