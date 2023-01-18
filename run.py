import streamlit as st
import sys
import pandas as pd
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2
import torch
import time
import av

def main():
    st.title("MALWARE IMAGE CLASSIFICATION")

    menu = ["None","image"]
    choice = st.selectbox("Mode", menu)
    
    if choice=="image":
        st.subheader("Image")
        
        d=st.date_input("Date")
        st.subheader("image")
        im=st.file_uploader('upload_image',type=['png','jpg','jpeg'])
        if(im):
                st.image(im)
                model=tf.keras.models.load_model('resnet50.h5')


                img =np.asarray(Image.open(im))
                im1=np.expand_dims(img,axis=0)
                pred=model.predict(im1)
                labels=["Adposhel","Agent","Allaple","Amonetize","Androm","Autorun","BrowseFox","Dinwod","Elex","Expiro","Fasong","HackKMS","Hlux","Injector","InstallCore","MultiPlug","Neoreklami","Neshta","Regrun","Sality","Snarasite","Stantinko","VBA","VBKrypt","Vilsel"]
                category=['Adware','Trojan','Worm','Adware','Backdoor','Worm','Adware','Trojan','Trojan','Virus','Worm','Trojan','Worm','Trojan','Adwate','Adware','Adware','Virus','Trojan','Virus','Trojan','Backdoor','Virus','Trojan','Trojan']
                st.write(labels[np.argmax(pred)],category[np.argmax(pred)])
                st.success("Succesfully predicted")

    if choice=="None":
        pass

            
main()