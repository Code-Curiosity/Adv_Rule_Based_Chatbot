# Python Rule-Based ChatBot

This repository contains a simple rule-based chatbot implemented in Python. The chatbot uses predefined rules to generate responses based on user inputs.

## How It Works

1. **Input Processing**: The chatbot takes user input and processes it to identify keywords or phrases.
2. **Rule Matching**: The processed input is matched against a set of predefined rules. Each rule consists of a pattern and a corresponding response.
3. **Response Generation**: If a match is found, the chatbot generates a response based on the matched rule. If no match is found, a default response is provided.
4. **Output**: The generated response is displayed to the user.

## Example

Here is a simple example of how the chatbot works:

1. User Input: "Hello"
2. Rule Matching: The input matches the rule for greeting.
3. Response Generation: The chatbot responds with "Hi there! How can I help you today?"

## Getting Started

To run the chatbot, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/code-curiosity/Python_Rule_Based_ChatBot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Python_Rule_Based_ChatBot
    ```
3. Run the chatbot script:
    ```bash
    python chatbot.py
    ```
    ## Customizing the Rules

    You can customize the rules by editing the `intent.json` file. Each rule should have tags, patterns, responses, and context. For example:

    ```json
    {
        "rules": [
            {
                "tags": "greeting",
                "patterns": ["hello", "hi", "hey"],
                "responses": ["Hi there! How can I help you today?", "Hello! What can I do for you?"],
                "context": ""
            },
            {
                "tags": "farewell",
                "patterns": ["bye", "goodbye", "see you"],
                "responses": ["Goodbye! Have a great day!", "See you later!"],
                "context": ""
            }
        ]
    }
    ```

    - **tags**: A label to categorize the rule.
    - **patterns**: A list of phrases that the chatbot will look for in the user input.
    - **responses**: A list of responses that the chatbot can use when a pattern is matched.
    - **context**: Additional information that can be used to provide more relevant responses based on the conversation history.
You can customize the rules by editing the `intent.json` file. Each rule should have tags, patterns, and responses. For example:
```json
{
    "rules": [
        {
            "tags": "greeting",
            "patterns": ["hello", "hi", "hey"],
            "responses": ["Hi there! How can I help you today?", "Hello! What can I do for you?"]
        },
        {
            "tags": "farewell",
            "patterns": ["bye", "goodbye", "see you"],
            "responses": ["Goodbye! Have a great day!", "See you later!"]
        }
    ]
}
```


## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
