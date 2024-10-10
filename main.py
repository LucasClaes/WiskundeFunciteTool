import input_handling as ih
import logging as lg


def Main():
    while not ih.stop_event.is_set():
        if ih.user_input:
            print(f"Input testen: {ih.user_input}")
            ih.user_input = None  # User inputs na gebruik resetten
        ih.threading.Event().wait(0.1)  # Delay om thread niet te overbelasten

if __name__ == '__main__':
    ih.start_input_thread()  # Start de input handling thread
    Main()
