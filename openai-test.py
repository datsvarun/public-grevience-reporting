import google.generativeai as genai
import PIL.Image
import os
import dotenv
import streamlit as st


st.set_page_config(
    page_title="Greviance Reporting Letter Generator",
    page_icon="⚠️"
)

# Check if the Google API key is provided in the sidebar
with st.sidebar:
    if 'GOOGLE_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        api_key = st.secrets['GOOGLE_API_KEY']
    else:
        api_key = st.text_input('Enter Google API Key:', type='password')
        if not (api_key.startswith('AI')):
            st.warning('Please enter your API Key!', icon='⚠️')
        else:
            st.success('Success!', icon='✅')
    os.environ['GOOGLE_API_KEY'] = api_key
    "[Get a Google Gemini API key](https://ai.google.dev/)"
    "[View the source code](https://github.com/wms31/streamlit-gemini/blob/main/app.py)"
    "[Check out the blog post!](https://letsaiml.com/creating-google-gemini-app-with-streamlit/)"

# Set the title and caption for the Streamlit app
st.title("🤖 Google Gemini Models")
st.caption("🚀 A streamlit app powered by Google Gemini")

# Create tabs for the Streamlit app
tab1 = st.tabs(["🌏 Generate Travel Plans - Gemini Pro"])

# Code for Gemini Pro Vision model
with tab1:
    st.write("🖼️ Using Gemini Pro Vision - Multimodal model")
    st.subheader("🔮 Generate letter from image")
    
    authority_prompt = st.text_input("Write the Name of the authority:", placeholder="Prompt", label_visibility="visible", key="image_prompt")
    name_prompt = st.text_input("Write your name:", placeholder="Concerned Citizen", label_visibility="visible", key="mage_prompt")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    image = ""

    if uploaded_file is not None:
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit=st.button("Generate Response")

    if submit:
        model = genai.GenerativeModel('gemini-pro-vision')
        with st.spinner("Generating your response using Gemini..."):
            if name_prompt!="":
                response = model.generate_content([name_prompt,image])
            else:
                response = model.generate_content(["Write a letter to the competent authority"+ authority_prompt + "about the problems in this picture, signed by" + name_prompt , image])
        response = response.text
        st.subheader("Gemini's response")
        st.write(response)

'''
genai.configure(api_key=os.environ.get('OPENAI_API_KEY'))
img = PIL.Image.open('IMG_20240701_100258705.jpg')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
authority = input("Enter authority name: ")
name = input("Enter your name: ")
response = model.generate_content(["Write a letter to the competent authority"+ authority + "about the problems in this picture, signed by" + name , img])
print(response.text)
'''
