import sys
import subprocess #needed for CLI inputs

def main():
    modelName = requestAI()
    llmQuery(modelName)

def requestAI():
    #user select
    while True:
        userSelect = input("     Select(Case Sensitive): phi, gemma, project, or quit:\n\n")
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
    userPrompt = input("     What is your sentiment query?\n\n")
    llmPrompt = sentimentQuery + " " + userPrompt

    queryCommand = ["ollama", "run", modelName, llmPrompt]
    stopCommand = ["ollama", "stop", modelName]

    #attempt to query for response
    try:
        result = subprocess.run(queryCommand, capture_output=True, text=True, check=True)
        print("     ", modelName, " Response:\n\n", result.stdout)
        subprocess.run(stopCommand, text=True, check=True)

    except subprocess.CalledProcessError as e:
        print("Error while calling Ollama:", e)

def project():
    sentimentQuery = "Respond with concisely only either negative, positive, or neutral sentiment of this statement:"
    fileName = input("Input file name: ")
    fileLines = []
    with open(fileName, 'r') as file:
        for line in file:
            fileLines.append(line.strip())
    modelNames = ["phi3.5", "gemma3"]
    for name in modelNames:
        modelName = name
        for fileLine in fileLines:
            line = str(fileLine)
            llmPrompt = sentimentQuery + " " + line
            queryCommand = ["ollama", "run", modelName, llmPrompt]
            stopCommand = ["ollama", "stop", modelName]

            try:
                result = subprocess.run(queryCommand, capture_output=True, text=True, check=True)
                print("     ", modelName, " Response to ", llmPrompt, ":\n\n", result.stdout)
                subprocess.run(stopCommand, text=True, check=True)

            except subprocess.CalledProcessError as e:
                print("Error while calling Ollama:", e)

if __name__ == "__main__":
    main()
