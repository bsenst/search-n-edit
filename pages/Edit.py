import pandas as pd

import streamlit as st

# Sample DataFrame
df = pd.read_csv("parsed_docx.csv", sep="#")

# Streamlit app
st.title("Editor")

df_index = st.selectbox("Select a database element", [i for i in range(1, len(df))])

topheader = st.text_input("topheader", df.loc[df_index]["topheader"])
superheader = st.text_input("superheader", df.loc[df_index]["superheader"])
header = st.text_input("header", df.loc[df_index]["header"])
subheader = st.text_input("subheader", df.loc[df_index]["subheader"])
text = st.text_area("text", df.loc[df_index]["text"], height=150)

if st.button("Save entry"):
    st.write("Entry saved to database")
