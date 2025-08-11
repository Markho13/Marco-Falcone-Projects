from mapfile  import majoroffice , tavern , doctor, sherif ,shop, oldhouse, mine , magione, cimitery , fight_module
from characters import Hunter, Preist, Occult

class map:
    def __init__ (self,Giocatore): 
        self.Giocatore=Giocatore
        self.mapp={
         "town":{
             "majoroffice":{"play": majoroffice},
             "locanda":{ "play" : tavern},
             "docotr":{ "play": doctor}, 
             "sherif":{ "play": sherif },
             "shop":{"play" : shop}
             },
        "oldhouse":{"play":oldhouse},
        "magione":{"play" : magione},
        "mine":{ "play" : mine},
        "cimitery":{"play" : cimitery}
        }
    def C_travel(self):
        for b, i in enumerate(self.mapp.keys(), start=1 ):
            print(str(b) + " - " + i)
        while True:
            c=int(input("where do yuo wish to  travel?\n"))
            if c==1:
                for a, y in enumerate(self.mapp["town"], start=1):
                        print(str(a) + " - " + y)
                while True:
                        v=int(input("what location do yuo wish to visit in the town?\n"))
                        if v==1:
                            majoroffice()
                        elif v==2:
                            tavern()
                        elif v==3:
                            doctor()
                        elif v==4:
                             sherif()
                        elif v==5:
                            shop()
                        else:
                            continue
            elif c==2:
                oldhouse(self.Giocatore)
            elif c==3:
                magione(self.Giocatore)
            elif c==4:
                mine(self.Giocatore)
            elif c==5:
                cimitery(self.Giocatore)
            else:
                continue


#GAME CONTROL   #in future need to be more dinamic so it s will be an object
def game_control(Giocatore, Mapp):
    while True:
        c=int(input("1-travel\n2-inventary\n3-Status\n"))
        if c==1:
           Mapp.C_travel()
        elif c==2:
           Giocatore.seeinventary()
        elif c==3:
            print(Giocatore.name + "\n" + Giocatore.race + "\n" )
        else:
           continue



# introduzione, to use a txt file for don't get lost on the dialogue

def intro():
    print("The sound of the wheels splashing through mud and the creaking of the wood fills the silence as the cart makes its way along the road to the village.\n")
    name=input("what's yuor name?\n")
    while True:
        r=input("DRIVER:Sorry i m old, did you say " + name + "? \n(y,n) \n" ).lower()
        if r=="y":
            print("\nWelcome at Eldharrow " + name +".\n")
            break
        elif r=="n":
            name=input ("So what's ypur name?\n")          
        else:
            continue
    print("DRIVER:So...the Holy See has finally decided to act.\nFor years,there have been whispers of the disappearances, strange deaths...\nand now the vanishing of that poor girl.\ni knew her.A kind soul, a light in all this darkness.\nAnd the darkness took her.\n")
    print("\nI was born in Eldharrow.\nLeft as soon as i could.Not far enought, sadly.\nNow i ferry people back there, and each journey...feels like a sentence.\n")
    print("\nThere is something in that place.\nSomething that clutches your heart before you even see the gates.\nEvil doesn't hide there...you breath it in.\n")
    while True:
            c=input("And you? What did you sat you were,uhu?.\nH=Devilhunter\nA warrior forged in battle, trained to slay the unholy woth stell and willpower.Silent.Retentless.Unbreakable.\nP=Priest\nA servant of the holy See, bearer of sacred rites and divine flame.Brings healing, protection, and righteoys judgment.\nO=Occult-bound\nOne marked by forbidden forces.Channels dark magic at great personal cost.Powerful, unstable-and feared.\n").lower()
            if c=="h":
                race="hunter"
                r=input("you choose "+ race + "do you wanna confirm it? it s not possible to change race during the game\n(y/n)\n" ).lower()
                if r=="y":
                    ptempt=Hunter(name, race)
                    break
                else:
                    continue
            elif c=="p":
                race="preist"
                r=input("you choose "+ race + "do you wanna confirm it? it s not possible to change race during the game\n(y/n)\n" ).lower()
                if r=="y":
                    ptempt=Preist(name, race)
                    break
                else:
                    continue
            elif c=="o":
                race="occult"
                r=input("you choose "+ race + "do you wanna confirm it? it s not possible to change race during the game\n(y/n)\n" ).lower()
                if r=="y":
                    ptempt= Occult(name, race)
                    break
                else:
                    continue           
            else:
                continue
    print("DRIVER:We'll see if that is enough.\nBecause what you'll find down there...is sick,corrupted, merciless.\n")
    print("Here we are, Eldharrow, i wish you good luch" + name + "you'll need it\n")
    return ptempt

