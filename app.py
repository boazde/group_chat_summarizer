import streamlit as st
from group_chat_summarizer import main

def main_app():
    st.title("Group Chat Summarizer")

    # User Input
    chat_export_file = st.text_input("Chat Export File")
    summary_file = st.text_input("Summary Output File")
    start_date = st.text_input("Start Date (MM/DD/YYYY)")
    end_date = st.text_input("End Date (MM/DD/YYYY)")
    chat_type = st.selectbox("Chat Type", ["WhatsApp", "Signal"])
    newsletter = st.checkbox("Generate Newsletter Introduction")

    # Generate Summary
    if st.button("Generate Summary"):
        if not chat_export_file or not summary_file or not start_date or not end_date:
            st.error("Please fill in all the required fields.")
        else:
            st.info("Generating Summary...")
            main(chat_type, chat_export_file, summary_file, start_date, end_date, newsletter)
            st.success("Summary generated successfully!")

# Run the app
if __name__ == "__main__":
    main_app()
