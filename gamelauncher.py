import pickle as pk
import sys
from _colorize import ANSIColors as co
from pathlib import Path
import subprocess as sb
import time
games : str = ""
game_list =[]
def run_game(game_name,game_path):
    print(f"{co.GREEN}\nRUNNING {game_name}...{co.RESET}\n")
    sb.call([game_path],shell=True)
#Menu displays all the games, including options to add more games and remove them from the list
# adding a game will clear the screen
#initially the program has no list of games so, add_game function will run first...
#if the "list.bin" file contains any game, then the program will only start from menu()
# drag and drop shortcuts or program exe, or type it directly
# first before entering the file to list.bin, check its existence.
def read_games():
    global games, game_list
    #step 1: check list.bin file existence
    games = co.INTENSE_BLUE+"║"+" "*(55)+"║\n"+co.RESET
    if Path.exists("C:/Users/Public/Documents/gamelist.bin"):
        with open("C:/Users/Public/Documents/gamelist.bin","rb") as list_:
            try: #checking whether THE FILE EXISTS BUT THERE IS NO DATA (RAISES EOFError)
                game_list = pk.load(list_)
            except EOFError:
                return 404 #error 404 implies that there is no element in C:/Users/Public/Documents/gamelist.bin
            
            #the game list structure will be:
            # [NAME, PATH, ICON (EMOJI)]
            for i,j in enumerate(game_list,1):
                name = j[0] if len(j[0]) < 30 else j[0][:29]+"..."
                games += f"{co.INTENSE_BLUE}║{co.RESET}           {[i]}  {j[2]}  {name}{" "*(35-len(name))}{co.INTENSE_BLUE}║{co.RESET}\n" #Here j[0] => game name
            games += f"{co.INTENSE_BLUE}║"+" "*55+f"║\n╚═══════════════════════════════════════════════════════╝{co.RESET}"
    else:
        with open("C:/Users/Public/Documents/gamelist.bin","wb") as f:
            pass #create an empty file
        return 1 #  no games found then add_game function


def add_game():
    global game_list
    sb.run(["cls"],shell=True)
    print(rf"""{co.BLUE}      ▄████▄ ████▄  ████▄    ███  ██ ██████ ██     ██ 
      ██▄▄██ ██  ██ ██  ██   ██ ▀▄██ ██▄▄   ██ ▄█▄ ██ 
      ██  ██ ████▀  ████▀    ██   ██ ██▄▄▄▄  ▀██▀██▀
{co.RESET}""",end="")
    game_path = str(input("      * Drag and drop the game exe\n        or the shortcut file Here\n\n  >> "))
    game_path=game_path.strip('\"')
    if not Path.exists(game_path.strip('\"')):
        print(f"\n  Error :: The provided game path doesn't seem to exist...\n  {co.INTENSE_RED}RETURNING TO MAIN SCREEN{co.RESET}",end="")
        time.sleep(2)

        return 1
    
    game_name = str(input("\n* Enter Game name\n  >> "))
    if len(game_name) == 0:
        print(f"\n  Error :: Game name can not be left empty...\n  {co.INTENSE_RED}RETURNING TO MAIN SCREEN{co.RESET}",end="")
        time.sleep(2)

        return 1
    icon = str(input("\n* Enter one Emoji to use as Icon >> "))[0]
    if len(icon) == 0:
        print("* Using default Icon...")
        icon = "🎮" #default icon
    print(f"{co.GREEN}\n\n* GAME ADDED SUCCESSFULLY ✔ ...{co.RESET}")

    #adding game list.bin (truncating the whole file, entering the games_list at once)
    game_list.append([game_name,game_path,icon])
    with open("C:/Users/Public/Documents/gamelist.bin","wb") as list_:
        pk.dump(game_list,list_)
    time.sleep(2)

    return 0

def trash_game():
    global game_list
    game_index = int(input("\n* Choose the game from above options\n  >>"))
    try:
        del game_list[game_index-1]
        print(f"{co.RED}\n  GAME REMOVED...\n{co.RESET}")

        with open("C:/Users/Public/Documents/gamelist.bin","wb") as list_:
            pk.dump(game_list,list_)

        time.sleep(2)
        return 0
    except:
        print(f"{co.RED}\n  GAME COULD NOT BE REMOVED...\n{co.RESET}")
        time.sleep(2)
        return 1

def menu():
    global games
    sb.run(["cls"],shell=True)
    print(rf"{co.INTENSE_BLUE}╔═══════════════════════════════════════════════════════╗{co.RESET}")
    print(rf"""{co.INTENSE_BLUE}║{co.RESET}      ██████╗  █████╗ ███╗   ███╗███████╗███████╗      {co.INTENSE_BLUE}║{co.RESET}
{co.INTENSE_BLUE}║{co.RESET}     ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝      {co.INTENSE_BLUE}║{co.RESET}
{co.INTENSE_BLUE}║{co.RESET}     ██║  ███╗███████║██╔████╔██║█████╗  ███████╗      {co.INTENSE_BLUE}║{co.RESET}
{co.INTENSE_BLUE}║{co.RESET}     ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║      {co.INTENSE_BLUE}║{co.RESET}
{co.INTENSE_BLUE}║{co.RESET}     ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║      {co.INTENSE_BLUE}║{co.RESET}
{co.INTENSE_BLUE}║{co.RESET}      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝      {co.INTENSE_BLUE}║{co.RESET}
{co.RESET}""",end="")
    print(f"{co.INTENSE_BLUE}╠═════════ {co.INTENSE_GREEN}[+] ADD GAME{co.INTENSE_BLUE} ══════ {co.INTENSE_RED}[-] REMOVE GAME{co.INTENSE_BLUE} ═════════╣{co.RESET}")
    print(games)

if read_games() == 1:
    add_game()
while True:
    menu()
    try:
        choice = str(input(f"{co.BLUE}  >> "))[0] ; print(co.RESET)
    except:
        print(co.RESET)
        continue

    #checking whether choice can be converted into an integer or not:
    try:
        game_index = int(choice)-1
        if game_index in range(0,len(game_list)):
            run_game(game_list[game_index][0],game_list[game_index][1])
            time.sleep(1)
            continue
    except:
        pass
    if choice.lower() == "+":
        if add_game() == 0:
            read_games()
            continue
        else:
            continue
    elif choice.lower() == "-" :
        if len(game_list)!=0:
            if trash_game() == 1:
                continue # cz no changes were made in the list so not running read_games()
            else:
                read_games();
                sb.run(["cls"],shell=True); continue
        elif len(game_list) == 0:
            print(f"{co.RED}\n* THERE ARE NO GAMES IN THE LIST...{co.RESET}")
            time.sleep(2)
            continue
    elif choice.lower() == "x":
        break
    else:
        continue
sys.exit()
