import random


print('ROCK_PAPER_SCISSOS'.center(50, '*'))
choice = ['R', 'P', 'S']
win, loss, tie = 0, 0, 0
quit_kw=['stop','exit','quit','terminate']
play_kw=['yes','ok','yeah','play']

def winner(player, computer):
    global win, loss, tie
    if player == computer:
        tie += 1;return 'you tie'
    elif player == 'R' and computer == 'S':
        win += 1;return 'you win'
    elif player == 'P' and computer == 'R':
        win += 1;return 'you win'
    elif player == 'S' and computer == 'P':
        win += 1;return 'you win'
    else:
        loss+=1
        win-=1
        return 'you loss..!'




while True:
    if win==3:print('your are ultimate winner');break
    if loss==3:print('your are ultimate looser');break
    print(f"win:{win}\t loss:{loss}\t tie:{tie}")
    print('enter R/rock p/paper s/scissors')
    player_choice = input().upper()
    stat1 = 'ROCK' if player_choice == 'R' else 'PAPER' if player_choice == 'P' else 'SCISSORS' if player_choice == 'S' else 'break'
    computer_choice = choice[random.randint(0,2)]
    stat2 = 'ROCK' if computer_choice == 'R' else 'PAPER' if computer_choice == 'P' else 'SCISSORS' if computer_choice == 'S' else 'break'
    if stat1 != 'break':
        print(f'{stat1} VERSUS...{stat2}')
    else:
        break
    result = winner(player_choice, computer_choice)
    print(f'guess what...{result}')
    print('wanna play agian...y?n')
    status = input().upper()
    if status == 'N':
        print(f"win:{win}\t loss:{loss}\t tie:{tie}")
        print('take care..:-(')
        break






