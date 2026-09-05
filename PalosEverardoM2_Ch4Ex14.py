"""Write a program that uses nested loops to draw this pattern:
    ##
    # #
    #  #
    #   #
    #    #
    #     #
"""

rows: int = 6
for i in range(rows):
    for j in range(i + 1):
        if j == 0 or j == i:
            print("#", end="")
        else:
            print(" ", end="")
    print()

