from game_functions import intro , cap1, game_control, map
from characters import player, Hunter , Preist, Occult

# choose of the name and the class
Giocatore = intro()
Mapp=map (Giocatore)
# add object ot the player's inventary
Giocatore.inventary["letter's Holy See"]="Eldharrow/dialogues/letterHS.txt" 
# tutorial for inventary and map ( need to be update abput map)
cap1(Giocatore)
# function for the gamecontrol
while True:
    play=game_control(Giocatore, Mapp)
    if play==False:
       break
#end of the game
print("The evil has been puryfied on Eldharrow")
    