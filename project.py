import time
import random
Day=0
def print_pause(texts,delays):
    #this function prints text and pauses
    print(texts)
    time.sleep(delays)
def sleep(Day):
    # this function for sleepiing
    print_pause('You went to sleep',1)
    print_pause('You woke up on the next day',2)
    time = str(Day)
    print_pause('Today is the day Number '+time,1)
    return Day

def endingcalc(CH):
    #this function calculates the ending
    Ending=''
    CH = CH
    if CH == 0:
        Ending = 'Minerals'
        return Ending
    elif CH == 1:
        Ending ='Water'
        return Ending
    else:
        print('Hi')
def sleeping(choice1,choice2,Answer1,Answer2,Score):
    # this function is to make the user to choose one of two choices
    print(choice1)
    print(choice2)
    Y = 0
    ran = random.randint(0,10)
    Day = Answer1
    while Y == 0 :
        X =str(input('(please enter one or two)'))
        if X == '1' :
            Y = 0
            Day += 1
            sleep(Day)
            Score += -1
        elif X == '2' :
            print(Answer2)
            Score +=5
            Y = 1
            return int(Day) , int(Score)
        else:
            Y  = 0
    return Day

def print_score(Score):
    #This prints the score
    Score =str(Score)
    print('The score'+ Score)

def randomizer(random1x1,random1x2 , random2):
    #this function for randomizing
    randoms = random.randint(0,1)
    if randoms == 0 :
        ran = random.randint(0,1)
        if ran == 0 :
            print_pause(random1x1,2)
        elif ran == 1:
            print_pause(random1x2,2)
        X = (randoms,ran)
        return X
    elif randoms == 1 :
        print_pause(random2,2)
        X = randoms
        return X
    else:
        return False
def monster(N1,N2):
    #this chooses the type of monster
    Num1 = N1
    Num2 = N2
    Monster = random.randint(Num1,Num2)
    if Monster <= 3 :
        MonsterYN = False
        MonsterST = 'No'
        return MonsterYN , Monster , MonsterST
    elif Monster <= 7 :
        MonsterYN = True
        MonsterST = 'Fake'
        return MonsterYN , Monster , MonsterST
    elif Monster > 7 :
        MonsterYN = True
        MonsterST = 'Real'
        return MonsterYN , Monster , MonsterST
    else :
        return False

def end_game():
    #this function for ending the game
    Y =0
    ListY = ('yes','ye','y','ys','es')
    ListN = ('no','n')
    while Y == 0 :
        X = str(input('Please write Yes or No '))
        X = X.lower()
        print(X)
        if X in ListY :
            print_pause('Ready to start a new adventure',2)
            print('------------------------------')
            Y = 1
        elif X in ListN :
            print_pause('Thanks for joining our adventure',1)
            print_pause('Goodbye',1)
            return True
        elif X == 'how' :
            print_pause('one night',1)
            print_pause('Two days',1)
            return True
def run(MonsterYN,MonsterST,S1C1,S1C2,S1A1,S1A2,Score,Ending):
    #this function is for running
    print_pause('You are running from the  monster',2)
    Ending = Ending
    MonsterST = MonsterST
    Var = random.randint(1,10)
    MonsterYN = MonsterYN
    if Ending == 'Minerals' :
        EndingNO = 1
        EndingPL = 'Cave'
        EndingIT = 'Minerals'
        EndingITWS = 'The minerals were'
        z = 'were'
    elif Ending == 'Water' :
        EndingNO = 2
        EndingPL = 'Body of Water'
        EndingIT = 'Bottle of water'
        EndingITWS = 'The bottle of water was'
        z = 'was'
    if Var <= 2 or MonsterST =='Fake':
        if MonsterST =='Fake':
            print_pause('You looked back You saw that',2)
            print_pause('the monster was fake',1)
            print_pause(f'You went back to the {EndingPL}',1)
            print_pause(f'While going inside the {EndingPL} you have found',2)
            print_pause(f'The {EndingIT} that were on the list',2)
            print_pause('You went to the base',2)
            print_pause(f'{EndingITWS} very useful',2)
            print_pause('Mission complete',1)
            print_pause(f'You have got the {Ending} ending',2)
            print_pause(f'This ending is the good ending number {EndingNO}',2)
            print_pause('There are two good ending',2)
            end = end_game()
            if end == True:
                return end
            else:
                print('-----')
        elif MonsterST == 'Real' :
            print_pause('The monster caught you',2)
            print_pause('unfortunatly you have died',2)
            print_pause('GAME OVER',1)
            print_pause('Are you ready for another adventure',2)
            end = end_game()
            if end == True:
                return end
            else:
                print('-----')
        else:
            print('Hi')
    elif Var > 2 or MonsterST =='No':
        print_pause('you have ran successfully to your base',2)
        sleeping(S1C1,S1C2,S1A1,S1A2,Score)
    else:
        print('Hi')
