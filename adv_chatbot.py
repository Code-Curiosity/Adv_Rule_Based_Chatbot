import random
import json
import re

# Load the intent file
def Load_intent(filenm = "intent.json"):
    try:
        with open(filenm, 'r', encoding='utf-8') as file:
            # Load the intent file and converting it into dictionary
            intent_file = json.load(file)
        print("Bot is ready")
        #For accessing the data from file we use ".get()" method
        return intent_file.get('intents',[]) #If the intents keyword is not found then it will return empty list
    except Exception as e:
        print(f"Something doesn't seem right 🫤 {e}")
        return [] #If the file is not found then it will return empty list, prevents crashing of program
intents = Load_intent() #Step:3 Load the intents from the json file

# Function to get synonyms for a word
def get_synonyms(word):
    for intent in intents:
        synonyms = intent.get("synonyms", {})
        for key, values in synonyms.items():
            if word == key or word in values:
                return [key] + values  # Return all synonyms including the original word
    return [word]  # Return the word itself if no synonyms are found


# Improved pattern matching logic with synonym checking
def is_similar(user_input, pattern):
    user_words = set(user_input.split())  # Split user input into words
    pattern_words = set(pattern.split())  # Split pattern into words
    
    overlap = user_words.intersection(pattern_words)  # Find common words
    overlap_count = len(overlap)  # Count the number of overlapping words
    
    if overlap_count == 0:
        return 0  # No match, return a score of 0

    # Score calculation using overlap count and pattern length
    score = overlap_count / len(pattern_words)
    return score  # Return the score instead of just True/False

# New pattern-matching function with synonym checking
def match_pattern(user_input, pattern):
    user_words = user_input.split()
    pattern_words = pattern.split()
    
    # Expand user words and pattern words with synonyms
    expanded_user_words = set()
    for word in user_words:
        expanded_user_words.update(get_synonyms(word))

    expanded_pattern_words = set()
    for word in pattern_words:
        expanded_pattern_words.update(get_synonyms(word))
        
    overlap = expanded_user_words.intersection(expanded_pattern_words)
    overlap_count = len(overlap)
    
    if overlap_count == 0:
        return 0  # No match

    score = overlap_count / len(expanded_pattern_words)
    return score
# Get response function
def get_response(user_input):
    user_input = user_input.lower()  # Convert user input to lower case for uniformity
    match_scores = {}  # Prepare dictionary for storing the matched scores of each intent
    
    # Loop through the intents
    for intent in intents:
        tag = intent["tag"]
        total_score = 0  # Total score for this tag
        
        for pattern in intent["patterns"]:
            pattern_lower = pattern.lower()
            
            # 1. Exact Match (Full sentence match)
            if pattern_lower == user_input:
                total_score += 5  # High score for exact match

            # 2. Partial Match (Pattern is a substring of user input)
            elif pattern_lower in user_input:
                total_score += 2  # Lower score for partial match

            # 3. Weighted Scoring System (Pattern similarity calculation)
            similarity_score = match_pattern(user_input, pattern_lower)
            total_score += similarity_score * 3  # Weight given to similarity match

        if total_score > 0:
            match_scores[tag] = total_score  # Save the score for this tag

    if not match_scores:
        unknown_responses = next(intent["responses"] for intent in intents if intent["tag"] == "unknown")
        return random.choice(unknown_responses)
    
    # Find the best match or matches
    max_score = max(match_scores.values())
    best_matches = [tag for tag, score in match_scores.items() if score == max_score]

    # Randomly select from the best matches if there's a tie
    best_match = random.choice(best_matches)
    best_responses = next(intent["responses"] for intent in intents if intent["tag"] == best_match)

    # Handle 'goodbye' tag
    if best_match == "goodbye":
        goodbye_response = random.choice(best_responses)
        print("Bot:", goodbye_response)
        exit()

    return random.choice(best_responses)
# Main loop
# The chatbot will keep running until the user types anything that fully or partially matches the tag goodbye
while True:
    user_input = input("You: ")
    response = get_response(user_input)  # Get the response and the detected tag
    print("Bot:", response)
    # We will not write the break statment as the logical part will already check
    # If the chat match the tag "goodbye" and if it does then it will terminate itself