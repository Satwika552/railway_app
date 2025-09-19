import streamlit as st

st.title("Indian Railways Traffic Optimizer 🚆")
st.write("This is a demo AI-powered decision support system for train scheduling.")

train = st.text_input("Enter Train Name:")
priority = st.selectbox("Select Priority:", ["High", "Medium", "Low"])

if st.button("Optimize"):
    st.success(f"Train {train} with {priority} priority scheduled successfully!")
