# import ollama
import ollama
import requests

'''
define a function that requets the ollama api for a list of models
'''

def ollamalist():
    try:
        response = requests.get('http://localhost:11434/models')
        response.raise_for_status()  # Raise an error for bad responses
        models = response.json()
        return models
    except requests.exceptions.RequestException as e:
        print(f"Error fetching models: {e}")
        return []






# Not working code

# def ollamalist():
#     return ollama.list()

