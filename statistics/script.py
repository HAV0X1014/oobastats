import json
import time
from modules.text_generation import encode
from modules.logging_colors import logger


with open('extensions/statistics/statistics.json', 'rt') as file:
        json_data = json.load(file)
        
def setup():
    logger.info(f'Statistics are being logged to statistics.json')

#run for every input received.
def input_modifier(user_input):
    #make a global variable for the start time
    global start_time
    start_time = time.time()
    #increment the count of prompts received
    json_data["prompts"] += 1
    #get the count of tokens in the prompt minus 1 for the empty token
    tokenCount = len(encode(user_input)[0])
    json_data["promptTokens"].append(tokenCount - 1)
    #get the count of characters in the prompt
    characterCount = str(len(user_input))
    json_data["promptCharacters"].append(characterCount)
    
    #write the in-memory JSON to disk to save it.
    with open('extensions/statistics/statistics.json', 'w') as filew:
        json.dump(json_data, filew, indent=1)
    #return the unmodified user input after finishing logging
    return user_input
    

#run for every output sent.
def output_modifier(output):
    #stop the generation timer as soon as possible
    end_time = time.time()
    #increment the count of responses sent
    json_data["responses"] += 1
    #get the count of tokens in the response minus one
    tokenCount = len(encode(output)[0])
    json_data["responseTokens"].append(tokenCount - 1)
    #get the count of characters in the prompt
    characterCount = str(len(output))
    json_data["responseCharacters"].append(characterCount)
    #add generation time to JSON
    elapsed_time = end_time - start_time
    json_data["generationTime"].append(elapsed_time)
    
    #write the in-memory JSON to disk to save it.
    with open('extensions/statistics/statistics.json', 'w') as filew:
        json.dump(json_data, filew, indent=1)
    #return the unmodified output after finishing logging
    return output
