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
def get_response(user_input):
    user_input = user_input.lower() #Step:1 Convert the user input to lower case for uniformity
    match_scores = {} #Step:2 Prepare dictionary for storing the matched scores of each intent
    #Step:4 Loop through the intents
    for intent in intents:
        # Count how many patterns match the user input for each intent
        match_count = sum(
            1 for pattern in intent["patterns"]
            #if re.search(r'\b' + re.escape(pattern.lower()) + r'\b', user_input)
            if pattern.lower() in user_input  # Check if pattern is a substring of the user input
        )

        # If there are matches, store the count in match_scores with the tag as the key
        if match_count > 0:
            match_scores[intent["tag"]] = match_count

    if not match_scores:
    # Directly find 'unknown' tag responses here without a separate function
        unknown_responses = next(intent["responses"] for intent in intents if intent["tag"] == "unknown")
        return random.choice(unknown_responses)
    
    best_match = max(match_scores, key=match_scores.get)  # Get the intent with most matches
    best_responses = next(intent["responses"] for intent in intents if intent["tag"] == best_match)

    # Check if the detected tag is 'goodbye' and return a random goodbye response before exiting
    if best_match == "goodbye":
        goodbye_response = random.choice(best_responses)
        print("Bot:", goodbye_response)
        exit()  # Terminate the program after displaying the random goodbye message
    
    return random.choice(best_responses)
# Main loop
# The chatbot will keep running until the user types anything that fully or partially matches the tag goodbye
while True:
    user_input = input("You: ")
    response = get_response(user_input)  # Get the response and the detected tag
    print("Bot:", response)
    # We will not write the break statment as the logical part will already check
    # If the chat match the tag "goodbye" and if it does then it will terminate itself