import random
import speech_recognition as sprc
from gtts import gTTS
import playsound as speakers
import os

print('ROCK_PAPER_SCISSOS'.center(50, '*'))
choices = ['rock', 'papper', 'scissors']
win, lose, tie = 0, 0, 0
quit_kw = ['stop', 'exit', 'quit', 'terminate']

def speak(text):
    text_to_say = gTTS(text)
    text_to_say.save('voice.mp3')
    speakers.playsound('voice.mp3')
    os.remove('voice.mp3')


def listen():
  with sprc.Microphone() as mic:

    while True:
        global player_text
        try:
            R = sprc.Recognizer()
            player_voice = R.listen(mic)
            player_text = str(R.recognize_google(player_voice))
            break
        except:
            speak('couldn\'t hear you. come again')
            break
    return player_text


def winner(player, computer):
    global win, lose, tie

    if player == 'rock' and computer == 'scissors':
        win += 1;
        return 'win'
    elif player == 'papper' and computer == 'rock':
        win += 1;
        return 'win'
    elif player == 'scissors' and computer == 'papper':
        win += 1;
        return 'win'

    else:
        lose += 1
        #win -= 1
        return 'loss'

while True:
    if win == 3: speak('I\'m done,your are ultimate winner with 3 wins');break
    if lose == 3: speak('I\'m done,your are ultimate looser 0 wins ');break
    speak('your score.')
    print(f"win:{win}\t lose:{lose}\t tie:{tie}")
    while True
        print('lets play a game. You go first')
        player_choice1 = None
        player_choice=None
        print('say: rock/papper/scissors')
        try:
            player_tx = listen()
            player_words = [x.casefold() for x in player_tx.split()]
            for word in choices:
                if word in player_words:
                    player_choice1 = word
                    break
            else: speak('say it correct')
        except:
            speak("couldn\'t hear you. try again")
        if player_choice1 in choices: break

    computer_choice = choices[random.randint(0, 2)]
    speak(f"my choice is {computer_choice}")
    print(player_choice1,computer_choice)
    if player_choice1 == computer_choice:
        tie += 1
        result='tie'

    else:
        result = winner(player_choice1, computer_choice)

    speak('you win..') if result == 'win' else speak('you win..') if result == 'lose' else speak(result)
    speak('Do you want play agian?')
    player_choice=listen()
    player_choice = [x for x in player_choice.split()]
    for opinion in quit_kw:
       if opinion in player_choice:
            speak('request accepted')
            speak('your score')
            print(f"win:{win}\t lose:{loss}\t tie:{tie}")
            speak('had a good time with you.Take care')
            player_choice=opinion
            break

    if player_choice in quit_kw:break
