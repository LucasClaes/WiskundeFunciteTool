import threading

stop_event = threading.Event()
user_input = None

def input_handler():
    global user_input  # Global variable to store user input
    while not stop_event.is_set():
        inp = input("Geef iets in: ")
        if inp.strip().lower() == 'exit':
            stop_event.set()  # Exit command to stop the thread
        else:
            user_input = inp  # Store the input for later use

def start_input_thread():
    keyboardThread = threading.Thread(target=input_handler)
    keyboardThread.start()
    