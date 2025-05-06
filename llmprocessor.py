import subprocess #needed for CLI inputs
import re #regex

class LlmProcessor:
    def __init__(self, modelName):
        self.modelName = modelName

    def llmSentimentQuery(self, queryInput):
        modelName = self.modelName

        #prep for sentiment query
        sentimentPrep = "Respond concisely and without explanation of why with only either negative, positive, or neutral sentiment of this statement:" #specifying AI

        #query command
        llmPrompt = sentimentPrep + " " + queryInput
        queryCommand = ["ollama", "run", modelName, llmPrompt] #CLI input

        #llm query
        try:
            response = subprocess.run(queryCommand, capture_output=True, text=True, check=True) #retrieve response from ollama
            responseSummary = re.search(r"\b(positive|negative|neutral)\b", response.stdout.lower()) #regex search for one word sentiment
            sentiment = responseSummary.group(1) if responseSummary else "unknown"

            return f'[Response to "{queryInput.strip()}"] => {sentiment}\n' #output string

        except subprocess.CalledProcessError as e:
            print(f"[Error while calling Ollama: {e}]")
            return f'[Response to "{queryInput.strip()}"] => error\n'