#primo capitolo

def cap1(Giocatore):
    print("The cart driver halts in front of the village entrance and turns toward you\nDRIVER:Here we are\n He says in a rough voice.\n")
    print("DRIVER:Good luck to you...and remember, some shadows are more than tricks of the eye.\nYou clomb down from the cart and find yourself facing a cluster of weathered wooden houses.\nthe air smells of old rain and spent smoke.\nYou dig throught you poket and find the letter sent to you by the Holy See, containing the details of yuor assignment.")
    while True:   
        c=int(input("select inventary from the game interface.?\n1-travel\n2-inventary\n3-Status\n"))
        if c==2:
            Giocatore.seeinventary()
            with open("Eldharrow/dialogues/letterHS.txt", "r", encoding="utf-8") as file:
               letter=file.read()
               print(letter)
            break
        else:
            continue
    print("\nYou slip the letter back into your cloak.\nAs you lift your gaze, a figure emerges from the village shadows.it's the Major\n")
    print("MAYOR:Welcome to Eldharrow! W e have been expecting you.\nIt is an honor to receive an envoy from the Holy See in our small and humble village.\nI shall make it my personal duty to assist you inevery way, and to ensure your stay is blessed with all the confort you may require.\n")
    print("You look around.The streets are almost deserted.\nthose few who remain slip away into the shadows, casting nervous glances from beneath their hoods.\nIt's not just silence that fills the air-it's dread.\nA quiet, crawling fear seeps from every stone, every shuttered window.\nomething dark has sunk its claws into this place...and it's still watching.\n")
    print("You open yuor mouth to speak, but the mayor leans in, cutting you off.\nHe brings his face close to yours and whispers:\n")
    print("MAYOR:Whatever else yuo wish to discuss...is better said in my office.\nAs you may have noticed, the people here don't take kindly to new faces-even those sent by the Holy See.\nI'd rather not have them too alarmed...Especiallu over something i'm quite sure you'll be disappointed not to find.")
    print("You step in the mayor's office and take a sit")
    print("MAYOR: People like you come to Eldharrow thinking they'll find monsters, mysteries, secrets to uncover.\nBut you know what they really find?\nBoredom.Silence.And a few squirrels that are to corious.\n")
    print("He smiles, setting more confortably into his worn leather chair.\nHe watches you, as trying to gauge how naive you are.")
    while True:
        d=int(input("1-If the town is really that quiet,I'll just accept it and won't bother anyone anymore.\n2-Your lies are tired as that chair.And they stink about the same.\n3-You are right.Maybe i'm just asking too many questions...\n"))
        if d==1 or d==3:
            print("MAYOR:There you go.Enjoy the peace.Eldharrow is a quiet place,as long as you don't dig too deep\n")
            while True:
                f=int(input("1-Before i go,tell me: the woods behind the town...is it really as quiet as they say?Or does someone prefer it that way?\n2-The deepest silences are hte ones that smell like fresh paint.\n3-The shadow do't forget.\n"))
                if f==1 or f==3:
                    print("MAYOR:You are not here on vacation.I know that.But be carefull:Eldharrow isn't a book to leaf through.\nIt's a wall that watches you.And walls, sometimes, fall on you.\n")
                    print("He stands and approches you")
                    print("MAYOR:The truth you seek...isn't ready to be found.\nAnd you are not ready ti bear it")
                    break
                elif f==2:
                    print("MAYOR:Enjoy your stay stranger.I wish you peaceful dreams.Because the night here...They can be long.\nYOU:I hope you sleep well yyo,Mayor.While you still can.")
                    break
                else :
                    continue
        elif d==2:
            print("MAYOR:You are not here on vacation.I know that.But be carefull:Eldharrow isn't a book to leaf through.\nIt's a wall that watches you.And walls, sometimes, fall on you.\n")
            print("He stands and approches you")
            print("MAYOR:The truth you seek...isn't ready to be found.\nAnd you are not ready ti bear it")
            break
        else:
            continue
    return  print(" The hunt is begin!")

        
    
    
