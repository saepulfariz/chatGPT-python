import os
import openai
openai.api_key = "ENTER YOUR APIKEY"

print("█▀█ █▀█ █▀▀ █▄░█ ▄▀█ █   █▀▀ █░█ ▄▀█ ▀█▀ █▀▀ █▀█ ▀█▀");
print("█▄█ █▀▀ ██▄ █░▀█ █▀█ █   █▄▄ █▀█ █▀█ ░█░ █▄█ █▀▀ ░█░");
print('Welcome Bot Open AI Python By Saepulfariz');
# script by saepulfariz 26/12/2022
print('');

print('Input your name : ', end = '');
nameQuestion = input();
print('');

print('Started AI....');
print("Type 'stop' to stop chat");

nameBot = '>> BOT AI \t:';
nameBotQuestion = '>> %s \t:'%(nameQuestion);

def rsp(question):
    prmt = "Q: {qst}\nA:".format(qst=question)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prmt,
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text


print('');
print("%s Hello %s, type to start chat."%(nameBot, nameQuestion));
i = 1
while i < 2 :
    print('%s '%(nameBotQuestion), end = '');
    inputQuestion = input();
    
    if inputQuestion == 'stop':
        print('');
        print('▀█▀ █░█ ▄▀█ █▄░█ █▄▀ █▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █▀ █ █▄░█ █▀▀');
        print('░█░ █▀█ █▀█ █░▀█ █░█ ▄█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   █▄█ ▄█ █ █░▀█ █▄█');
        break
    else :
        answerAI = rsp(inputQuestion);
        print('%s %s'%(nameBot, answerAI));













