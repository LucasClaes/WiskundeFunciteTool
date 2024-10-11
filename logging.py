import datetime
import os

# Maakt een log map aan als die nog niet bestaat
if not os.path.exists('logs'):
    os.makedirs('logs')

# Log bestand aanmaken
ct = datetime.datetime.now()
dt_string = ct.strftime("%Y-%m-%d_%H-%M-%S")
file_name = os.path.join('logs', f"{dt_string}_log.txt")  # Create file in 'logs' subfolder

# Log bestand maken bij het programma maken
with open(file_name, "w") as filehandle:
    filehandle.write("Log gestart op: " + ct.strftime("%Y-%m-%d %H:%M:%S") + "\n")

# Functie om logs in het bestand te schrijven
def log(message):
    ct = datetime.datetime.now()
    with open(file_name, "a") as filehandle:  # "a" for append mode
        filehandle.write(f"{ct.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
# Testjes

if __name__ == "__main__":
    log("First log message.")
    log("Second log message.")
