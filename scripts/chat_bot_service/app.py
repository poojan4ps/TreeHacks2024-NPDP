import gradio as gr
import requests
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname='ehr_database',
    user='postgres',
    password='admin123',
    host='tree-hacks-ehr-data.cn8kq2284drd.us-east-1.rds.amazonaws.com',
    port='5432'
)
# Define your chatbot function
def chatbot(input_text):
    # Your chatbot logic here
   

    url = "https://api.together.xyz/v1/completions"

    payload = {
    "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "prompt": "<s>[INST] "+ input_text+ " [/INST]",
    "max_tokens": 100,
    "stop": ["</s>", "[/INST]"],
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "repetition_penalty": 1,
    "n": 1
    }
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer 1018dc73006cb81e2bde91a7b4667b122e8db39ece49d5815b91a7c4810fcb26"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data['choices'][0]['text']
    

# Create Gradio interface
iface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="AskMedi", allow_flagging=False)

# Launch Gradio interface
iface.launch(share=True)