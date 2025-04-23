# #Overview of Program 
# Main will create 2 objects: WebScraper, LlmProcessor
# - WebScraper is instantiated with a filename
#   - performing the scrapeTitle() method will output titles into a file
# - LlmProcessor is instantiated with a filename
#   - 
# requestFile() - the menu for user to enter in a file name to read
# requestLLM() - the menu for the user to select which LLM to use

import os
from webscraper import WebScraper #object for webscraping websites
from llmprocessor import LlmProcessor #object for llm sentiment analysis

_llmList = ["phi3.5", "gemma3"]
_WEBSITES_INPUT = "txt_websites.txt"
_WEBSCRAPE_OUTPUT = "txt_webscrape.txt"
_LLM_OUTPUT = "txt_llmOutput.txt"


def main():
    fileName = requestFile()
    llmModel = requestLLM()

#requests for file name or quit
def requestFile():
    while True:
        userInput = input("Please input a file name or 'quit':]\n") #ask user for name or quit

        #file validation or quitting program
        #if valid, returns the file path
        #else continue requesting
        if userInput == 'quit': #check to quit
            quit()
        elif os.path.isfile(userInput): #check and returns if true
            print("File Exists")
            return userInput
        else: #loop to beginning of userInput
            print("File Not Found")
            continue

def requestLLM():
    while True:
        print("Loaded LLM:")
        for llm in _llmList:
            print(f"{llm}")
        userInput = input("Please select a LLM to use or 'quit':")
        if userInput in _llmList:
            return userInput
        else:
            print("Invalid Input.")
            continue

if __name__ == "__main__":
    main()
