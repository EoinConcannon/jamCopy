
def hello(input_message):
    # When this command is used, everything after the word "hello" in the message will be sent to this function.
    # Example: "@Jam hello Ronan" -> this function receivces "Ronan" as the messsage.
    #
    # Your job is to process the message so that this function returns the correct outputs for challenge 1.
    # (for no, it just echoes back the same message)



    if(len(input_message) != 0):
        message = "Hello, " + input_message + "!"
        

        input_message = input_message.lower()


        if input_message == "seamus":
            message = "I'm sorry Seamus, I can't do that"
    
        elif input_message == "eoin":
            message = "Hello Cisco’s favourite CEO Eoin!"
    
        elif input_message == "mark":
            message = "Hello Cisco’s favourite CEO Mark!"
    
        elif input_message == "chuck robbins":            
            message = "Hello Cisco’s favourite CEO Chuck Robbins!"
        
        elif len(input_message) == 5:
            if input_message.count('c') == 2:
                if input_message.count('i') == 1:
                    if input_message.count('s') == 1:
                        if input_message.count('o') == 1:
                            message = "Hello, Cisco in disguise!"


        return message




    message = ("Hello, Cisco!")
  
    return message
