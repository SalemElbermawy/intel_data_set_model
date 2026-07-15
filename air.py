import streamlit as st
import pandas as pd
import joblib


st.set_page_config(page_icon="✈️",page_title="Air Plane")

# load model

@st.cache_resource

def load_model_air():
    
    model=joblib.load("air.pkl")
    
    return model

with st.spinner("model is downloading ... ") :
    try:
        loaded_model=load_model_air()
        st.success("Model downloaded !!!")
        
    except:
        st.error("Model Faild !!")
        

st.title("AirPlane Satisfaction")

st.header("Just enter the next value to get the result")


gender=st.selectbox("Select the gender",options=["Male","Female"])

customer_type=st.selectbox("Select Customer Type",options=["Loyal Customer","disloyal Customer"])

age=st.number_input("Enter your age",min_value=0,max_value=100)

type_of_travel=st.selectbox("Choose the type of travel",options=["Personal Travel","Business travel",])

class_type=st.selectbox("Class Type",options=["Eco Plus","Business",])

flight_distance=st.number_input("Enter Flight Distance",min_value=0)

st.subheader("The value of service between (1,5)")

wifi_service=st.number_input("Rate the wifi service",min_value=0,max_value=5)

time_convenient=st.number_input("Rate the time convenient",min_value=0,max_value=5)

online_booking=st.number_input("Rate the online booking",max_value=5,min_value=0)

food=st.number_input("Rate food & drink",max_value=5,min_value=0)

online_boarding=st.number_input("Rate online boarding",min_value=0,max_value=5)

seats=st.number_input("Rate the seats comfort",min_value=0,max_value=5)


entertainment=st.number_input("Rate inflight entertainment",min_value=0,max_value=5)

onboard=st.number_input("Rate on-board service",min_value=0,max_value=5)

leg_room=st.number_input("Rate leg room space",min_value=0,max_value=5)

baggage=st.number_input("Rate Baggage Handling",max_value=5,min_value=0)

checkin=st.number_input("Rate checkin service",max_value=5,min_value=0)

inflight_service=st.number_input("Rate inflight service",min_value=0,max_value=5)

cleanliness=st.number_input("Rate the cleanliness",max_value=5,min_value=0)

arrival=st.number_input(" Arrival delay in minutes",min_value=0)


def prepair_inputs():
    
    data=pd.DataFrame(
        [[gender,customer_type,age,type_of_travel,class_name,flight_distance,wifi_service,time_convenient,
          online_booking,food,online_boarding,seats,entertainment,onboard,leg_room,baggage,checkin,inflight_service,cleanliness,arrival]],columns=['Gender', 'Customer Type', 'Age', 'Type of Travel', 'Class',
       'Flight Distance', 'Inflight wifi service',
       'Departure/Arrival time convenient', 'Ease of Online booking',
       'Food and drink', 'Online boarding', 'Seat comfort',
       'Inflight entertainment', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Inflight service',
       'Cleanliness', 'Arrival Delay in Minutes', ]
    )
    
    classes=["neutral or dissatisfied","satisfied"]
    
    result=loaded_model.predict(data)
    
    class_name=classes[result]
    
    return class_name

    



