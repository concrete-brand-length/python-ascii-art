from pyfiglet import figlet_format
import termcolor

def ASCII_Art():

    print("Hello. This program allows you to create some ASCII art. Let's get started\n")
    text_choice = input("What message would you like to print: ")

    
    while True:
        color_options = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        print(f"\nColour Options: {color_options}")
        color_choice = input("What colour would you like: ")
        
        if color_choice not in color_options:
            print("Please only enter a valid color!: ")
        else:
            break

    while True:
        font_options = ["bulbhead", "digital", "doh", "dotmatrix", "isometric1", "isometric2", "slant"]
        print(f"Font Options: {font_options}")
        font_choice = input("Which font would you like: ")

        if font_choice not in font_options:
            print("Please only enter a valid font!")
        else:
            break

    return termcolor.colored(figlet_format(text_choice, font_choice), color_choice )

print(ASCII_Art())
