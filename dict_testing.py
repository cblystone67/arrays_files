def count_words(file_path):
    word_counts = {}  # Initialize an empty dictionary to store word counts

    # Open the file in read mode
    with open(file_path, 'r')as file:
        # Read each line in the file
        for line in file:
            # Split the line into words
            words = line.split()
            # Iterate through each word
            for word in words:
                # Remove punctuation and convert to lowercase (optional)
                word = word.strip().lower()
                # Update the word count in the dictionary
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def main():
    file_path = '/Users/christopherblystone/Documents/Joy of Coding/turing.txt'
    word_counts = count_words(file_path)
    for word, count in word_counts.items():
        print(f'{word}: {count}')

    print("end of main")


if __name__ == "__main__":
    main()
