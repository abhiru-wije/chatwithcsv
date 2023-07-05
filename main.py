import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import pandas as pd
import os
import tempfile


def main():
    
    load_dotenv()
    
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")
        
    st.set_page_config(page_title="Ask Your CSV")
    st.header("Ask Your CSV")
    
    csv_file = st.file_uploader("Upload a csv file", type="csv")
    if csv_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(csv_file.getvalue())
        
        
        agent = create_csv_agent(OpenAI(temperature=0), tfile.name, Verbose=True)
        
        user_question = st.text_input("Ask a question about your csv:")
        
        if user_question is not None and user_question != "":
            with st.spinner(text="In Progress..."):
                st.write(agent.run(user_question))
    
if __name__ == "__main__":
    main()