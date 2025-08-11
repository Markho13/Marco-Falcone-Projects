# Main class for the player
class player:
    def __init__ (self, name, race):
        self.name=name
        self.race=race 
        self.charisma=0
        self.hp=100
        self.inventary={}
    def seeinventary(self):
        print("INVENTARY:\n")
        for i in self.inventary.items():
            print("-", i,)       
                                                           #aggiungere usa lo strumento
    def newoblect(self,obj,descr,quant):
        print("You got " + obj + "\n")
        self.inventary[obj]={
            "description":descr,
            "quantity":quant
        }
    def useobj(self, obj,):
        print("you used "+obj+" \n" )
        del self.inventary[obj]
                                                            #rendere l'inventario dinamico e correggerlo
#subclasses      
class Hunter(player):
    def __init__(self, name,race):
        super().__init__(name, race)
        self.defence=10
        self.stamina=30
    def resetdef(self):
        self.defence=10
    def reset(self):
        self.defence=15
        self.stamina=35
        self.hp=100
    def comb(self):
        while True:
            a=int(input("1-use gun\n2-use knife\n3-defence\n"))
            if a==1:
                print("shot with the gun\n")
                return 60
            elif a==2:
                print("Stab with the knife\n")
                return 30
                #self.stamina -= 10
            elif a==3:
                print(" protect yuor self and take back stamina")
                self.defence +=5
                self.stamina +=15
            else:
                pass
class Preist(player):
    def __init__(self, name,race):
        super().__init__(name, race)
        self.defence=20
        self.stamina=40
    def resetdef(self):
        self.defence=20
    def reset(self):
        self.defence=15
        self.stamina=35
        self.hp=100
    def comb(self):

        while True:
            a=int(input("1-use gun\n2-use knife\n3-defence\n"))
            if a==1:
                print("shot with the gun\n")
                return 60
            elif a==2:
                print("Stab with the knife\n")
                return 30
                #self.stamana -= 10
            elif a==3:
                print(" protect yuor self and take back stamina")
                self.defence +=5
                self.stamina +=15
            else:
                pass
class Occult(player):
    def __init__(self, name,race):
        super().__init__(name, race)
        self.defence=15
        self.stamina=35
    def resetdef(self):
        self.defence=20
    def reset(self):
        self.defence=15
        self.stamina=35
        self.hp=100
    def comb (self):    
        while True:
            a=int(input("1-use gun\n2-use knife\n3-defence\n"))
            if a==1:
                print("shot with the gun\n")
                return 60
            elif a==2:
                print("Stab with the knife\n")
                return 30 
            elif a==3:
                print(" protect yuor self and take back stamina")
                self.defence +=5
                self.stamina +=15
            else:
                pass

# for the next step of the game, dinamic npg
#class NPG:
 #   def __init__ (self, name, dstory, relation, place) :
        #self.name= name
       # self.dstory=dstory
       # self.relation=relation
      #  self.place=place

# class monsters
class Vampire:
    def __init__ (self):
        self.hp=150
        self.defence=30
        self.stamina=50
    def comb (self):
        print("the Vampire attack you\n")
        return 60   
        
                                                       #create a fight function for the monsters that use stamina and take choose
class mostermine:
    def __init__ (self):
        self.hp=300
        self.defence=50
        self.stamina=100
    def comb (self):    
        print("the Vampire attack you\n")
        return 60

class Boss:
    def __init__ (self):
        self.hp=200
        self.defence=35
        self.stamina=75
    def comb (self):    
        print("the Vampire attack you\n")
        return 60   
