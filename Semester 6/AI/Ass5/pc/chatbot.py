from nltk.chat.util import Chat, reflections
from tkinter import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter
from tkinter import *

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"I need help",
        ["what kind of help you need"]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Akash Ranajkar. you can call me anytime!",]
    ],
    [
        r"Where are you from ?",
        ["From earth!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good, How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I am created today only",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"how to go to (.*)? ",
        ["Go to www.redbus.com and book ticket for %1",]

    ],
    [
        r"how to go to (.*)? ",
        ["Go to www.redbus.com and book ticket for %1",]

    ],
    
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
     [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)?",
        ["please ask proper question"]
    ],
]

def chat():
    print("Greetings! My name is Chatbot-T1, What is yours?.")
    Chatbot = Chat(pairs, reflections)
    Chatbot.converse()

# def openG():
#     print("Opening www.google.com")
#     driver = webdriver.Chrome()
#     driver.get("https://www.googe.com")
# def chat():
#     print("Hi! I am a chatbot ")
#     chat = Chat(pairs, reflections)
    
#     chat.converse()
    

if __name__ == "__main__":
    # root = Tk()

    # root.geometry('100x100+100+100')
    # root.title("Chatbot")
    # btn1 = Button(root, text="Chat", command=firstChatBot).grid(column=1, row=1)
    # root.mainloop()
    chat()
    