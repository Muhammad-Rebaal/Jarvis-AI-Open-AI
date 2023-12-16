fileopen = open("API_Key.txt","r")
API = fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def reply(question, chat_log = None):
    File_log =open("abc.txt","w")
    chat_log_template = File_log.write("")
    File_log.close()

    if chat_log is None:
        chat_log = chat_log_template
    
    prompt = f"{chat_log} You : {question}\n Jarvis: "
    response = completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0    
                )
    answer = response.choice[0].text.strip()
    chat_log_template_update = chat_log_template +f"\n You: {question}\n Jarvis : {answer}"
    Filelog = open("","w")
    Filelog.write(chat_log_template_update)
    Filelog.close()
    return answer

print(reply("How are you?"))