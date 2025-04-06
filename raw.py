def minion_game(s):
    # Define player names
    name = "Stuart"
    name1 = "Kevin"

    # Generate all substrings
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])

    # Classify substrings based on the first character
    vowels_substrings, consonants_substrings = [], []
    for substring in substrings:
        if substring[0] in "aeiouAEIOU":
            vowels_substrings.append(substring)
        else:
            consonants_substrings.append(substring)

    # Function to count frequency of substrings in the original string
    def count_frequencies(original_string, substrings):
        frequencies = {}
        for substring in substrings:
            count = 0
            start = 0
            while start < len(original_string):
                pos = original_string.find(substring, start)
                if pos != -1:
                    count += 1
                    start = pos + 1
                else:
                    break
            frequencies[substring] = count
        return frequencies

    # Find frequencies of elements in vowels_substrings and consonants_substrings
    vowels_frequencies = count_frequencies(s, vowels_substrings)
    consonants_frequencies = count_frequencies(s, consonants_substrings)

    # Calculate total frequencies
    total_vowels_frequency = sum(vowels_frequencies.values())
    total_consonants_frequency = sum(consonants_frequencies.values())

    # Determine the winner and print only the player with the score
    if total_vowels_frequency > total_consonants_frequency:
        print(f'{name1} {total_vowels_frequency}')
    else:
        print(f'{name} {total_consonants_frequency}')


if __name__ == '__main__':
    s = input()
    minion_game(s)