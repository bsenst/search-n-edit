import numpy as np
import pandas as pd

import streamlit as st

# Sample DataFrame
df = pd.read_csv("parsed_docx_en.csv", sep="#")
df_es = pd.read_csv("parsed_docx_es.csv", sep="#")

# Streamlit app
st.title("Search")

st.caption(
    "This search function is based on the following document:"
    " https://tbinternet.ohchr.org/_layouts/15/treatybodyexternal/Download.aspx?symbolno=CERD%2FC%2FURY%2FCO%2F21-23&Lang=en"
)

search_term = st.selectbox("Select a search term:", ["", "migrant", "indigenous", "workers"])
language = st.selectbox("Select a language:", ["English"])

# Filter the DataFrame based on the search term
if language == "English":
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
else:
    filtered_df = df_es[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

# Display the filtered DataFrame
if search_term:
    st.write(f"{len(filtered_df)} search results:")
    for row in filtered_df.iterrows():
        st.divider()
        for el in row[1][1:]:
            st.write(el)
