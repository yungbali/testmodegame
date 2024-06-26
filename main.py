import streamlit as st
import json
import openai

# Set up OpenAI API key
openai.api_key = "sk-proj-RYmd9vpLkMziDIrWlJIzT3BlbkFJODK1x5uNETzsUMWw1jzk"

# Load the master file
with open("master_file.json", "r") as file:
    master_data = json.load(file)

# Main title
st.title(master_data["title"])

# Function to display scenario details
def display_scenario(scenario):
    st.subheader(scenario["title"])
    st.write(scenario["background"])

# Function to display clues
def display_clues(clues):
    for key, value in clues.items():
        st.subheader(key.capitalize() + ":")
        for clue in value:
            st.write("- " + clue)

# Function to display suspects
def display_suspects(suspects):
    for key, value in suspects.items():
        st.subheader(key.capitalize() + ":")
        for suspect in value:
            st.write("- " + suspect["name"])
            st.write(suspect["description"])

# Introduction section
with st.form("Introduction"):
    st.write("You are a seasoned detective tasked with solving the mysterious disappearance of a young girl named Sarah. She was last seen leaving her home after a heated argument with her parents. It's suspected that Sarah might have been coerced online and is now a victim of human trafficking. Your mission is to unravel the truth behind Sarah's disappearance and bring her home safely.")
    st.form_submit_button("Start Investigation")

# Scenario section
with st.form("Scenario"):
    st.subheader("Choose a Scenario:")
    selected_scenario = st.radio("", [scenario["title"] for scenario in master_data["scenarios"]])
    selected_scenario_index = [scenario["title"] for scenario in master_data["scenarios"]].index(selected_scenario)
    display_scenario(master_data["scenarios"][selected_scenario_index])
    st.form_submit_button("Continue Investigation")

# Clue section
with st.form("Clues"):
    st.subheader("Clues:")
    selected_clues = master_data["clues"]
    display_clues(selected_clues)
    st.form_submit_button("Analyze Clues")

# Suspect section
with st.form("Suspects"):
    st.subheader("Suspects:")
    selected_suspects = master_data["suspects"]
    display_suspects(selected_suspects)
    selected_suspect = st.selectbox("Select a Suspect:", [suspect["name"] for suspect in selected_suspects["openai"]])
    if selected_suspect == "OpenAI":
        st.subheader("Interrogate OpenAI:")
        question = st.text_input("Ask a question:")
        if st.button("Ask"):
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=question,
                max_tokens=50
            )
            st.write(response.choices[0].text.strip())
    st.form_submit_button("Interrogate Suspects")
