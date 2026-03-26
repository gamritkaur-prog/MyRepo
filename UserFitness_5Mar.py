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

st.title("Tabbed Pane Layout")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "📈 Analytics",
    "📉 Visualization",
    "📝 Summary",
    "💡 Recommendations"
])

with tab1:
        st.write("Basic Information")
        st.dataframe(df)
with tab2: 
     st.write("Dataset Analytics")
     gender=st.selectbox("Choose Gender",df["Gender"].unique(),key="gender_filter_1")
     filter1=df[(df["Gender"]==gender)] #filter1 contain data based on gender
     st.dataframe(filter1)

with tab3: 
     st.write("Dataset Visualization")
with tab4: 
     st.write("Summary")
     
with tab5: 
     st.write("Recommendations")
