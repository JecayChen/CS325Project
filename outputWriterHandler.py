from Interfaces import WriterOutputProcessor
from webscraper import WebScraper
from llmprocessor import LlmProcessor

class OutputArticleTitles:
    def __init__(self, readFromFile:str): #instantiate with file input
        self.readFromFile = readFromFile

    def output(self, writeToFile:str)->None:
        try:
            #clean the response text file
            cleanFile(writeToFile)

            #output articleTitles to fileWriteTo
            with open(self.readFromFile, 'r') as readFile:
                for line in readFile: #for each website in the file input
                    scrape = WebScraper(line) #instantiate WebScraper with url
                    titleNames = scrape.scrapeTitles() #and scrape titles into an array

                    with open(writeToFile, 'a') as writeFile: #output file
                        for title in titleNames: #write all the titles in title array
                            writeFile.write(title + "\n")
                        writeFile.write("\n")
        except Exception as e:
            print(f"Error in OutputArticleTitles.output: {e}")

class OutputLLM:
    def __init__(self, modelName:str, readFromFile:str):
        self.llm = LlmProcessor(modelName)
        self.readFromFile = readFromFile

    def output(self, writeToFile:str)->None:
        try:
            #clean the response text file
            cleanFile(writeToFile)

            #output articleTitles to fileWriteTo
            with open(self.readFromFile, 'r') as readFile:
                for line in readFile: #for each article title in the file input
                    llmResponse = self.llm.llmSentimentQuery(line) #retrieve the sentiment analysis
                    
                    with open(writeToFile, 'a') as writeFile: #write llm response into output file
                        writeFile.write(llmResponse)

        except Exception as e:
            print(f"Error in OutputLLM.output: {e}")

def cleanFile(fileName:str)->None:
    try:
        with open(fileName, 'w') as writeFile:
            writeFile.write("")
    except Exception as e:
        print(f"Error in cleanFile: {e}")