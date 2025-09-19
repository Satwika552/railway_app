import streamlit as st

st.title("📝 Notepad App")

text = st.text_area("Write your notes here:")

if st.button("Save Note"):
    with open("notes.txt", "a") as f:
        f.write(text + "\n")
    st.success("Note saved!")

if st.button("Show Saved Notes"):
    with open("notes.txt", "r") as f:
        notes = f.read()
    st.text_area("Your Notes:", notes, height=200)
