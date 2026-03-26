import streamlit as st
import pandas as pd


df=pd.DataFrame({
    "Name":["Aman","Riyan","Jazz","Sara","Dj","Khushi"],
    "Subject":["Math","Math","Computer","Science","Math","Computer"],
    "Score":[78,92,89,65,88,71]
})
st.title("Student Score Board")

st.subheader("Student Data as Table")
st.table(df)

st.subheader("Student Data as Data Frame")
st.dataframe(df) # Search/Download

st.subheader("Show Data Information")
st.write(df.info())

st.subheader("Show Summary Statistics")
st.write(df.describe())

st.subheader("Mean Score")
st.write(df["Score"].mean())

st.header("Add Some Interactivity")
# we need to take input from user

st.subheader("Using Number Input")
limit=st.number_input("How Many Rows You Want To See?",min_value=1,max_value=6,step=1)
new_df=df.head(limit)
st.dataframe(new_df)

st.subheader("Using SLider")
l=st.slider("Select Range",min_value=1,max_value=6,step=1)
new_df1=df.head(l)
st.dataframe(new_df1)