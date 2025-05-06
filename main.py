# #Overview of Program 
# Main will create 2 objects: WebScraper, LlmProcessor
# - WebScraper is instantiated with a string url
#   - scrapeTitle() method will return a string array of articleTitles
# - LlmProcessor is instantiated with a string line
#   - 
# requestFile() - the menu for user to enter in a file name to read; output sting fileName
# requestLLM() - the menu for the user to select which LLM to use;  output string llmModel

import os
from outputWriterHandler import OutputArticleTitles #object for webscraping websites by URL
from llmprocessor import LlmProcessor #object for llm sentiment analysis

_llmList = ["phi3.5", "gemma3"]
_WEBSCRAPE_OUTPUT = "/TextFiles/txt_webscrape.txt"
_LLM_OUTPUT = "/TextFiles/txt_llmOutput.txt"


def main():
    fileName = requestFile()
    llmModel = requestLLM()

    outputArticles = OutputArticleTitles(fileName)
    outputArticles(_WEBSCRAPE_OUTPUT)

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

#request for LLM model or quit
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
