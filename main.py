import threading
import input_handling
stop_event = threading.Event()
user_input = None




def input_handler():
    global user_input  # Globaale variable voor user inputs gebruiken
    while not stop_event.is_set():
        inp = input("Geef iets in: ")
        if inp.strip().lower() == 'exit':
            stop_event.set()  # Thread afsluiten bij het stop commando
        else:
            user_input = inp

# Keyboard thread starten
keyboardThread = threading.Thread(target=input_handler)
keyboardThread.start()

def Main():
    global user_input  # Globaale variable voor user inputs gebruiken
    while not stop_event.is_set():
        if user_input:
            print(f"Input testen: {user_input}")
            user_input = None  #Input resetten na gebruik

if __name__ == '__main__':
    Main()
