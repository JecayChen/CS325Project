# #Overview of Program 
# Main will call for loading output objects: ArticleTitles and LLM
# requestFile() - the menu for user to enter in a file name to read; output sting fileName
# requestLLM() - the menu for the user to select which LLM to use;  output string llmModel

import os
import sys
from outputWriterHandler import OutputArticleTitles #object for outputting websites
from outputWriterHandler import OutputLLM #object for outputting llm response

_llmList = ["phi3.5", "gemma3"]
_WEBSCRAPE_OUTPUT = "TextFiles/txt_webscrape.txt"
_LLM_OUTPUT = "TextFiles/txt_llmOutput.txt"


def main():
    fileName = requestFile()
    llmModel = requestLLM()

    outputArticles = OutputArticleTitles(fileName)
    outputArticles.output(_WEBSCRAPE_OUTPUT)
    print(f"Web article titles written to {_WEBSCRAPE_OUTPUT}")

    outputLLMResponse = OutputLLM(llmModel, _WEBSCRAPE_OUTPUT)
    outputLLMResponse.output(_LLM_OUTPUT)
    print(f"LLM sentiment analysis written to {_LLM_OUTPUT}")

    print("Complete.")

#requests for file name or quit
def requestFile()->str:
    while True: #loop for a correct input
        userInput = input("Please input a file name or 'quit': ") #ask user for name or quit

        #file validation or quitting program
        #if valid, returns the file path
        #else continue requesting
        if userInput == 'quit': #check to quit
            sys.exit(0)
        elif os.path.isfile(userInput): #check and returns if true
            print("File Exists\n")
            return userInput
        else: #loop to beginning of userInput
            print("File Not Found\n")
            continue

#request for LLM model or quit
def requestLLM()->str:
    while True: #loop for a correct input
        print("Loaded LLM:") #preloaded llms
        for llm in _llmList:
            print(f"{llm}")

        userInput = input("\nPlease select a LLM to use or 'quit': ")

        if userInput == 'quit': #check to quit
            sys.exit(0)
        elif userInput in _llmList: #checks to see if it is a correct llm
            return userInput
        else:
            print("Invalid Input.")
            continue

if __name__ == "__main__":
    main()
