import art

import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10]
choice='yes'
user_choice=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while user_choice=='y':
    print(art.logo)
    l_user = [random.choice(cards), random.choice(cards)]
    l_comp = [random.choice(cards), random.choice(cards)]
    sum_user = l_user[0] + l_user[1]
    sum_comp = l_comp[0] + l_comp[1]
    a=11;b=10
    while choice=='yes':
            print("Your cards: ", l_user, "\tSum: ", sum_user)
            print("Computer card: ", l_comp[0])
            if (a in l_user and b in l_user) or (a in l_comp and b in l_comp) :
                if sum_user==21:
                    print("Your cards: ", l_user, "\tSum: ", sum_user)
                    print("Computer cards: ", l_comp, "\tSum: ", sum_comp)
                    print("YOU WON!!")
                    break
                else:
                    print("Your cards: ", l_user, "\tSum: ", sum_user)
                    print("Computer cards: ", l_comp, "\tSum: ", sum_comp)
                    print("YOU LOST😞")
                    break

            elif sum_user>21 :
                if 11 in l_user:
                    l_user.remove(11)
                    l_user.append(1)
                    sum_user=sum(l_user)
                    if sum_user>21:
                        print("Your cards: ", l_user, "\tSum: ", sum_user)
                        print("Computer cards: ", l_comp, "\tSum: ", sum_comp)
                        print("YOU LOST😞")
                        break
                else:
                    print("Your cards: ", l_user, "\tSum: ", sum_user)
                    print("Computer cards: ", l_comp, "\tSum: ", sum_comp)
                    print("YOU LOST😞")
                    break
            choice=input("Do you want to draw cards, press 'yes' for yes or 'no' for pass: ")
            if choice=='yes':
                l_user.append(random.choice(cards))
                sum_user=sum(l_user)
            else:
                break
    while sum_comp<=17:
        l_comp.append(random.choice(cards))
        sum_comp=sum(l_comp)
    if sum_user<=21:
        if sum_comp>21:
            print("Your cards: ", l_user, "\tSum: ", sum_user)
            print("Computer cards: ", l_comp, "\tSum: ", sum_comp)
            print("Opponent went over. YOU WON!!")
        else:
            if sum_comp>sum_user:
                print("Your cards: ", l_user, "\tSum: ", sum_user)
                print("Computer cards: ", l_comp, "\tSum: ", sum_comp)
                print("YOU LOST😞")
            elif sum_comp<sum_user:
                print("Your cards: ", l_user, "\tSum: ", sum_user)
                print("Computer cards: ", l_comp, "\tSum: ", sum_comp)
                print("YOU WON!!")
            else:
                print("Your cards: ", l_user, "\tSum: ", sum_user)
                print("Computer cards: ", l_user, "\tSum: ", sum_comp)
                print("DRAW")
    choice='yes'
    user_choice=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")