def take_photo(MonsterST,Ending):
    # this function for taking a photo for the monster
    Ending = Ending
    MonsterST = MonsterST
    Var = random.randint(1,10)
    if Ending == 'Minerals' :
        EndingNO = 1
        EndingPL = 'Cave'
        EndingIT = 'Minerals'
        EndingITWS = 'The minerals were'
        z = 'were'
    elif Ending == 'Water' :
        EndingNO = 2
        EndingPL = 'Body of Water'
        EndingIT = 'Bottle of water'
        EndingITWS = 'The bottle of water was'
        z = 'was'
    if Var >=4 or MonsterST== 'Fake':
        print_pause('You have took the photo',1)
        print_pause('after that you ran back to the base',2)
        print_pause('you looked at the photo',2)
        if MonsterST == 'Fake' :
            print_pause('the photo was empty',1)
            print_pause(f'You went back to the {EndingPL}',2)
            print_pause('There was no trace of a monster',2)
            print_pause(f'You successfully took the {EndingIT}',2)
            print_pause(f'The {EndingIT} that {z} on the list',2)
            print_pause(f'{EndingITWS} very useful',2)
            print_pause('You went back to the base',2)
            print_pause('The {EndingIT} you have collected ',2)
            print_pause(f'{z} very usefull',1)
            print_pause('Mission complete',1)
            print_pause(f'You have got the {Ending} ending',2)
            print_pause('This ending is the good ending ',2)
            print_pause(f'number {str(EndingNO)}',1)
            print_pause('There are two good ending',2)
            print_pause('Are you ready for another adventure',2)
            end = end_game()
            if end == True:
                return end
            else:
                print('-----')
        elif MonsterST == 'Real':
            print_pause('The photo had a ',1)
            print_pause('detailed image of the creature',2)
            print_pause('You sent the photo ',1)
            print_pause('to the main base',1)
            print_pause('You waited for the signal',2)
            print_pause('You got the signal',1)
            print_pause('They told you to not continue',1)
            print_pause('Because it was too dangerous',2)
            print_pause('Mission paused',1)
            print_pause('You have got the "Dangerous" ending',2)
            print_pause('This is the only neutral ending',1)
            print_pause('Are you ready for another adventure',2)
            end = end_game()
            if end == True:
                return end
            else:
                print('-----')
        else:
            print('hi')
    elif Var <= 4 and MonsterST == 'Real':
        print_pause('The monster caught you',2)
        print_pause('unfortunatly you have died',2)
        print_pause('GAME OVER',1)
        print_pause('Are you ready for another adventure',2)
        end = end_game()
        if end == True:
            return end
        else:
            print('-----')
    else:
        print('Hi')
