from english_words import get_english_words_set
from collections import Counter

word_list = get_english_words_set(["web2"], lower=True)
print(f"Total available words: {len(word_list)}")


def find_words(letters):
    """Find all words that can be formed using the given letters.

    Returns:
        set: Returns a set of generated words.
    """
    letter_count = Counter(letters)

    return {
        word
        for word in word_list
        if len(word) > 2 and all(word.count(ch) <= letter_count[ch] for ch in word)
    }


def main():
    letters = [
        char
        for char in input("Enter the available letters: \n>> ").lower()
        if char.isalpha()
    ]

    valid_words = find_words(letters=letters)

    print(
        f"{len(valid_words)} valid words found for the combination [{', '.join(letters)}]:\n"
        + "\n".join(valid_words)
        if valid_words
        else "No valid words found, try again :("
    )


if __name__ == "__main__":
    main()
