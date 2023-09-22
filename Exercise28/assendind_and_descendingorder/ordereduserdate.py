numbers = []
words = []

# Taking numbers as input
while True:
    try:
        num = input("Enter a number (0 to stop): ")
        num = int(num)
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Taking words as input
while True:
    word = input("Enter a word (END to stop): ")
    if word == "END":
        break
    words.append(word)

# Sorting and printing numbers
sorted_numbers_asc = sorted(numbers)
sorted_numbers_desc = sorted(numbers, reverse=True)

print("Numbers in ascending order:", sorted_numbers_asc)
print("Numbers in descending order:", sorted_numbers_desc)

# Sorting and printing words
sorted_words_asc = sorted(words)
sorted_words_desc = sorted(words, reverse=True)

print("Words in ascending order:", sorted_words_asc)
print("Words in descending order:", sorted_words_desc)
