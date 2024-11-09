import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from critique_LLM import get_enhanced_prompt
from SQL_query_LLM import get_SQL_query
from SQL_runtime_1 import sql_and_dataframe
from insight_LLM import get_insights
from plot_LLM import render_plot

def generate_response(question):
    enhanced_prompt = get_enhanced_prompt(question)
    print("Enhanced Prompt: ", enhanced_prompt)

    SQL_query = get_SQL_query(enhanced_prompt)
    print(SQL_query)

    dataframe = sql_and_dataframe(SQL_query)
    print(dataframe)

    Inference = get_insights(question, dataframe)
    print(Inference)

    
    
    return Inference, dataframe

st.title("Chat with Election Data")

# Get the chat input from the user
chat_input = st.text_input("Enter your Question : ", "")

# Generate the response and plot
if chat_input:
    response_text, df = generate_response(chat_input)
    
    # Display the response text
    st.write(response_text)


    # Display the dataframe
    st.dataframe(df)

    render_plot(df)
    if os.path.exists("output_plot.png"):
        st.title("Visualization Plot")
        st.image("output_plot.png")
        os.remove("output_plot.png")
    else:
        st.error("Failed to generate plot.")