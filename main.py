# Overview of Program #
# 
#

import sys
import os
import subprocess #needed for CLI inputs
from webscraper import WebScraper #object for websraping websites
from llmprocessor import LlmProcessor #object for llm sentiment analysis

def main():
    fileName = requestFile()
    outputTitles(fileName)

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

def outputTitles(fileName):
    #clean the response text file
    with open('response.txt', 'w') as writeFile:
        writeFile.write("")

    #read the websites file
    with open(fileName, 'r') as readFile:
        for line in readFile: #for each website
            scrape = WebScraper(line) #check to see if its valid
            titleNames = scrape.scrapeTitles() #and scrape titles
            with open('response.txt', 'a') as writeFile: #output file
                writeFile.write(f"!Titles for {line}\n") #website name
                for title in titleNames: #all the titles in website
                    writeFile.write(title + "\n")
                writeFile.write("\n")

if __name__ == "__main__":
    main()
