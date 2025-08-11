from characters import Vampire , Boss , mostermine
            
#function for the fight, need improvements
def fight_module(Gamer, Enemy):
    print(" the fight is begin\n")
    while Gamer.hp > 0 and Enemy.hp>0:
         print("\n" + Gamer.name + ": "+ str(Gamer.hp) + " HP --- Monster" + str(Enemy.hp)+ " HP \n" )
         hit=Gamer.comb() 
         Enemy.hp -= max(hit-Enemy.defence, 0)           
         if Enemy.hp > 0 :
            HIT=Enemy.comb()
            Gamer.hp -= max(HIT-Gamer.defence, 0)
            if Gamer.hp <= 0:
             return print(" you have been defeted")
            else:
             Gamer.resetdef()
             continue
    else:
        Gamer.reset()
        return print( " the enemy has been defeted, you won")

#the funcion for the locations, it need to be dinamic( after the database) the dialogue and the story need improvements

def majoroffice():
    print("The Mayor sits at his desk, hands clasped.He strare at you with a half-smile, but his eyes are nervous.\n")
    print("MAYOR:I do't understand why you keep tormenting me with these insinuatuions...\nYOU:Enough lies,Mayor.I have proof that you covered up every single disappearence in this town.\n")
    while True:
         c=int(input("1-If you don't talk now, the next concil meeting will be yuor political funeral.\n2-Do the right thing-I could say you were forced...and save your skin.\n3-Talk or i will make yuo slip all the teeth!\n"))
         if c==1 or c==2:
              print("MAYORl: You don't know what you are asking me to do...This isn't about politics annymore.It's About survival.\n")
              d=int(input("1-I know you did it to protevt someone...but you protected monsters.\n2-How many families have yuo looked in the eye while lying to them?\n3-If you fall the vampires lose their shield.Do you want to be rembered as a hero or a coward?\n "))
              return True, print("Alright...There is a house...The DE VARNE mansion. If you want answers, go there. But...don't do it at night.\n")
         elif  c==3:
              print("Threatening me won't help you.You are out oof yoour depth, and you don't even see it.\n")
              d=int(input("1-Then sink with them.YOur choice.\n2-If I'mm out of my depth, then you are drowing with me.\n3-Fine don't talk...but when this blow up, your name will be the first on the list.\n"))
              return True, print("Alright...There is a house...The DE VARNE mansion. If you want answers, go there. But...don't do it at night.\n")
         else:
              continue

def tavern():
    print("The tavern reeks of smoke, sweat, and rotting wood.\nAfew patrons glance your way as you enter, then return to their drinks.\nThe waitress watches you from behind the counter, wary and silent.\n")
    print("WAITRESS: Hello, stranger. It's not often we see new faces around here. what brings you here?\n")
    while True:
         c=int(input("1-I'm here to find the missing girl. Was she a friend of yours?\n2-Just ppassing through, nothing important.\n3-I'm trying to understand what's going on in this town\n"))
         if c==1:
              print("WAITRESS(grows somber):Ah ... she was a dear friend of mine. she hasn't benen heard from in days and evryone here is worried.\nI hope you menage to find her\n")
              while True:
                   d=int(input("1-I'll do everything to help her.\n2-Maybe it's best not to poke around\n3-Telll me, do yuo know anything more?\n"))
                   if d==1:
                        print("WAITRESS: Thank you, truly. I'll just tell you this:\nthe doctor knows more than he lets on, but he's afraid of the mayor and the sheriff.Be careful with him\n")
                        return True, print("With a faint smile, the waitress grabs your arm. I don't know why...but i belive you cansave her.\nGood luck stranger")
                   elif d==2 or d==3:
                        return True, print("The waitress closes up, becomes evasive, and the conversdation ends without further information.\n")
                   else:
                        continue
         elif c==2 or c==3:
               return True, print("The waitress closes up, becomes evasive, and the conversdation ends without further information.\n") 
         else:
              continue
         
