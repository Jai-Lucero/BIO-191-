def count_syllables(word):
    vowels = 'aeiouy'
    syllables = 0
    last_char_vowel = False
    
    for char in word:
        if char.lower() in vowels:
            if not last_char_vowel:
                syllables += 1
            last_char_vowel = True
        else:
            last_char_vowel = False
    
    return max(syllables, 1)

word = input("Enter a word: ")
print("The word", (word), "has", count_syllables(word), "syllables.")