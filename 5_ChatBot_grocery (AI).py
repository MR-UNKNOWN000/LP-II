import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        r"\b(1|hello|hi|hey)\b": " Hello! Welcome to our grocery store. How can I help you today?",
        r"\b(2|how are you)\b": "I'm just a bot, but I'm here to assist you with groceries!",
        r"\b(3|order status|track order)\b": "Please provide your order ID to check the status.",
        r"\b(4|shipping time|delivery time)\b": "We offer same-day delivery and standard shipping (3-5 business days).",
        r"\b(5|return policy)\b": "You can return items within 7 days if unopened. Would you like help with a return?",
        r"\b(6|thank you|thanks)\b": " You're welcome! Let me know if you need anything else.",
        r"\b(7|price|cost)\b": "Please specify the product name to check its price.",
        r"\b(8|milk)\b": "Milk is 30rs per liter.",
        r"\b(9|eggs)\b": "A dozen eggs cost 80rs.",
        r"\b(10|rice)\b": "Rice is 50rs per kg.",
        r"\b(11|vegetables|veggies)\b": "We have fresh vegetables available. What are you looking for?",
        r"\b(12|fruits)\b": "We have apples, bananas, and oranges in stock. Which one do you need?",
        r"\b(13|snacks)\b": "We have chips, biscuits, and chocolates available.",
        r"\b(14|beverages|drinks)\b": "We have soft drinks, juices, and bottled water. What would you like?",
        r"\b(15|buy|order)\b": "You can place an order on our website or visit our store.",
        r"\b(16|payment methods)\b": "We accept cash, credit/debit cards, and UPI payments.",
        r"\b(17|store hours|timing)\b": "Our store is open from 8 AM to 10 PM every day.",
        r"\b(18|location|address)\b": "We are located at XYZ Market, Main Street, City.",
        r"\b(19|bye|exit)\b": "Goodbye! Happy shopping! 🛍"
    }

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
   
    return "I am sorry, I didn't understand that. Can you rephrase or ask about a specific grocery item?"

# Chatbot interaction loop
print("Welcome to our Grocery Chatbot! Type 'exit' to end the conversation.")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Happy shopping! 🛍")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)

    '''✅ Title:
Rule-Based Grocery Chatbot Using Python

✅ Algorithm:
Convert the user input to lowercase for uniform matching.

Use regular expressions (regex) to pattern-match user queries.

If a pattern matches, return the corresponding response.

If no pattern matches, return a default message.

✅ Short Theory:
This chatbot is a rule-based conversational agent that uses regex pattern matching to identify keywords or intents from the user's message and respond accordingly. It simulates basic customer service for a grocery store, handling greetings, product inquiries, prices, orders, and store information.

✅ Features:
Keyword-based response mapping using re.search()

Multiple grocery-related intents handled (price, product, order, location)

Case-insensitive input handling

Simple fallback for unrecognized inputs

Exit condition using exit or bye

✅ Sample Output:
vbnet
Copy
Edit
You: hi
Chatbot: Hello! Welcome to our grocery store. How can I help you today?

You: What is the price of milk?
Chatbot: Milk is 30rs per liter.

You: Exit
Chatbot: Goodbye! Happy shopping! 🛍
✅ Data Structures Used:
Dictionary for pattern-response mapping

Regex (re module) for string pattern matching

✅ Time & Space Complexity:
Time Complexity: O(N) for matching N patterns (assuming regex cost is small)

Space Complexity: O(N) where N is number of predefined patterns

✅ Applications:
Small retail or grocery support bots

Educational demos of rule-based NLP

FAQ automation systems

✅ Viva Questions & Answers:
Q1: What is the chatbot based on?
A1: It is a rule-based chatbot using regex pattern matching.

Q2: What module is used for pattern matching?
A2: Python’s built-in re (regular expression) module.

Q3: How does the bot handle unknown inputs?
A3: It returns a default message when no pattern matches.

Q4: Is this chatbot AI-based?
A4: No, it's rule-based and does not use NLP or ML techniques.

Q5: How can you improve this chatbot?
A5: By integrating NLP libraries, context tracking, or machine learning models.'''