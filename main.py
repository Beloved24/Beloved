# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

file = open("story.txt","r")
read_data = file.read()
per_word = read_data.split()

print("total Words: ", len(per_word))

search_word_count = input("Enter the word: ")
file = open("story.txt", "r")
read_data = file.read()
word_count = read_data.lower().count(search_word_count)
print(f"The word '{search_word_count}' appeared {word_count} times.")

count = 0
file = open("story.txt", "r")
read_data = file.read()
words = set(read_data.split())
for word in words:
    count += 1

print("Total Unique words:", count)