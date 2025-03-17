# CS325 Project

## Setting Up

1. Go to [Ollama](https://ollama.com/download) and download the most recent version for your device.
2. Once Ollama is installed, enter these commands in the CLI to install the most recent version of phi3.5 and gemma3:4b
    - <code>ollama pull phi3.5</code>
    - <code>ollama pull gemma3:4b</code>
3. Download the project files and locate them in the CLI.
4. Import the .yaml file for the Conda environment and activate it.
    - <code>conda env create -f environment.yaml</code>
    - <code>conda activate cs325project</code>
5. Run the Python main.py script
    - <code>python main.py</code>
6. Respond to the prompts and get results.