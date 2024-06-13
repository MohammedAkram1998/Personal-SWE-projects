# step 1 imports 
import os
import re
import streamlit as streamlit 
from dotenv import load_dotenv
import openai
import time
# step 2 configure front end 
streamlit.set_page_config(
    page_title="Research assistant",
      page_icon=":smile:",
    layout="wide",
    initial_sidebar_state="expanded",)
# step 3 design the css 
def f_css():
    custom_css = """
    <style>
        /* Change the background color */
        body { background-color: #f0f2f6; }
        
        /* Style the main page title */
        .stApp h1 { color: #333; }
        
        /* Style chat input and messages */
        .stTextInput>div>div>input { color: #4a4a4a; background-color: #eef2f7; border-radius: 20px; }
        .chat-bubble { background-color: #e7e9ec; border-radius: 20px; }
        .stButton>button { border-radius: 20px; border: 1px solid #4A90E2; color: #fff; background-color: #4A90E2; }
        
        /* Style file uploader */
        .stFileUploader { border-radius: 20px; border: 2px dashed #4A90E2; color: #4A90E2; }
        
        /* Customize sidebar */
        .stSidebar { background-color: #fafbfc; }
        .stSidebar .sidebar-content { padding: 20px; }
        
        /* Adjust font sizes */
        .stMarkdown p, .stMarkdown li { font-size: 16px; }
    </style>
    """
    streamlit.markdown(custom_css, unsafe_allow_html=True)
f_css()
# step 4 set the variables 
assistant_id = "asst_iTl0T9huI56OyVyTxsyX9CUh"
thread_id = "thread_aQIikedwyY61nH5z6cYpd8O6"
llm = "gpt-4-1106-preview"  
# step 5 read the api key 
load_dotenv()
connection  = openai.OpenAI()
# step 6 configure session 
if not "session_active" in streamlit.session_state:
    streamlit.session_state.start_chat =  False

if not "thread_id" in streamlit.session_state:
    streamlit.session_state.thread_id =  None

# step 7 button to begin a research session 
button_clicked = streamlit.sidebar.button("Begin Research")
if button_clicked:
    streamlit.session_state.session_active = True
# step 8  create a new thread for the research session 
    thread_2 = connection .beta.threads.create()
    streamlit.session_state.thread_id = thread_2.id
# step 9 Make the title 
streamlit.markdown("<h1 style='color: #4A90E2;'>Researcher Assistant</h1>", unsafe_allow_html=True)
# step 10 make text cleaner 
def clean_text(t):
    text = re.sub(r'【\d+†source】', '', t)
    return text
# step 11 set up session defaults 
if streamlit.session_state.get('session_active', False):
    streamlit.session_state.setdefault('llm', llm) 
    streamlit.session_state.setdefault('messages', [])
# step 12 show existing messages 
    for i  in streamlit.session_state.get('messages', []):
     if "role" in i  and "content" in i:
        with streamlit.chat_message(i["role"]):
            streamlit.markdown(i["content"])
     else:
        placeholder_content = i.get("content", "Content is not available .")
        default_role = i.get("role", "user")  
        
        with streamlit.chat_message(default_role):
            streamlit.markdown(placeholder_content)
#step 13 make chat input for the researcher 
    input = streamlit.chat_input("Ready to Research?")
    if input is not None :
        streamlit.session_state.messages.append({"content": input  ,  "role": "user"})
        if input:  
           with streamlit.chat_message("user"):
            streamlit.markdown(input)
#step 14 add the researchers message 
        connection .beta.threads.messages.create(
         thread_id= streamlit.session_state.thread_id, content=input , role="user")
# step 15 make a run 
        r = connection .beta.threads.runs.create(
            assistant_id=assistant_id,
            thread_id=streamlit.session_state.thread_id,
            instructions="""Answer the researchers queries from the provided files.""")
# step 16 wait for assistant 
        while not r.status == "completed":
                time.sleep(0.5)
                r = connection .beta.threads.runs.retrieve(
                   run_id =r.id, thread_id=   streamlit.session_state.thread_id)
# step 17 get messages added by the assistant 
        messages = connection .beta.threads.messages.list(thread_id= streamlit.session_state.thread_id)
# step 18 display messages 
        for j in messages:
            if j.run_id != r.id:
              continue 
            if hasattr(j.content[0].text,   'value'):
               message_content = j.content[0].text.value
            else:
               message_content = j.content[0].text
            message_content_2 = clean_text(message_content)
            streamlit.session_state.messages.append({"role": "assistant", "content": message_content_2})
            colored_message = f"<p style='color: #4A90E2;'>{message_content_2}</p>"
            with streamlit.chat_message("assistant"):
                streamlit.markdown(message_content_2, unsafe_allow_html=True)
#end of application.py