import streamlit as st
from PIL import Image
import numpy as np
import cv2

with st.spinner("Wait model  is downloading ..."):
    
    try:
        pass
    except Exception as e:
        pass

st.set_page_config(page_title="Intel Data Set")

st.title("CNN Model (Intel Data)")

st.write("You can upload images has (Sea,Building,Forest,Mountain,Street,Glacier) and the model will classify the image" )

image_upload=st.file_uploader("Upload Your Image",type=["png","jpg","jpeg"])




if image_upload != None:
    
    image_read=Image.open(image_upload)
    st.image(image_read,use_container_width=True,caption="uploaded image")
    
    img_arr=np.array(image_read)
    
    img_arr=cv2.resize(img_arr,(224,224))
    
    img_arr=np.expand_dims(img_arr,0)
    
    
    
    if st.button("Activate Model",type="primary"):
        
        with st.spinner("Wait ... "):
            result=model.predict(img_arr)
            
            st.markdown(f"""
                      <h3 style="padding:5px; border-radius:5px; color:#F9F9EB; background:#B8BA34;">The decision {result}</h3>  
                        
                        
                        
                        """)
        
        

