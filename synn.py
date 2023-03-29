import undetected_chromedriver as webdriver
from bs4 import BeautifulSoup
import constants as const
import time
import pyautogui 

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={const.profile}")
driver = webdriver.Chrome(options=options, use_subprocess=True)
driver.get(const.streamer_chat)

x = True
seen_messages = set()
    
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
    
def sayHello():
    pyautogui.typewrite("Hey all")
    pyautogui.press("enter")

def main():
    while x:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        chats = soup.find_all(class_='chat-line__message')
        for chat in chats:
            chat_list = splitChat(chat.text)
            if chat.text not in seen_messages:
                print(f"{chat_list[0]} -> {chat_list[1]}")
                seen_messages.add(chat.text)
            if chat_list[1] in const.raffle_triggers:
                print("RAFFLE")
                time.sleep(5)
                enterRaffle()
                time.sleep(25)
                driver.refresh()
                chat_list.clear()
        time.sleep(1)
        
if __name__=="__main__":
    sayHello()
    main()
