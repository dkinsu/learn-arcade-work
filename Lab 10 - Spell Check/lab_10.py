import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

dictionary = open("dictionary.txt")
dictionary_list = []
for line in dictionary:
    dictionary_line = line.strip()
    dictionary_list.append(dictionary_line)
dictionary.close()

line_number = 0
alice = open("AliceInWonderLand200.txt")
for line in alice:
    word_list = split_line(line)
    line_number += 1
    for word in word_list:
        found = False
        i = 0
        while i < len(dictionary_list) and not found:  # If not at end of dictionary list, keep searching
            if word.upper() == dictionary_list[i]:
                found = True
            i += 1
        if not found:
            print(word, "at line number", line_number, "not found")
alice.close()

# read line
# split line into list of words - use split line
# for word in word list
# Linear search
# while not at end of dictionary and not found: search
"""found = False
i = 0
for word in word_list:
    while i < len(dictionary_list) and not found:
        if word.upper() == dictionary_list[i]:
            found = True
        i += 1"""
print("--- Binary Search ---")
# Binary Search
line_number = 0
alice = open("AliceInWonderLand200.txt")
for line in alice:
    word_list = split_line(line)
    line_number += 1
    for word in word_list:
        lower_bound = 0
        upper_bound = len(dictionary_list)
        middle_bound = (lower_bound + upper_bound // 2)

