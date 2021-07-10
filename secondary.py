# author: <name here>
# date: <date here>

# -------------------- Section 4 -------------------- #

# Input | ASCII Art


# Objectives:
#   1. Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol | Integer / Float | The symbol used to create the diamond.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Call the function you defined to create the diamond, sending the character as an argument.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#           $
#          $$$
#         $$$$$
#        $$$$$$$
#       $$$$$$$$$
#      $$$$$$$$$$$
#     $$$$$$$$$$$$$
#      $$$$$$$$$$$
#       $$$$$$$$$
#        $$$$$$$
#         $$$$$
#          $$$
#           $
#
# ---- WRITE CODE BELOW ---- #
s = input('>> ')

print(
    ' ' * 6 + s * 1 + '\n' +
    ' ' * 5 + s * 3 + '\n' +
    ' ' * 4 + s * 5 + '\n' +
    ' ' * 3 + s * 7 + '\n' +
    ' ' * 2 + s * 9 + '\n' +
    ' ' * 1 + s * 11 + '\n' +
    ' ' * 0 + s * 13 + '\n' +
    ' ' * 1 + s * 11 + '\n' +
    ' ' * 2 + s * 9 + '\n' +
    ' ' * 3 + s * 7 + '\n' +
    ' ' * 4 + s * 5 + '\n' +
    ' ' * 5 + s * 3 + '\n' +
    ' ' * 6 + s * 1 + '\n'
)

#   2. Framed Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol1 | Integer / Float | The symbol used to create the diamond.
#           symbol2 | Integer / Float | The symbol used to create the frame.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Prompt input from the user in the form of a single character again, and save it to a second variable.
#       d. Call the function you defined to create the framed diamond, sending the characters as arguments.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> &
#   >> ~
#
#     ~~~~~~$~~~~~~
#     ~~~~~$$$~~~~~
#     ~~~~$$$$$~~~~
#     ~~~$$$$$$$~~~
#     ~~$$$$$$$$$~~
#     ~$$$$$$$$$$$~
#     $$$$$$$$$$$$$
#     ~$$$$$$$$$$$~
#     ~~$$$$$$$$$~~
#     ~~~$$$$$$$~~~
#     ~~~~$$$$$~~~~
#     ~~~~~$$$~~~~~
#     ~~~~~~$~~~~~~
#
# ---- WRITE CODE BELOW ---- #

s1 = input('>> ')
s2 = input('>> ')

print(
    s2 * 6 + s1 * 1 + s2 * 6 + '\n' +
    s2 * 5 + s1 * 3 + s2 * 5 + '\n' +
    s2 * 4 + s1 * 5 + s2 * 4 + '\n' +
    s2 * 3 + s1 * 7 + s2 * 3 + '\n' +
    s2 * 2 + s1 * 9 + s2 * 2 + '\n' +
    s2 * 1 + s1 * 11 + s2 * 1 + '\n' +
    s2 * 0 + s1 * 13 + s2 * 0 + '\n' +
    s2 * 1 + s1 * 11 + s2 * 1 + '\n' +
    s2 * 2 + s1 * 9 + s2 * 2 + '\n' +
    s2 * 3 + s1 * 7 + s2 * 3 + '\n' +
    s2 * 4 + s1 * 5 + s2 * 4 + '\n' +
    s2 * 5 + s1 * 3 + s2 * 5 + '\n' +
    s2 * 6 + s1 * 1 + s2 * 6 + '\n'
)
