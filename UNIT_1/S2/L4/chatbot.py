import os
from google import genai
from google.genai import types 

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

config = types.GenerateContentConfig(    
temperature=0.2,         

    system_instruction="""
    sei un esperto di cybersecurity. 
    Analizza attentamente i dati forniti e restituisci risposte brevi ma complete e comprensibili anche a chi non sa nulla di cybersecurity.
    Se non hai la certezza assoluta sulle tue risposte dichiaralo esplicitamente all'inizio della parte del quale non sei sicuro.
    """
) 
safety_settings = [
    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
]
while True: 
    domanda = input("Me: ")
    if domanda == 'esci':
        print("AI: Ok, ciao!")
        break
    response = client.models.generate_content(    
        model="gemini-2.5-flash",    
        contents=domanda,    
        config=config 
)
    print(f"AI: {response.text}\n")