# Adv\_Rule\_Based\_Chatbot

A Python-based advanced rule-based chatbot that uses improved intent matching, context handling, scoring systems, and user input correction — all without relying on external libraries. Perfect for learning and enhancing chatbot development with pure Python.

## 🚀 Features

1. **Improved Intent Matching:**

   - Enhanced pattern matching with synonyms handling and better scoring mechanisms.
   - Recognizes phrases with similar meanings, providing more accurate responses.

2. **Context Handling:**

   - Remembers previous interactions to maintain context throughout the conversation.
   - Provides appropriate responses based on conversation history.

3. **Enhanced Scoring System:**

   - Assigns weights to important keywords to improve response accuracy.
   - Uses a scoring mechanism to select the most relevant tag when multiple tags match.

4. **Handling Multiple Tags:**

   - Handles multiple intents within a single user input.
   - Provides segmented responses to address all parts of the input.

5. **Improved Response Selection:**

   - Supports various response styles: Casual, Formal, Humorous, etc.
   - Dynamically selects responses based on user preferences.

6. **User Input Correction:**

   - Detects and corrects minor spelling errors to enhance pattern matching.

7. **Feedback System:**

   - Collects user feedback to improve future interactions.

---

## 📂 File Structure

- `adv_chatbot.py`: The main Python file containing the chatbot logic.
- `intent.json`: The JSON file containing predefined intents, patterns, and responses.
- `README.md`: Documentation file (this one).

---

## 🔍 How It Works

1. **User Input Processing:**
   - Converts user input to lowercase and splits it into words.
2. **Intent Matching & Scoring:**
   - Matches user input against predefined patterns using scoring mechanisms.
3. **Contextual Responses:**
   - Takes conversation history into account while generating responses.
4. **Response Generation:**
   - Chooses the most appropriate response or asks for clarification if needed.

---

## 📌 Example Usage

```
You: Hello
Bot: Hi there! How can I help you today?

You: What's the weather like?
Bot: I'm just a chatbot, but I recommend checking a weather website!

You: Tell me a joke
Bot: Why did the chicken join a band? Because it had the drumsticks!

You: Another one
Bot: What do you call a bear with no teeth? A gummy bear!
```

---

## 💡 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/code-curiosity/Adv_Rule_Based_Chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Adv_Rule_Based_Chatbot
   ```
3. Run the chatbot:
   ```bash
   python adv_chatbot.py
   ```

---

## 🔨 Customizing Intents

Modify the `intent.json` file to add new patterns, responses, and tags:

```json
{
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["hello", "hi", "hey"],
            "responses": ["Hello! How can I assist you?", "Hi! What can I do for you today?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["bye", "goodbye", "see you later"],
            "responses": ["Goodbye! Have a great day!", "See you next time!"]
        }
    ]
}
```

---

## 📢 Contributions

Contributions are welcome! Feel free to fork the repo and submit a pull request with improvements or suggestions.
