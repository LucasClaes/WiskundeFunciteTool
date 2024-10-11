import threading

stop_event = threading.Event()
user_input = None

def input_handler():
    global user_input  # Globale variable voor user inputs
    while not stop_event.is_set():
        inp = input("Geef iets in: ")
        if inp.strip().lower() == 'exit':
            stop_event.set()  # Exit commando om thread af te sluiten
        else:
            user_input = inp  # Input opslaan voor later gebruik

def start_input_thread():
    keyboardThread = threading.Thread(target=input_handler)
    keyboardThread.start()
    