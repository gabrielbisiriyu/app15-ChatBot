import openai

class ChatBot:
    def __init__(self):
        openai.api_key="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"  

    def get_response(self,userinput):
        response=openai.Completion.create(
            engine="text-davinci-003",
            prompt=userinput,
            max_tokens=4000, # The bot produces a maximum of 4000 words
            temperature=0.5 # 0.5 gives the best answers
        ).choices[0].text
        return response 



if __name__ == "__main__":
    chatbot=ChatBot() 
    response=chatbot.get_response("how big is an elephant") 
    print(response)
    
