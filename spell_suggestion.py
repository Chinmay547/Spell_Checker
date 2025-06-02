# Step 1: Predefined dictionary
word_dict = {
    'a': ['apple', 'ant', 'arrow'],
    'b': ['ball', 'bat', 'banana'],
    'c': ['cat', 'cup', 'car'],
    't': ['the', 'this', 'that'],
}

# Step 2: Function to check similarity
def similarity_score(word1, word2):
    matches = 0
    min_len = min(len(word1), len(word2))
    for i in range(min_len):
        if word1[i] == word2[i]:
            matches += 1
    return matches

# Step 3: Function to get best suggestion
def get_suggestion(word):
    first_letter = word[0].lower()
    if first_letter in word_dict:
        candidates = word_dict[first_letter]
        max_score = 0
        suggestion = None
        for candidate in candidates:
            score = similarity_score(word.lower(), candidate)
            if score > max_score:
                max_score = score
                suggestion = candidate
        # Only suggest if score is reasonably high and it's not an exact match
        if suggestion and suggestion != word.lower() and max_score >= 2:
            return suggestion
    return None

# Step 4: Main program
user_input = input("Enter a sentence: ")
words = user_input.split()

for word in words:
    suggestion = get_suggestion(word)
    if suggestion:
        print(f"Did you mean '{suggestion}' instead of '{word}'?")
