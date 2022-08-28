from tkinter.filedialog import *
from tkinter.messagebox import *
import os

PATH = os.path.dirname(os.path.abspath(__file__))

def start_game():
    # Launch game executable : /bin/engine-sim-app.exe
    # If game executable not found, throw error
    game_file = os.path.join(PATH, "bin/engine-sim-app.exe")
    if not os.path.exists(game_file):
        showerror("Error", "Game executable not found\nPlease put the launcher in the game root directory")
    # Launch game executable
    os.chdir("bin/")
    os.system("engine-sim-app.exe")
    os.chdir("../")

def get_engine_engine_line(engine_file):
    # Get the line from .mr file that contains "engine engine"
    with open(engine_file, "r") as f:
        line_number = 0
        for line in f:
            if not "engine engine" in line:
                line_number += 1
            else:
                break
    return line_number

def get_engine_name(engine_file, engine_engine_line):
    # Get the name of the engine from the .mr file
    with open(engine_file, "r") as f:
        line_nb = engine_engine_line
        content = f.readlines()
        line = content[line_nb]
        while line_nb >= 0:
            line = content[line_nb]
            if "public node" in line:
                engine_name = line.split("public node ")[1].split(" ")[0]
                return engine_name
            line_nb -= 1

def modify_main_mr(engine_file, engine_name):
    # Modify main.mr file to use the selected engine
    main_mr_file = os.path.join(PATH, "assets\main.mr")
    with open(main_mr_file, "r") as f:
        content = f.readlines()
    
    # Find the line that contains "import engines/"
    line_number = 0
    for line in content:
        if 'import "engines/' in line:
            break
        line_number += 1
    
    # Modify the line to use the selected engine file
    content[line_number] = 'import "engines/' + engine_file + '"\n'

    # Find the line that contains "set_engine"
    line_number = 0
    for line in content:
        if 'set_engine' in line:
            break
        line_number += 1
    
    # Modify the line to use the selected engine name
    content[line_number + 1] = "    " + engine_name + "()\n"

    # Write the modified content to the main.mr file
    with open(main_mr_file, "w") as f:
        f.writelines(content)

def change_engine():
    # Open file dialog to select engine .mr file
    engine_file = askopenfilename(initialdir=PATH, title="Select engine .mr file", filetypes=(("engine .mr files", "*.mr"), ("all files", "*.*")))
    # If engine .mr file not selected, throw error
    if engine_file == "":
        showerror("Error", "No engine .mr file selected")
    else:
        try :
            engine_engine_line = get_engine_engine_line(engine_file)
            engine_name = get_engine_name(engine_file, engine_engine_line)
            engine_file_name = engine_file.split('assets/engines/')[-1]
            modify_main_mr(engine_file_name, engine_name)
        except Exception as e:
            showerror("Error", "Error while changing engine")
        else :
            showinfo("Success", "Engine changed")