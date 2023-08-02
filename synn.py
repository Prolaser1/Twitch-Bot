from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pyautogui
import random 

#Setting up driver
#For PC
#driver = webdriver.Chrome(r'C:\Users\benwo\Documents\chromedriver\chromedriver.exe')
#For mac
driver = webdriver.Chrome(r'/Users/benworsley/Documents/chromedriver/chromedriver')
time.sleep(5)
driver.get('https://twitch.tv/synn/chat')

#Declaring variables
seen_messages = set()
key_list = ["!sraffle", "!raffle"]
#[RafflesEntered, RafflesWon]
RaffleList = [0,0]
x=1
while x !=101:
    sraffle = "!sraffle " + str(x)+'k'
    raffle = "!raffle " + str(x)+'k'
    key_list.append(sraffle)
    key_list.append(raffle)
    x += 1
    
    
def splitChat(chat):
    if chat.split(" ")[0] == "StreamElements":
        text = chat.split(" ")[1:]
        text = " ".join(text)
        return [chat.split(" ")[0], text]
    else:
        return chat.split(": ")
    
def enterRaffle():
    pyautogui.keyDown("shift")
    pyautogui.press('1')
    pyautogui.keyUp('shift')
    pyautogui.typewrite('join')
    pyautogui.press("enter")

def enterGiveaway():
    pyautogui.keyDown("shift")
    pyautogui.press('1')
    pyautogui.keyUp('shift')
    pyautogui.typewrite('ticket max')
    pyautogui.press("enter")
    
def DisplayRaffleInfo():
    print(f"Raffles Won = {RaffleList[1]}\nRaffles Entered = {RaffleList[0]}\nWinRate = {RaffleList[1]/RaffleList[0]*100}%")
    
def catchWin(chat):
    if chat[0] == 'StreamElements':
        text = chat[1].split(" ")
        if 'prolaser9000,' in text or 'prolaser9000' in text:
            print('WON RAFFLE')
            RaffleList[1] = RaffleList[1] +1 
            DisplayRaffleInfo()
            time.sleep(10)
            enterGiveaway()

def main():
    while x:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        chats = soup.find_all(class_='chat-line__message')
        for chat in chats:
            chat_list = splitChat(chat.text)
            if chat.text not in seen_messages:
                #print(f"{chat_list[0]} -> {chat_list[1]}")
                seen_messages.add(chat.text)       
                catchWin(chat_list)
            if chat_list[1] in key_list:
                print("RAFFLE ENTERING")
                RaffleList[0] = RaffleList[0] + 1
                time.sleep(random.randint(5, 20))
                enterRaffle()
                time.sleep(10)
                driver.refresh()
                chat_list.clear()
            
        time.sleep(1)
        
if __name__ == '__main__':
    main()
