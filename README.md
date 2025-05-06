# CS325 Project

Hello! This is a business article sentiment analyzer. By inputting in a text file of news websites, it will attempt to scrape and analyze the titles with a preloaded LLM. The output will be in the TextFiles folder.

NOTE: The web scraper may not work for specific websites that are designed differently or are protected. Your milage wil vary.

Currently, the LLMs preloaded are:
- Phi3.5
- Gemma3:4B

## Setting Up

1.	Go to [Anaconda]( https://www.anaconda.com/docs/getting-started/miniconda/install) and follow the instructions for download the most recent version for your device.
2.	Go to [Ollama](https://ollama.com/download) and download the most recent version for your device.
3.	Run Ollama.
4.	Enter these commands in the CLI to install the most recent version of phi3.5 and gemma3:4b
    - <code>ollama pull phi3.5</code>
    - <code>ollama pull gemma3:4b</code>
5.	Download the project files and locate them in the CLI.
6.	Import the .yaml file for the Conda environment and activate it.
    - <code>conda env create -f requirements.yaml</code>
    - <code>conda activate cs325project</code>
7.	Run the Python main.py script
    - <code>python main.py</code>
8.	Respond to the prompts and get results.