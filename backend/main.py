from dotenv import load_dotenv
import os
load_dotenv()

from regex import new_transcript
from api import extract_features, generate_frd

def analyse_text(transcript):
    chunks = new_transcript(transcript)
    data = ""
    z = len(chunks)
    j = 0
    k = 0
    s = "API_KEY"
    for i in range(z):
        print(i)
        p = s+str(k)
        API_KEY = os.getenv(p)
        response = extract_features(chunks[i],API_KEY)
        data += response.text
        j += 1
        if j==15 :
            j = 0
            k = (k+1)%3
    clean_data =  data.replace("```", "")
    p = s+str(k)
    frd = generate_frd(clean_data,os.getenv(p))
    return frd.text







