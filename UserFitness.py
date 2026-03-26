import streamlit as st
import pandas as pd
import plotly.express as px

st.title ("User Fitness Track Board")

#uplaod the file
st.info("The File Type is CSV only")
uploaded_file=st.file_uploader("Upload your CSV File",type=["csv"])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.success("File Uploaded Successfully")
    st.subheader("Preview Data")
    st.dataframe(df)
else:
    st.warning("Please Upload Your CSV File")

#Show descriptive statisics
st.write(df.describe())


st.subheader("Using SLider")
l=st.slider("Select Range",min_value=1,max_value=6,step=1)
new_df1=df.head(l)
st.dataframe(new_df1)

fig=px.line(df,x=df["CaloriesBurned"])
st.plotly_chart(fig)

#Upload any data , show the data, Plot some of graphs using Matplotlib, seaborn or plotly