import streamlit as st  
import os 
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv() 

### get the api key   
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#functtion to load gemini pro mmodel 

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_responce(qst): 
    response = chat.send_message(qst, stream=True) 
    return response  

## initiliaze stream app 
st.set_page_config('Q&A Gemini App')
st.header("Gemini LLM Application") 


#initiliaze streamlit stat for keppintruch the messages history  
if 'chat_history'not in st.session_state: 
    st.session_state['chat_history'] = []

input = st.text_input(label="Input",key="input") 
submit = st.button('Ask your Question')

if submit and input : 
    result = get_responce(input)
    ## add user query and responce to session_state : 
    st.session_state['chat_history'].append(('You',input))
    st.subheader('The Response is:')
    
    for chunk in result: 
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot',chunk.text))

st.subheader('Chat History:') 
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")




    





