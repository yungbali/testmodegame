# ui_service.py

import streamlit as st
import requests

def get_scenes():
    response = requests.get('http://localhost:5000/scenes')
    scenes = response.json()
    return scenes

def main():
    st.title('The Case of the Missing Child: A Text Adventure')
    scenes = get_scenes()
    selected_scene = st.selectbox('Select Scene', [scene['name'] for scene in scenes])
    st.write(f'Scene Description: {scenes[selected_scene]["description"]}')

if __name__ == '__main__':
    main()
