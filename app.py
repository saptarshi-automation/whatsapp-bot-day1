while True:
    user_input = input("You: ")

    if "price" in user_input.lower():
        print("Bot: Our products start from ₹499.")

    elif "location" in user_input.lower():
        print("Bot: We are located in Kolkata.")

    elif "hello" in user_input.lower():
        print("Bot: Hello! How can I assist you?")

    elif "hoodie" in user_input.lower():
        print("Bot: Yes, hoodies are available!")

    elif "discount" in user_input.lower():
     print("Bot: Congrats! we have 10 % discount just for today ;)")

    else:
        print("Bot: Please ask about price, location, or products.")