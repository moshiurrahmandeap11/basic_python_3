# Word Count by using dictionary

def word_count(text):
    words = text.split()
    count_dict = {}
    for word in words:
        word = word.lower()
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict


# Example usage
input_text = input("Enter a string to count word occurrences: ")
result = word_count(input_text)
print("Word count:", result)