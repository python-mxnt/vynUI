# import ollama
import ollama

'''
get ollama to list all available model son host machine inside a function and
return the list in another file
'''

def ollamalist():
    return ollama.list()

