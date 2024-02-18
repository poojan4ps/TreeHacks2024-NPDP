import requests
import creds
import gradio as gr
import psycopg2

conn = psycopg2.connect(
    dbname='ehr_database',
    user='postgres',
    password='admin123',
    host='tree-hacks-ehr-data.cn8kq2284drd.us-east-1.rds.amazonaws.com',
    port='5432'
)

def summarize_ehr_records(prompt):
    headers, payload = make_paylaod(prompt)
    response = requests.post(creds.url , json=payload, headers=headers)
    data = response.json()
    

    insert_patient("8c85983a-a538-522f-bce0-03678b0fc7ce" , data['choices'][0]['text'])

def insert_patient(id , val):

    cur = conn.cursor()
    cur.execute("INSERT INTO ehr_summary (patient_id, summary) VALUES (%s, %s)", (id , val))
    conn.commit()
    cur.close()
    

def make_paylaod(prompt):
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer "+creds.api_key
    }
    
    payload = {
        "model": creds.model,
        "prompt": "<s>[INST] " + prompt  + " [/INST]",
        "max_tokens": creds.token_len,
        "stop": ["</s>", "[/INST]"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        
    }
    
    return headers , payload



input_string =  """
Patient Name: Lily Garcia
Date of Visit: December 10, 2023
Chief Complaint: Anxiety
History of Present Illness:
Lily Garcia, a 35-year-old female, presents with complaints of persistent feelings of worry, nervousness, and restlessness for the past several months. She reports difficulty concentrating, irritability, and trouble falling asleep at night.
Past Medical History:
Lily Garcia has a history of generalized anxiety disorder and depression. She takes medications for anxiety and attends therapy sessions regularly.
Family History:
There is a family history of anxiety and mood disorders.
Social History:
Lily Garcia works as a teacher and lives with her partner. She enjoys reading and spending time with her pets.
Physical Examination:
Vital signs are stable. The patient appears anxious but is cooperative and engages in conversation.
"""


prompt_data = "Summarize the above deatils of a paitent for a doctor make it short within 1024 chars"
summarize_ehr_records(str(input_string) +"  "+prompt_data)