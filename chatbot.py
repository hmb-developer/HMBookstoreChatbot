import spacy
nlp = spacy.load("en_core_web_sm")

def respond_to_user(user_input):
    doc = nlp(user_input)

    for token in doc:
        print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}") 

    if "hello" in user_input.lower() or "hi" in user_input.lower() or "hey" in user_input.lower():
        response = "Hello! Welcome to HM Bookstore. How can I assist you today?"
    
    elif any(token.lemma_ in ["recommend", "suggest"] for token in doc):
        return "Sure! What genre are you interested in?"
    elif any(token.lemma_ in ["buy", "purchase"] for token in doc):
        return "Great! Do you have a specific book in mind or are you looking for recommendations?"
    elif any(token.lemma_ in ["how are you", "what do you do"] for token in doc):
        return "I'm doing well, thank you for asking! How would you like me to assist you?"
    else:
        for entity in doc.ents:
            if entity.label_ == "PERSON":
                return f"Ah, Are you talking about {entity.text}! What would you like to know about them?"
            elif entity.label_ == "ORG":
                return f"Thank you for mentioning {entity.text}. How can I help you with that?"
            elif entity.label_ == "GPE":
                return f"Ah, {entity.text}. That's a great place! How can I assist you with your book search?"
            else:
              return "I'm sorry, I didn't understand that.I am still learning. Can you please rephrase?"

    return response

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = respond_to_user(user_input)
    print(f"Chatbot: {response}") 

















#def greet():
#    return "Welcome to ABC Bookstore! How can I help you find your next great read today?"