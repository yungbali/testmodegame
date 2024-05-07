import streamlit as st
import json

# Load the master file
with open("master_file.json", "r") as file:
    master_data = json.load(file)

# Main title
st.title(master_data["title"])

# Display scenarios
st.header("Scenarios:")
for scenario in master_data["scenarios"]:
    st.subheader(scenario["title"])
    st.write(scenario["background"])
    st.write("Zoom Instructions:")
    st.write(scenario["zoom_instructions"])

# Display general Zoom instructions
st.header("General Instructions for Playing the Game on Zoom:")
for key, value in master_data["general_zoom_instructions"].items():
    st.subheader(key.capitalize() + ":")
    st.write(value)

# Display additional scenarios
st.header("Additional Scenarios:")
for scenario in master_data["additional_scenarios"]:
    st.subheader(scenario["title"])
    st.write(scenario["background"])

# Display clues
st.header("Clues:")
for key, value in master_data["clues"].items():
    st.subheader(key.capitalize() + ":")
    for clue in value:
        st.write("- " + clue)

# Display suspects
st.header("Suspects:")
for key, value in master_data["suspects"].items():
    st.subheader(key.capitalize() + ":")
    for suspect in value:
        st.write("- " + suspect["name"])
        st.write(suspect["description"])
