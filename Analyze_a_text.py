import string

def analyze_text(file_path, target_word=None):
    """
    Analyze a text file to count the number of lines, words, and occurrences of a specific word.

    :param file_path: Path to the text file.
    :param target_word: The word to count occurrences of (case-insensitive). If None, this count is skipped.
    :return: A dictionary with counts of lines, total words, and occurrences of the target word.
    """
    line_count = 0
    word_count = 0
    target_word_count = 0

    # Open the file and start processing
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            words = line.strip().split()
            word_count += len(words)

            # Count the target word, if specified
            if target_word:
                target_word_count += sum(word.strip(string.punctuation).lower() == target_word.lower() for word in words)

    # Compile the results
    result = {
        'lines': line_count,
        'words': word_count,
        'target_word_occurrences': target_word_count if target_word else 'N/A'
    }

    return result

# Example usage
file_path = 'example.txt'  # Replace with your file path
target_word = 'Python'     # Replace with your target word or set to None
analysis = analyze_text(file_path, target_word)
print(analysis)
