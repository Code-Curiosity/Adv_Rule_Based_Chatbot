import random
import json
import re

# Load the intent file
def Load_intent(filenm = "intent.json"):
    try:
        with open(filenm, 'r', encoding='utf-8') as file:
            # Load the intent file
            intents = json.load(file)
        print("Bot is ready")
        #For accessing the data from file we use data.get() method
        return data.get('intents',[]) #If the keyword is not found then it will return empty list
    except Exception as e:
        print("Something doesn't seem right 🫤")
        return [] #If the file is not found then it will return empty list, prevents crashing of program
    