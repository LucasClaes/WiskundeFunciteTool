import input_handling as ih
import my_logging as lg
from sympy import symbols, solve

try:  # Probeer sympy te importeren
    from sympy import *
except ModuleNotFoundError:  # Als sympy niet geïnstalleerd is, doe het volgende
    message = "Sympy is niet geïnstalleerd.\nVoer \"pip install sympy\" uit om sympy te installeren."
    print(message)
    lg.log(message)
    lg.close_log()
except Exception as e:
    print("Oeps, er ging iets mis.")
    lg.log(e)
    lg.close_log()


def nulwaarde_berekenen(vergelijking_str):
    # Definieer de symbolen
    x, m = symbols('x m')

    # Maak de vergelijking
    vergelijking = eval(vergelijking_str)

    # Bereken de nulwaarden
    nulwaarde = solve(vergelijking, x)

    return nulwaarde


def Main():
    Check = True
    print("Geef een functie op: ")
    while not ih.stop_event.is_set():
        if ih.user_input:
            lg.log(f"Input: {ih.user_input}")
            
            try:
                # Bereken de nulwaarde van de functie
                nulwaarde = nulwaarde_berekenen(ih.user_input)
                print(f"De nulwaarde(s) van de functie is/zijn: {nulwaarde}")
                lg.log(f"Nulwaarde(s): {nulwaarde}")
            except Exception as e:
                print("Fout bij het berekenen van de nulwaarde.")
                Check = False

            if not Check:
                message = "Ingegeven functie was niet geldig"
                print(message), lg.log(message)
                Check = True

            print("\nGeef een functie op: ")    
            ih.user_input = None  # Reset gebruikersinvoer na gebruik
        
        ih.threading.Event().wait(0.1)  # Vertraging om input thread niet te overbelasten
    lg.log(f"")

if __name__ == '__main__':
    ih.start_input_thread()  # Start de invoer handling thread
    Main()
