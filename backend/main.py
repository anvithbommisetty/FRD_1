from dotenv import load_dotenv
import os
load_dotenv()

from regex import new_transcript
from api import extract_features, generate_frd

def analyse_text(transcript):
    chunks = new_transcript(transcript)
    data = ""
    totalChunks = len(chunks)
    currentRequests = 0
    currentApiKey = 0
    totalApiKeys = 3
    s = "API_KEY"
    for i in range(totalChunks):
        print(i)
        p = s+str(k)
        API_KEY = os.getenv(p)
        response = extract_features(chunks[i],API_KEY)
        data += response.text
        currentRequests+= 1
        if currentRequests==15 :
            currentRequests = 0
            currentApiKey = (currentApiKey+1)%totalApiKeys
    clean_data =  data.replace("```", "")
    p = s+str(currentApiKey)
    frd = generate_frd(clean_data,os.getenv(p))
    return frd.text