def sherif():
    print("The Sheriff's office is silent and stifling. A stale smell of tobacco lingers in the air.\nBehind a desk cluttered wuth papers and old revolvers, the Sheriff eyes you with a grim stare.\nHis badge glints faintly under the dum light.\n")
    print("SHERIFF:Who the hell do you think you are, barging in like this?\n")
    while True:
         c=int(input("1-You are hiding something.Care to explain why your hands are so dirty?\n2-(Throw holy water on him\n3-I'm here for the girl.And yuo are going to help me.\n"))
         if c==1 or c==3:
              print("SHERIFF:I don't know anything about that.And even if i did...you think I'd risk my neck fro this?\n")
              while True:
                   d=int(input("1-You are sccared. That means I'm close\n2-Help me, and you might just walk out of this alive\n3-(punch him in the face)\n"))
                   if d==1 or d==2:
                        print("SHERIFF:Okay!Okay!, enought!I'll tell you! The girl was taken to the old mansion up the hill.I didn't want to be part of this!\nThe mayor-he said it was the only way to keep the town safe!")
                        break
                   elif d==3:
                        print("I don't wanna hurt you Sheriff.Just tell me what i need to know")
                        print("SHERIFF: Go to the mansion...that's where they're keeping her.Or whatever's left of her.\nBut i never told you this- I was never here, you hear me?")
                        break
                   else:
                        continue
         elif c==2:
            print("SHERIFF:Okay!Okay!, enought!I'll tell you! The girl was taken to the old mansion up the hill.I didn't want to be part of this!\nThe mayor-he said it was the only way to keep the town safe!")
            break
         else:
              continue
    return True, print("You rio the sheriff's badge off his chest.\nYOU:Leave this town, now.Before I change my mind.\nSHERIff:I...I' m sorry iu didn't have choose")
              
def shop():
      with open("Eldharrow/dialogues/shop.txt", "r", encoding="utf-8") as file:
               story=file.read()
               print(story)
      return True
     
def doctor():
    print("You step into the doctor's study. The airsmells of alchool and old books. He loos up from his desk, startled by yuor presence.\n")
    print("DOCTOR:What are you doing here? I''m busy.\nUnless you are ddying, make it quick.\n")
    while True:
         c=int(input("1-I know you are hiding something.Talk\n2-Please...people are dying.i need to understand what's going on\n3-Sorry.I just need some answers.Quietly\n"))
         if c==1:
              print("DOCTOR:Then leave. I have patient who matter.\n")
              return True, print("He pusges you out firmly and slams the door in your face with out saying a word\n")
         elif c==2 or c==3:
              while True:
                  print("DOCTOR:They already told me to stay quiet. Mayor.. Sheriff. Said i was delusional.Spreading panic.I can't...\n")
                  d=int(input("1-Then just tell me what you saw. I won't say it come fromyou.\n2-So you are just going to let more people die?\n3-I understand.But i'm not walking away blind."))
                  if d==2:
                        print("You don't understand what i'm risking. This cpmversation is over.")
                        return True, print("He pusges you out firmly and slams the door in your face with out saying a word\n")
                  elif d==1 or d==3:
                         with open("Eldharrow/dialogues/doctor.txt", "r", encoding="utf-8") as file:
                          story=file.read()
                          print(story)
                          return True, print("You have my word Doctor - this nightmare will end.\n")
                  else:
                       continue
         else:
             continue   
         
def mine(Giocatore):
     Enemy=mostermine()
     with open("Eldharrow/dialogues/mine1.txt", "r", encoding="utf-8") as file:
               story=file.read()
               print(story)
     fight_module(Giocatore, Enemy)
     return True

def oldhouse(Giocatore):
    Enemy=Vampire()
    with open("Eldharrow/dialogues/oldhouse1.txt", "r", encoding="utf-8") as file:
               story=file.read()
               print(story)
    fight_module(Giocatore, Enemy)
    return True

def magione(Giocatore): 
    Enemy=Vampire()
    with open("Eldharrow/dialogues/Maison.txt", "r", encoding="utf-8") as file:
               story=file.read()
               print(story)
    fight_module(Giocatore, Enemy)
    return True
     
def cimitery(Giocatore):
    Enemy=Boss()
    fight_module(Giocatore,Enemy)
    return False