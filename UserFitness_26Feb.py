import streamlit as st
import pandas as pd


st.title ("User Fitness Track Board")

#uplaod the file
st.info("The File Type is CSV only")
uploaded_file=st.file_uploader("Upload your CSV File",type=["csv"])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.success("File Uploaded Successfully")

else:
    st.warning("Please Upload Your CSV File")


# To display raw data, insights, expanations and other details
st.info("Using  Check for Interactivity (Hide and Show)")

if st.checkbox("Preview Data"): #if user clicked the checkbox
    st.subheader("Preview Data")
    st.dataframe(df)

if st.sidebar.checkbox("Preview Data"): #if user clicked the checkbox
    st.subheader("Preview Data")
    st.dataframe(df)

st.info("Using Radio for Interactivity (Hide and Show)")
option=st.radio("Choose View",["Table","Chart","Statistics"])

if option=="Table":
    st.subheader("Preview Data")
    st.dataframe(df)
elif option=="Chart":
    st.bar_chart(df.set_index("Gender")["Age"])
elif option=="Statistics":
    st.subheader("Summary Statistics")
    st.write(df.describe())

# To display raw data, insights, explanations and other details
with st.expander("Preview Data"):
    st.dataframe(df)

with st.expander("Age Wise ENgagement Score"):
    st.line_chart(df.set_index("Age")["EngagementScore"])

with st.expander("Engagements Insight"):
    option=st.radio("Choose View",["Gender Wise","Age Wise","Subscription Wise"])
    if option=="Gender Wise":
        st.bar_chart(df.set_index("Gender")["EngagementScore"])
    elif option=="Age Wise":
        st.line_chart(df.set_index("Age")["EngagementScore"])
    elif option=="Subscription Wise":
        st.bar_chart(df.set_index("SubscriptionType")["EngagementScore"])



    