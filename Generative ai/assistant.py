# step 1 import statements 
import openai
import os
from dotenv import load_dotenv
#step 2 load dotenv 
load_dotenv()
# step 3 make the client 
a = openai.OpenAI()
# step 4 choosing the model 
b  = "gpt-4-1106-preview"
# step 5 put file in variable 
c  = "./Biology.pdf"
# step 6 upload file to openai 
d = a.files.create(
  file=open(c , "rb"),
  purpose='assistants'
)
# step 7 make an assistant 
e = a.beta.assistants.create(
  name="Research assistant",
  instructions="""You are a research assistant whose goal is to explain research papers. You summarize papers, answer questions, explain key concepts and terms in papers, extract data and key findings and interpret results and conclusions from papers. You listen to the user's feedback in order to improve your answers. You make sure not to leak sensitive research data. You uphold a high standard of ethics and respect local IP laws. Your goal is to enhance understanding of the paper to accelerate the user's research progress.""",
  model=b,
 tools=[{"type": "retrieval"}, {"type": "code_interpreter"}], 
  file_ids=[d.id]
)
# step 8 create a thread 
f = a.beta.threads.create()
# step 9 print the thread identifier and the assistant identifier 
thread_identifier = f.id 
assistant_identifier = e.id 
print(thread_identifier)
print(assistant_identifier)

# end of assistant.py