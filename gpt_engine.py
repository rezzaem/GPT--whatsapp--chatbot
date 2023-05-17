# import openai
# from api_secrets import api_key
# openai.api_key=api_key
# prompt="""Brainstorm some ideas combining VR and fitness:"""
# response=openai.Completion.create(engine='text-davinci-001',prompt=prompt,max_tokens=6)
# print(response)
#-------------------------------------------------------------------------------------------------
# import os
# import openai

# openai.api_key = api_key

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Brainstorm some ideas combining VR and fitness:",
#   temperature=0.6, #
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=1,
#   presence_penalty=1
# )
# print(response)
#-------------------------------------------------------------------------------------------------
# import openai
# from api_secrets import api_key

# openai.api_key=api_key

# completion=openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=[{"role":"user","content":"Write an essay about penguins"}])
# print(completion.choices[0].message.content)
#-------------------------------------------------------------------------------------------------
import openai
from api_secrets import api_key

openai.api_key=api_key

messages=[]
system_msg="Receptionist at Mehr Bushehr Laboratory"
messages.append({"role":"system","content":system_msg})

print("your new assistant is ready!")
while input !="quit()":
    message=input("user:")
    messages.append({"role":"user","content":message})
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply=response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    print("\n"+"bot:"+reply+"\n")