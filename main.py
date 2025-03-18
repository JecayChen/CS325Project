import sys
import subprocess #needed for CLI inputs

def main():
    modelName = requestAI()
    llmQuery(modelName)

def requestAI():
    #user select
    while True:
        userSelect = input("[Select(Case Sensitive): phi, gemma, project, or quit:]\n")
        if(userSelect == "quit"):
            quit()
        elif(userSelect == "phi"):
            return "phi3.5"
            break
        elif(userSelect == "gemma"):
            return "gemma3"
        elif(userSelect == "project"):
            project()
            return None
        else:
            continue

def llmQuery(modelName):
    #for when input is not set
    if modelName is None:
        sys.exit()
    
    #setup for CLI query
    sentimentQuery = "Respond with concisely only either negative, positive, or neutral sentiment of this statement:"
    userPrompt = input("[What is your sentiment query?]\n")
    llmPrompt = sentimentQuery + " " + userPrompt

    queryCommand = ["ollama", "run", modelName, llmPrompt]
    stopCommand = ["ollama", "stop", modelName]

    #attempt to query for response
    try:
        result = subprocess.run(queryCommand, capture_output=True, text=True, check=True)
        print("[", modelName, " Response:]\n\n", result.stdout)
        subprocess.run(stopCommand, text=True, check=True)

    except subprocess.CalledProcessError as e:
        print("[Error while calling Ollama:]", e)

#code for project requirements
def project():
    #prep for sentiment query
    sentimentQuery = "Respond with concisely only either negative, positive, or neutral sentiment of this statement:"

    #file reading
    fileName = input("[Input file name:]\n")
    fileLines = []
    with open(fileName, 'r') as file:
        for line in file:
            fileLines.append(line.strip())

    #clean response text
    with open('response.txt', 'w') as file:
            file.write("")

    #models being used
    modelNames = ["phi3.5", "gemma3"]

    #cycle through models
    for name in modelNames:
        modelName = name
        stopCommand = ["ollama", "stop", modelName]

        #cycle through text prompts
        for fileLine in fileLines:
            line = str(fileLine)
            llmPrompt = sentimentQuery + " " + line
            queryCommand = ["ollama", "run", modelName, llmPrompt]

            #llm query
            try:
                result = subprocess.run(queryCommand, capture_output=True, text=True, check=True)
                fileInput = "[" + modelName + " Response to \"" + line + "\":]\n" + result.stdout

                #write to file
                with open('response.txt', 'a') as file:
                    file.write(fileInput)

            except subprocess.CalledProcessError as e:
                print("[Error while calling Ollama:]", e)

        #stop llm running afterwards
        subprocess.run(stopCommand, text=True, check=True)

if __name__ == "__main__":
    main()
