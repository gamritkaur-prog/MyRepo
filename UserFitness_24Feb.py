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

st.info("Interactive Analytics using Streamlit using Filters")
st.subheader("Using SLider")
l=st.slider("Select Range",min_value=1,max_value=6,step=1)
new_df1=df.head(l)
st.dataframe(new_df1)

st.subheader("Using Drop Down List")
selected_gender=st.selectbox("Choose Gender",df["Gender"].unique())
filtered_gender_df=df[(df["Gender"]==selected_gender)]
st.dataframe(filtered_gender_df)

selected_city=st.selectbox("Choose City",df["City"].unique())
filter_city_df=df[(df["City"]==selected_city)] #by user
st.dataframe(filter_city_df)

#Create- Use meaning full names
#subscription filter
selected_subscr=st.selectbox("Choose Subscription Type",df["SubscriptionType"].unique())
filtered_subscr_df=df[(df["SubscriptionType"]==selected_subscr)]
st.dataframe(filtered_subscr_df)

#Workout filters
selected_workout=st.selectbox("Choose Workout Type",df["WorkoutType"].unique())
filtered_workout_df=df[(df["WorkoutType"]==selected_workout)]
st.dataframe(filtered_workout_df)


st.info("Interactive Analytics using Streamlit using Drill Down")
#What if I want to see  Female having Premium Subscription
#Two Filters - First Select Gender, Then Select Subscription and then so data - TRY
gender=st.selectbox("Choose Gender",df["Gender"].unique(),key="gender_filter_1")
filter1=df[(df["Gender"]==gender)] #filter1 contain data based on gender

select_subscr=st.selectbox("Choose Subscription Type",df["SubscriptionType"].unique(),key="sub_1")
filter2=filter1[(filter1["SubscriptionType"]==select_subscr)]

workout=st.selectbox("Choose Workout Type",df["WorkoutType"].unique(),key="workout_1")
final_filter=filter2[(filter2["WorkoutType"]==workout)]
st.subheader(f"{gender} having {select_subscr} subscription and WorkoutType={workout}")

st.dataframe(final_filter)

#Streamlit assign unique ID based on label, position and type
# if two are same-conflict happens 


st.info("Interactive Analytics using Streamlit using Drill Down side by side")

#Create Columns
col1,col2,col3=st.columns(3)

with col1:
    gender=gender=st.selectbox("Choose Gender",df["Gender"].unique(),key="gender_filter_2")
with col2:
    select_subscr=st.selectbox("Choose Subscription Type",df["SubscriptionType"].unique(),key="sub_2")
with col3:
    workout=st.selectbox("Choose Workout Type",df["WorkoutType"].unique(),key="workout_2")

filter1=df[(df["Gender"]==gender)] #filter1 contain data based on gender
filter2=filter1[(filter1["SubscriptionType"]==select_subscr)]
final_filter=filter2[(filter2["WorkoutType"]==workout)]
st.subheader(f"{gender} having {select_subscr} subscription and WorkoutType={workout}")

st.dataframe(final_filter)


st.sidebar.selectbox("Choose Gender",df["Gender"].unique(),key="gender_filter_3")
st.sidebar.selectbox("Choose Subscription Type",df["SubscriptionType"].unique(),key="sub_3")


#Activity: Create Two or three columns