import random

symbol=('Clubs', 'Spades', 'Hearts', 'Diamonds')
number=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#cards 2-10 (their value is their number); J,Q,K -value 10, A-1 or 11 (whichever is more convenient)
value={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


#all cards
class Cards:
    def __init__(self,symbol,number):
        self.symbol=symbol
        self.number=number
    
    def __str__(self):
        return self.number +" of "+ self.symbol
 

#create a deck of cards
class Create_deck:
    def __init__(self):
        self.deck=[]
        for i in symbol:
            for j in number:
                self.deck.append(Cards(i,j))
    def extract_card(self):
        single_card=self.deck.pop()
        return single_card
    def shuffle(self):
        random.shuffle(self.deck)


#keeps track of the balance and the bet of the player     
class Balance:
    def __init__(self,balance):
        self.balance=balance
        self.bet=0
    def _balance_str(self):
        return "Your remaining balance is: "+self.balance
    def _bet_str(self):
        return self.bet
    def bet_won(self):
        self.balance+=self.bet
    def bet_lost(self):
        self.balance-=self.bet
    def __str__(self):
        return self.balance


#shows cards of the player and the dealer and keep track of the value and aces
class Hand :
    def __init__(self):
        self.hand=[]
        self.ace=0
        self.value=0
    #add card   
    def hit(self,card):
        self.hand.append(card) #card from extract_card
        self.value+=value[card.number]
        if card.number=='Ace':
            self.ace+=1
    #check ace value
    def check_ace(self):
        while self.ace>0 and self.value>21:
            self.value-=10
            self.ace-=1
    def __str__(self):
        hand=''
        for i in self.hand:
            hand+=i.__str__()+'\n'
        return hand +" Points "+ str(self.value)
    def clear(self):
        self.hand=[]
        self.value=0
        self.ace=0


#Functions
#-----------------------------------------------------------------------------       

#player goes bust (goes over 21)
def player_bust():
    balance.bet_lost()
    print("Player goes bust! Your balance is: " + str(balance.__str__()))
    player_hand.clear()
    dealer_hand.clear()


#player wins (has a higher value than the dealer)
def player_wins():
    balance.bet_won()
    print("Player won! Your balance is: " + str(balance.__str__()))
    player_hand.clear()
    dealer_hand.clear()

#dealer wins (has a higher value than the player)
def dealer_wins():
    balance.bet_lost()
    print("Dealer wins! Your balance is: " + str(balance.__str__()))
    player_hand.clear()
    dealer_hand.clear()

#dealer goes bust (goes over 21)
def dealer_bust():
    balance.bet_won()
    print("Dealer goes bust!")
    player_hand.clear()
    dealer_hand.clear()

#push (its a draw)
def push():
    print("Push (player and dealer are tied)! Your balance is: " + str(balance.__str__()))
    player_hand.clear()
    dealer_hand.clear()

#place a bet
def place_bet():
    valid=0
    while valid==0:
        balance.bet=int(input("Place your bet: "))
        if balance.bet<=balance.balance:
            valid=1
        else:
            print("Please type a valid value")
    


balance=Balance(int(input("How much money would you like to have? \n Please state your balance: ")))
deck=Create_deck()
player_hand=Hand()
dealer_hand=Hand()
deck.shuffle()

while balance.balance>0 or deck.deck!=[]:
    place_bet()
    player_hand.hit(deck.extract_card())
    dealer_hand.hit(deck.extract_card())
    player_hand.hit(deck.extract_card())
    player_hand.check_ace()
    print("Your cards are: " , end=" ")
    print(player_hand.__str__())
    print("\n The dealer's cards are: ",end=" " )
    print(dealer_hand.__str__())
    dealer_hand.hit(deck.extract_card())
    player_hand.check_ace()
    if player_hand.value==21:
        print("You have 21!")
        player_wins()
    elif player_hand.value>21:
        player_bust()
    else:
        hit=1
        while hit==1:
            response=input("Do you want another card? Type yes or no \n")
            if response=='yes':
                player_hand.hit(deck.extract_card())
                player_hand.check_ace()
                print("Your cards are: ", end=" ")
                print(player_hand.__str__())
            if response=='no':
                hit=0
            if response!='yes' and response!='no':
                print("Invalid response")
            player_hand.check_ace()
            if player_hand.value>21:
                hit=0
        player_hand.check_ace()
        if player_hand.value>21:
            player_bust()
        else: 
            print("The dealer's cards are: ",end=" " )
            print(dealer_hand.__str__())
            dealer_hand.check_ace()
            if dealer_hand.value>21:
                dealer_bust()
                player_wins()
            else:
                while dealer_hand.value<=16:
                    dealer_hand.hit(deck.extract_card())
                    dealer_hand.check_ace()
                dealer_hand.check_ace()
                print("The dealer's cards are: ",end=" " )
                print(dealer_hand.__str__())
                if dealer_hand.value>21:
                    dealer_bust()
                    player_wins()
                else:
                    if dealer_hand.value==player_hand.value:
                        push()
                    elif dealer_hand.value<player_hand.value:
                        player_wins()
                    elif dealer_hand.value>player_hand.value:
                        dealer_wins()
   
                








