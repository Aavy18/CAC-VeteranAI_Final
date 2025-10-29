# CACVeteranAI
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![AI Model](https://img.shields.io/badge/Model-Mistral-yellow)

CAC Veteran AI, or VAI for short, is a submission to the Congressional App Challenge made by Aavyan Anand and Tejas Kashyap

Table of Contents:
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

-------------------------------
## Overview
-------------------------------

VAI (Veteran AI) is designed to provide accessible emotional support and guidance to military veterans using AI technology. 
It creates a safe space where veterans can express their thoughts and receive compassionate, automated responses. 
It also includes emergency keyword detection that can connect users to crisis resources, like 988 Suicide and Crisis Lifeline.

-------------------------------
## Features
-------------------------------
- AI Counseling Chat – Uses Ollama + Mistral for local, private responses
  
- Tkinter GUI – Simple and intuitive interface
  
- Crisis Keyword Detection – Detects words like “suicide” or “hurt myself”
  
- Automated Call Function – Connects to crisis helpline when triggered
  
- Privacy-First – All processing is local with Ollama (no cloud data storage)


-------------------------------
## Requirements
-------------------------------
- **Python 3.10+**
- Ollama (local AI runtime)
- Internet connection for first-time model pull

-------------------------------
## Setup:
-------------------------------
Install Python 3.10+
-------------------------------
https://www.python.org/downloads/
We need Python 3.10+ to run properly

-------------------------------
Install Required Libraries
-------------------------------
Install ollama and tkinter(tk)

Use:
```bash
pip install tk ollama
```

-------------------------------
Install Ollama
-------------------------------
Download Ollama from:
https://ollama.com/download

Once installed, verify it works by running:
ollama --version

-------------------------------
Download Mistral Model
-------------------------------
VAI uses the “Mistral” model for its responses.

In Terminal, type:
```bash
ollama pull mistral
```

This will download the AI model locally (only required once).

-------------------------------
Running Program
-------------------------------
Make sure you are running terminal in the same folder as mainVai.py
See usage for example demo

-------------------------------
Troubleshooting
-------------------------------
If you get “Ollama not found” errors:
  • Make sure Ollama is running in the background.
  • On Mac, open the Ollama app manually once before using it in Python.

-------------------------------
Notes
-------------------------------
In this demo, the “Call” button dials a placeholder number.  
In a real deployment, this would call 988 (Suicide and Crisis Lifeline).

--------------------------------------------------------------
## Usage
--------------------------------------------------------------

Program use:
1. When you run the project, you will see a graphical display(using Tkinter).
2. Enter information in the text box and click send
3. Wait for AI to respond
4. If you say one of the keywords, it will call a number(in real use, this would be 988 Suicide and Crisis Lifeline)
5. Close the window to be done
Ex:
<img width="598" height="625" alt="Screenshot 2025-10-28 at 6 38 12 PM" src="https://github.com/user-attachments/assets/a5a9cd5d-bdb4-47b1-8526-aa0033f1ad6d" />


There are multiple files in this project; the only script to run is the mainVai.py file. All the other scripts have snippets of code and cannot run the full projects.


--------------------------------------------------------------
## License
--------------------------------------------------------------
MIT License

Copyright <2025> <Aavyan Anand and Tejas Kashyap>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


