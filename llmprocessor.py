import subprocess #needed for CLI inputs
import re #regex

class LlmProcessor:
    def __init__(self, modelName):
        self.modelName = modelName

    def llmSentimentQuery(self, queryInput):
        modelName = self.modelName

        #prep for sentiment query
        sentimentPrep = "Respond with concisely only either negative, positive, or neutral sentiment of this statement:" #specifying AI

        #query command
        llmPrompt = sentimentPrep + " " + queryInput
        queryCommand = ["ollama", "run", modelName, llmPrompt] #CLI input

        #llm query
        try:
            response = subprocess.run(queryCommand, capture_output=True, text=True, check=True) #retrieve response from ollama
            responseSummary = re.search(r"\b(positive|negative|neutral)\b", response.stdout.lower()) #regex search for one word sentiment

            return "[Response to \"" + queryInput + "\":]\n" + responseSummary #output string

        except subprocess.CalledProcessError as e:
            print(f"[Error while calling Ollama: {e}]")