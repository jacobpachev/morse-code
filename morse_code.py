import os
import time
alphabet = {"A": "*-", "B": "-***", "C": "-*-*", "D": "-**", "E": "*", "F": "**-*", "G": "--*", "H": "****", "I": "**", "J": "*---", "K": "-*-", "L":"*-**", "M": "--", "N":"-*", "O": "---", "P": "*--*", "Q": "--*-", "R": "*-*", "S": "***", "T": "-", "U": "**-", "V": "***-", "W": "*--", "X": "-**-", "Y": "-*--", "Z": "--**", " ": " ", "0": "-----", "1": "*----", "2": "**---", "3": "***--", "4": "****-", "5": "*****", "6": "-****", "7": "--***", "8": "---**", "9": "---**", ".": "*-*-*-", ",": "--**--", ":":"---***", "?":"**--**"}
msg = str(input("Enter a message to be encoded into morse code: ")).upper()
morse_msg = []

def dot():
    os.system("./beep.sh 550 0.1s")
def dash():
    os.system("./beep.sh 550 0.3s")
for i in range(len(msg)):
    morse_msg.append(alphabet[msg[i]])
for i in range(len(morse_msg)):
    cur_char = morse_msg[i]
    for x in range(len(cur_char)):
        print(cur_char[x])
        if(cur_char[x] == "*"):
            dot()
        elif(cur_char[x] == "-"):
            dash()
        else:
            time.sleep(1)
    time.sleep(0.3)

