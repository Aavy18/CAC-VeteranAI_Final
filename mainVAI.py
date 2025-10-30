#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 15:22:32 2025

@authors: 
    tejaskashyap AavyanAnand

This is the main file for the CAC Veteran AI project
"""

import ollama
import tkinter as tk
from tkinter import scrolledtext
import webbrowser
#idk what these are 
from ollama import chat
from ollama import ChatResponse

class VAI:
    def __init__(self, root):
        self.root = root
        root.title("Veteran Counseling Chatbot")
        root.geometry('600x600')
        root.configure(bg = "navyblue")

        # Chat display box
        self.chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state="disabled", borderwidth=0)
        self.chat_box.pack(pady=10)
        #this is a filler phone number, sin a real situation, this would be 988
        self.temp_number = "+1"
        # Input text box
        self.text_area = tk.Entry(root, width=50, borderwidth=0)
        self.text_area.pack(pady=5)

        # Send button
        send_button = tk.Button(root, text="Send", command=self.handle_send, borderwidth=0,highlightthickness=0)
        send_button.pack(pady=5)

        #call button
        call_button = tk.Button(root, text= "Call 988 Suicide Helpline", command = lambda: self.call_number(self.temp_number),borderwidth=0,highlightthickness=0)
        call_button.pack()
    
    def handle_send(self):
        user_input = self.get_input()
        """Triggered when user presses Send."""
        #if the input is nothing, do nothing
        if not user_input:
            return
        # Display user message
        self.append_message("You", user_input)
        self.text_area.delete(0, tk.END)

        # Safety keyword check
        self.check_response(user_input, ["suicide", "kill myself", "end it", "hurt myself"])

        # Get AI response
        response = self.chat_response(user_input)
        self.append_message("VeteranAI", response)
    
    def append_message(self, sender, message):
        """
        Append a message to the ScrolledText chat box (keeps it read-only).
        """
        #unlockes the box
        self.chat_box.config(state="normal")
        #displays
        self.chat_box.insert(tk.END, f"{sender}: {message}\n\n")
        #closes
        self.chat_box.config(state="disabled")
        #scrolles to the very end after an input
        self.chat_box.see(tk.END)


    def pack_user_responses(self, user_input):
        """
        display user messages.
        """
        self.append_message("You", user_input)

    def pack_AI_response(self, ollama_response):
        """
        Display AI messages
        """
        self.append_message("VeteranAI", ollama_response)


    def get_input(self):
        """
        Retrieves and prints the text from the text object
        No params or returns
        """
        entered_text = self.text_area.get()
        print(f"Entered text: {entered_text}")
        return entered_text
    
    #ollama func
    def chat_response(self, user_input): 
        #please fix this function to include error handling and the corrrect imports
        self.response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_input}])
        return self.response["message"]["content"]
    
    def check_response(self, userIn, keywords):
        for word in keywords:
            if word in userIn.lower():
                #call suicide helpline; in reality, this would put the user on call with 988
                print("Callling 988")
                self.append_message("VeteranAI", "You look like you could be in distress - Calling 988")
                #currently, this is a filler number. In reality, this would be 988
                self.call_number(self.temp_number)
                break
    

    def call_number(self, number):
        """
        Open the macOS FaceTime dialer with a number.
        We researched ways to call people and came accros this in python docs
        https://docs.python.org/3/library/webbrowser.html
        """
        #needs to be on same wifi as phone/have same number as phone
        print(f"Calling {number}")
        try:
            webbrowser.open(f"tel:{number}")
            self.append_message("System", f"Opening dialer for {number}...")
        except Exception as e:
            self.append_message("System", f"Failed to open dialer: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    helper = VAI(root)
    root.mainloop()

