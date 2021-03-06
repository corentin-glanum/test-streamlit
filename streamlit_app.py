# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This demo lets you to explore the Udacity self-driving car image dataset.
# More info: https://github.com/streamlit/demo-self-driving

import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os
import streamlit as st
import pandas as pd
import imghdr
import time
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions

# Streamlit encourages well-structured code, like starting execution in a main() function.
def main():


    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Training", "Testing"])
    if app_mode == "Training":
        st.sidebar.success('To continue select "Run the app".')
        st.text('This is some text.')
        directory = os.path.join('data')
        photos = []
        for file in os.listdir(directory):
            filepath = os.path.join(directory, file)

            # Find all valid images
            if imghdr.what(filepath) is not None:
                photos.append(file)

        photos.sort()
        option = st.sidebar.selectbox('Please select a sample image, then click Magic Time button', photos)
        pressed = st.sidebar.button('Magic Time')
        if pressed:
            st.write('rererer')
        pic = os.path.join(directory, option)

        run_app(pic)
    elif app_mode == "Testing":
       st.sidebar.success('GG')
       dataframe = np.random.randn(10, 20)
       st.dataframe(dataframe)
       x = st.slider('x')  # ???? this is a widget
       st.write(x, 'squared is', x * x)
       st.text_input("Your name", key="name")
       # You can access the value at any point with:
       st.session_state.name
       df = pd.DataFrame({
           'first column': [1, 2, 3, 4],
           'second column': [10, 20, 30, 40]
           })
       
       option = st.selectbox(
           'Which number do you like best?',
            df['first column'])
       
       'You selected: ', option
        
       'Starting a long computation...'
    
       # Add a placeholder
       latest_iteration = st.empty()
       bar = st.progress(0)
        
       for i in range(100):
         # Update the progress bar with each iteration.
         latest_iteration.text(f'Iteration {i+1}')
         bar.progress(i + 1)
         time.sleep(0.1)
        
       '...and now we\'re done!'

def run_app(img):
    evaluate(img)
    
def evaluate(img_fname):
    classifier = load_model('models/cnn_80epochs_imgsize160.h5')
    model = ResNet50(weights='imagenet')
    img = image.load_img(img_fname, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = classifier.predict(x)
    # print the probability and category name for the 5 categories 
    # with highest probability: 
    st.image(img_fname)
    st.write(preds)
    
if __name__ == "__main__":
    main()
