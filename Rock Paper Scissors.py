# A Python program for the Rock, Paper, Scissors game. 
import random



def rock_paper_scissors():
    throws = ('r', 'p', 's')
    cpu = random.choice(throws)
    cpu_score = 0
    player_score = 0    
    count = 1
    print()
    win = int(input('How many points does it take to win? '))
    print()
    
    while player_score < win and cpu_score < win:
        print()
        print('********************* ROUND # ' + str(count) + ' *********************')
        print()
        player = (input('Pick your throw: [r]ock, [p]aper, or [s]cissors?'))
        
        cpu = random.choice(throws)
        
        if player == cpu:
            print('Tie!')
            
        elif player == "r":
                if cpu == "p":
                    print('Computer threw paper, you lose!')
                    cpu_score += 1
                    count += 1
                else:
                    print('Computer threw scissors, you win!')
                    player_score += 1
                    count += 1
                    
        elif player == "p":
                if cpu == "s":
                    print('Computer threw scissors, you lose!')
                    cpu_score += 1
                    count += 1
                else:
                    print('Computer threw rock, you win!')
                    player_score += 1
                    count += 1
                    
        elif player == "s":
                if cpu == "r":
                    print('Computer threw rock, you lose!')
                    cpu_score += 1
                    count += 1
                else:
                    print('Computer threw paper, you win!')
                    player_score += 1
                    count += 1
        else:
            print("That's not a valid play.")
        
    
    print()
    print('Your score: ', player_score)
    print("Computer's score: ", cpu_score)
    
    print() 
    print('********************* GAME OVER ********************')
    print()
    
    if player_score > cpu_score:
        print('You win!')
    if cpu_score > player_score:
        print('Computer wins!')
        
        
        
        
        

        
def main():
    print('ROCK PAPER SCISSORS in Python')
    print()
    print('Rules: 1) Rock wins over Scissors.')
    print('       2) Scissors wins over Paper.')
    print('       3) Paper wins over Rock.')
    
    rock_paper_scissors()
    
main()
