class outputArticleTitles:
    def __init__(self):
        pass # TODO

    def outputBusinessTitles(fileWriteTo):
        #clean the response text file
        with open(_WEBSCRAPE_OUTPUT, 'w') as writeFile:
            writeFile.write("")

        #read the websites file
        with open(fileName, 'r') as readFile:
            for line in readFile: #for each website
                scrape = WebScraper(line) #check to see if its valid
                titleNames = scrape.scrapeTitles() #and scrape titles
                with open(_WEBSCRAPE_OUTPUT, 'a') as writeFile: #output file
                    writeFile.write(f"!Titles for {line}\n") #website name
                    for title in titleNames: #all the titles in website
                        writeFile.write(title + "\n")
                    writeFile.write("\n")

class outputLLM:
    def __init__(self):
        pass  # TODO
    def outputSentimentAnalysis():
        pass # TODO