def sneak(MonsterST,MonsterYN,Ending):
    #this funtion for sneaking
    Ending = Ending
    MonsterST = MonsterST
    MonsterYN = MonsterYN
    Var = random.randint(1,10)
    if Ending == 'Minerals' :
        EndingNO = 1
        EndingPL = 'Cave'
        EndingIT = 'Minerals'
        EndingITWS = 'The minerals were'
        z = 'were'
    elif Ending == 'Water' :
        EndingNO = 2
        EndingPL = 'Body of Water'
        EndingIT = 'Bottle of water'
        EndingITWS = 'The bottle of water was'
        z = 'was'
    if MonsterST == 'Real':
        if Var <= 9:
            print_pause('The monster caught you',2)
            print_pause('unfortunatly you have died',2)
            print_pause('GAME OVER',1)
            print_pause('Are you ready for another adventure',2)
            end = end_game()
            if end == True:
                return end
            else:
                print('-----')
        elif Var > 9:
            print_pause('You have sneaked behind the monster',1)
            print_pause(f'then you took the {EndingIT}',2)
            print_pause('You went back to the base')
            print_pause(f'{EndingITWS} very usefull',2)
            print_pause('Mission complete',1)
            print_pause(f'You have got the {Ending} ending',2)
            print_pause(f'This ending is the good ending number {EndingNO}',2)
            print_pause('There are two good ending',2)
            print_pause('Are you ready for another adventure',2)
            end = end_game()
            if end == True:
                return end
            else:
                print('-----')
        else:
            print('Hi')
    elif MonsterST == 'Fake':
        print_pause('You tried to sneak',1)
        print_pause('After that you looked ',1)
        print_pause('and saw that there was no',2)
        print_pause('Monster in that place',1)
        print_pause(f'You went back to the  {EndingPL}',2)
        print_pause(f'then you took the {EndingIT}',2)
        print_pause('You went back to the base',1)
        print_pause(f'{EndingITWS} very usefull',2)
        print_pause('Mission complete',1)
        print_pause(f'You have got the {Ending} ending',2)
        print_pause(f'This ending is the good ending number {EndingNO}',2)
        print_pause('There are two good ending',2)
        print_pause('Are you ready for another adventure',2)
        end = end_game()
        if end == True:
            return end
        else:
            print('-----')
    else:
        print('Hi ')
