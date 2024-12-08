from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

import ollama


def getresponse(input_text, no_of_words, user_type):

# Path to the safetensors model



    template = """
               Write a blog for {user_type} on given topic {input_text} in given length {no_of_words}.
               """
    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model="llama3.2:3b")


    chain = prompt | model
    response = chain.invoke({
        "user_type": user_type,
        "input_text": input_text,
        "no_of_words": no_of_words
    })

    return response