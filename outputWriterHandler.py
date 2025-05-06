from webscraper import WebScraper
from llmprocessor import LlmProcessor

class OutputArticleTitles():
    def __init__(self, readFromFile): #instantiate with file input
        self.readFromFile = readFromFile

    def outputBusinessTitles(self, writeToFile):
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
            print(f"Error in outputBusinessTitles: {e}")

class outputLLM:
    def __init__(self, modelName, readFromFile):
        self.llm = LlmProcessor(modelName)
        self.readFromFile = readFromFile

    def outputSentimentAnalysis(self, writeToFile):
        try:
            llm = self.llm

            #clean the response text file
            cleanFile(writeToFile)

            #output articleTitles to fileWriteTo
            with open(self.readFromFile, 'r') as readFile:
                for line in readFile: #for each article title in the file input
                    llmResponse = llm.llmSentimentQuery(line) #retrieve the sentiment analysis
                    with open(writeToFile, 'a') as writeFile: #write llm response into output file
                        writeFile.write(llmResponse)

        except Exception as e:
            print(f"Error in outputBusinessTitles: {e}")

def cleanFile(fileName):
    try:
        with open(fileName, 'w') as writeFile:
            writeFile.write("")
    except Exception as e:
        print(f"Error in cleanFile: {e}")