while True :
    ListMYNMMST=monster(1,10)
    MonsterYN = ListMYNMMST[0]
    #Is there a monster True=Yes False=NO
    Monster =ListMYNMMST[1]
    #this is just for checking
    MonsterST = ListMYNMMST[2]
    #the state of the monster Fake=Fake monster Real=there is a monster
    Score = 10
    Day = 0
    Y = 0
    A = 0
    list_planets = ('TRAPPIST-1e','Kepler-452b')
    print_pause('Hi you are at planet '
                +random.choice(list_planets)+
                ' the year is 2200',2)
    print_pause('You have a hard mission',2)
    print_pause('Your mission is to find one of the items on the list',2)
    print_pause('Water or Minerals',1)
    print_pause('When you find them  ',2)
    print_pause('you need to get sample',1)
    print_pause('of the item to the ship',1)
    print_pause('After that you need to wait or a signal',2)
    print_pause('giving you the instructions for the next mission',2)
    print_pause('You are in your base right now ',2)
    print_pause('you can do one of two things',1)
    print_pause('First you can go to sleep',2)
    print_pause('Second you can to explore the zone near you base ',2)
    lDS1='Enter 1 to go inside'
    lDS2='Enter 2 to explore'
    ListDS=(sleeping(lDS1,lDS2,Day,'You have started exploring',Score))
    CN ='You have found a narrow cave'
    CW ='You have found a wide cave'
    BW ='You have found a body of water'
    ListCHCV =(randomizer(CN,CW,BW))
    ListCVBW =('Cave','water body')
    ListNRWI =('Narrow','wide')
    if ListCHCV == 1 :
        CH = ListCHCV
        CV = 90
    elif len(ListCHCV) == 2 :
        CH = ListCHCV[0]
        CV = ListCHCV[1]
    else :
        print('')
    MK = 0
    Z = 0
    end = ''
    End = ''
    Day = ListDS[0]
    Score = ListDS[1]
    Ending =endingcalc(CH)
    if CH == 0:
        print_pause(f'this cave is very {ListNRWI[CV]}',2)
        print_pause('You have the choice to',2)
        print_pause(f'First you can go inside the {ListNRWI[CV]} cave',2)
        print_pause('Second you can go Back to the base',2)
        ran = random.randint(0,9)
        while MK == 0:
            if CV == 0 :
                while Z == 0 :
                    print_pause('Enter 1 to go inside',1)
                    print_pause('Enter 2 to go back to base',1)
                    X = str(input('Please enter 1 or 2 '))
                    if X == '1' and ran > 2:
                        print_pause('While trying to go inside the cave',2)
                        print_pause('unfortunatly you have died',2)
                        print_pause('GAME OVER',1)
                        print_pause('Are you ready for another adventure',2)
                        print_score(Score)
                        End = end_game()
                        print (End)
                        if End == True :
                            m = 1
                            break
                        else:
                            print('')
                        Z = ''

                    elif X == '1' :
                        print_pause('While going inside',2)
                        print_pause('the cave you have found',1)
                        print_pause('The minerals that were on the list',2)
                        print_pause('You took them and went to the base',2)
                        print_pause('The minerals you have collected ',2)
                        print_pause('were very usefull',2)
                        print_pause('Mission complete',1)
                        print_pause('You have got the "Minerals" ending',2)
                        print_pause('This ending is the good ',2)
                        print_pause('ending number 1',2)
                        print_pause('There are two good ending',2)
                        print_pause('Are you ready for another adventure',2)
                        print_score(Score)
                        End = end_game()
                        if End == True :
                            break
                        Z = ''
                    elif X == '2':
                        lDS3 = 'Enter 2 to go to the cave'
                        lDS4 = 'You went to the cave'
                        ListDS= (sleeping(lDS1,lDS3,Day,lDS4,Score))
                        Day = ListDS[0]
                        Score = ListDS[1]
                    if End == True :
                        break
                Z = 1
            elif CV == 1:
                if MonsterYN == False :
                    print_pause('While going inside the cave you have found',2)
                    print_pause('The minerals that were on the list',2)
                    print_pause('You took them and went to the base',2)
                    print_pause('The minerals you have collected ',2)
                    print_pause('were very usefull',1)
                    print_pause('Mission complete',1)
                    print_pause('You have got the "Minerals" ending',2)
                    print_pause('This ending is the good ending number 1',2)
                    print_pause('There are two good ending',2)
                    print_pause('Are you ready for another adventure',2)
                    print_score(Score)
                    End = end_game()
                    if End == True :
                        break
                    else:
                        print('')
                elif MonsterYN == True:
                    if MonsterST == 'Real' :
                        print_pause('While going inside the cave ',2)
                        print_pause('You saw a strange silhouette',2)
                        print_pause('The silhouette does not',2)
                        print_pause('look like a human',1)
                        print_pause('Near the sillhouette you ',2)
                        print_pause('saw a bunch of minerals',2)
                        print_pause('You have three things to do',2)
                        print_pause('First move is to Run',1)
                        print_pause('Second move is to try taking a photo',2)
                        print_pause('Third move is to Sneak ',2)
                        print_pause('and take the minerals',1)
                        while A == 0 :
                            print_pause('Enter 1 to Run',2)
                            print_pause('Enter 2 to try taking the photo',2)
                            print_pause('Enter 3 to Sneak ',1)
                            X = str(input('Please enter your choice'))
                            if X == '1' :
                                MYN = MonsterYN
                                MST = MonsterST
                                lDS3 = 'Enter 2 to go to the cave'
                                lDS4 = 'You went to the cave'
                                D = Day
                                S = Score
                                E = Ending
                                end=run(MYN,MST,lDS1,lDS3,D,lDS4,S,E)
                                print_score(Score)
                                if end == True:
                                    break
                                else:
                                    print('---')
                                MonsterST = 'Fake'
                                MonsterYN = False
                            elif X == '2':
                                end = take_photo(MonsterST,Ending)
                                print_score(Score)
                                if end == True:
                                    break
                                else:
                                    print('---')
                            elif X == '3':
                                end =sneak(MonsterST,MonsterYN,Ending)
                                print_score(Score)
                                if end == True:
                                    break
                                else:
                                    print('---')
                            else:
                                print('Invalid input')
                    elif MonsterST == 'Fake':
                        print_pause('While going inside the cave ',2)
                        print_pause('You saw a strange silhouette',2)
                        print_pause('The silhouette does not',2)
                        print_pause('look like a human',1)
                        print_pause('Near the sillhouette you ',2)
                        print_pause('saw a bunch of mineral',2)
                        print_pause('You have three things to do',2)
                        print_pause('First move is to Run',1)
                        print_pause('Second move is to try taking a photo',2)
                        print_pause('Third move to Sneak ',2)
                        print_pause('and take the minerals',2)
                        while A == 0 :
                            print_pause('Enter 1 to Run',2)
                            print_pause('Enter 2 to try taking the photo',2)
                            print_pause('Enter 3 to Sneak ',1)
                            X = input('Please enter your choice')
                            if X == '1' :
                                MYN = MonsterYN
                                MST = MonsterST
                                re1 = 'Enter 1 to go inside'
                                re2 ='Enter 2 to go to the cave'
                                D = Day
                                re3 = 'You went back to the cave'
                                S = Score
                                E = Ending
                                end=run(MYN,MST,re1,re1,D,re3,S,E)
                                print_score(Score)
                                if end == True:
                                    break
                                else:
                                    print('---')
                                MonsterST = 'Fake'
                                MonsterYN = False
                            elif X == '2':
                                end =take_photo(MonsterST,Ending)
                                print_score(Score)
                                if end == True:
                                    break
                                else:
                                    print('---')
                            elif X == '3':
                                end =sneak(MonsterST,MonsterYN,Ending)
                                print('score')
                                if end == True:
                                    break
                                else:
                                    print('---')
                            else:
                                print('Invalid input')
                    else:
                        print('HI')
                        break
                else:
                    print('Hi')
                    break
            else:
                print('Hi')
                break
    elif CH == 1:
        print_pause('This is an item that is on the list',2)
        ListMYNMMST=monster(1,7)
        MonsterYN = ListMYNMMST[0]
        #Is there a monster True=Yes False=NO
        Monster =ListMYNMMST[1]
        #this is just for checking
        MonsterST = ListMYNMMST[2]
        # print(MonsterST)
        # print(Ending)
        if MonsterYN == False:
            print_pause('You had some bottles in',1)
            print_pause('in your backpack',2)
            print_pause('You have filled the bottles',2)
            print_pause('Successfully it had alot of',1)
            print_pause('Usefull information',1)
            print_pause('Mission complete',1)
            print_pause('You have got the "Water Bottle" ending',2)
            print_pause('This ending is the good ending number 2',2)
            print_pause('There are two good ending',2)
            print_pause('Are you ready for another adventure',2)
            print_score(Score)
            End = end_game()
            if End == True :
                break
            else:
                print('')
        elif MonsterYN == True :
            if MonsterST == 'Fake':
                print_pause('You saw a strange silhouette',2)
                print_pause('The silhouette does not look like a human',2)
                print_pause('The silhouette was near the body of water',2)
                print_pause('You have three things to do',2)
                print_pause('First move is to Run',1)
                print_pause('Second move is to try taking a photo',2)
                print_pause('Third move is to Sneak and take the Water',2)
            while A == 0 :
                print_pause('Enter 1 to Run',2)
                print_pause('Enter 2 to try taking the photo',2)
                print_pause('Enter 3 to Sneak ',1)
                X = str(input('Please enter your choice'))
                if X == '1' :
                    MYN =MonsterYN
                    MST=MonsterST
                    re1='Enter 1 to go inside'
                    re2='Enter 2 to go to the water'
                    D=Day
                    re3='You went back to the cave'
                    S=Score
                    E=Ending
                    end =run(MYN,MST,re1,re2,D,re3,S,E)
                    print_score(Score)
                    if end == True:
                        break
                    else:
                        print('---')
                    MonsterST = 'Fake'
                    MonsterYN = False
                elif X == '2':
                    end =take_photo(MonsterST,Ending)
                    print_score(Score)
                    if end == True:
                        break
                    else:
                        print('---')
                elif X == '3':
                    end =sneak(MonsterST,MonsterYN,Ending)
                    print_score(Score)
                    if end == True:
                        break
                    else:
                        print('---')
                else:
                    print('Invalid input')
            else:
                print('Hi')
                break
        else:
            print('Hi')
            break
    else:
        print('Hi')
        break
    if end == True or End == True :
        break
    else:
        print('')

