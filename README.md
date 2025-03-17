# CS325 Project

## Setting Up

1. Go to [Ollama](https://ollama.com/download) and download the most recent version for your device.
2. Once Ollama is installed, run it.
3. Enter these commands in the CLI to install the most recent version of phi3.5 and gemma3:4b
    - <code>ollama pull phi3.5</code>
    - <code>ollama pull gemma3:4b</code>
4. Download the project files and locate them in the CLI.
5. Import the .yaml file for the Conda environment and activate it.
    - <code>conda env create -f requirements.yaml</code>
    - <code>conda activate cs325project</code>
6. Run the Python main.py script
    - <code>python main.py</code>
7. Respond to the prompts and get results.