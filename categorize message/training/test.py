from vectorize import clean_messages
from augment import get_messages
from unidecode import unidecode
import pandas as pd

if __name__ == '__main__':
    
    discord_msgs = get_messages()
    FILE_augmented_messages = open("resources/augmented_messages.txt", "r")

    augmented_msgs = FILE_augmented_messages.readlines()

    for i in range(len(augmented_msgs)):
        augmented_msgs[i] = augmented_msgs[i].replace("\n", "")
    
    temp = discord_msgs
    temp.extend(augmented_msgs)

    all_messages = []

    for msg in temp:
        if (len(msg) > 1) and (len(msg.split()) > 2):
            all_messages.append(msg)
    
 
    DF_all_msg = pd.DataFrame(all_messages)
    
    DF_all_msg.to_excel("resources/all_messages.xlsx")
    