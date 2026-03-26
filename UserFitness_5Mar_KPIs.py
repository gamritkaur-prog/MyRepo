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


total_users=len(df)
avg_age=df["Age"].mean()
min_escore=df["EngagementScore"].min()
max_escore=df["EngagementScore"].max()

st.info("KPIs")
kpi1,kpi2,kpi3,kpi4=st.columns(4)

with kpi1:
    st.metric(" 📊 Total Users",total_users)
with kpi2:
    st.metric("📊 Avergae Age",avg_age)
with kpi3:
    st.metric("📊 Min Engagement Score",min_escore)
with kpi4:
    st.metric(" 📊Max Engagement Score",max_escore)

st.info("KPIs with Filters")
gender=st.selectbox("Choose Gender",df["Gender"].unique(),key="gender_filter_1")
filter1=df[(df["Gender"]==gender)] #filter1 conta

total_users=len(filter1)
avg_age=filter1["Age"].mean()
min_escore=filter1["EngagementScore"].min()
max_escore=filter1["EngagementScore"].max()

kpi1,kpi2,kpi3,kpi4=st.columns(4)

with kpi1:
    st.metric("Total Users",total_users)
with kpi2:
    st.metric("Avergae Age",f"{avg_age:.2f}")
with kpi3:
    st.metric("Min Engagement Score",min_escore)
with kpi4:
    st.metric("Max Engagement Score",max_escore)


def kpi_card(title,value,subtitle=""):
    st.markdown(
        f"""
        <div style=" 
             padding:15px;
             border-radius:20px;
             background:rgba(125,234,232,0.4);
             border:1px solid rgba(255,0,0,1);
             box-shadow: 0 20px 20px rgba(0,255,0,0,1);
        ">
            <div style="font-size:14px; color:blue;"> {title}</div>
            <div style="font-size:40px;"> {value}</div>
            <div> {subtitle}</div>
        </div>
        """, unsafe_allow_html=True
    )

kpi1,kpi2,kpi3,kpi4=st.columns(4)

with kpi1:
    kpi_card(" 📊 Total Users",total_users,"")
with kpi2:
    kpi_card("📊 Avergae Age",f"{avg_age:.1f}")
with kpi3:
    kpi_card("📊 Min Score",min_escore)
with kpi4:
    kpi_card(" 📊Max  Score",max_escore)