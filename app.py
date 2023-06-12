import streamlit as st
from group_chat_summarizer import main
from datetime import datetime

def main_app():
    st.title("Group Chat Summarizer")

    # User Input
    chat_export_file = st.file_uploader("Chat Export File")
    summary_file = st.text_input("Summary Output File")
    start_date = st.date_input("Start Date", value=datetime.today())
    end_date = st.date_input("End Date", value=datetime.today())
    chat_type = st.selectbox("Chat Type", ["WhatsApp", "Signal"])
    newsletter = st.checkbox("Generate Newsletter Introduction")

    # Generate Summary
    if st.button("Generate Summary"):
        if not chat_export_file or not summary_file:
            st.error("Please fill in all the required fields.")
        elif start_date > end_date:
            st.error("Start Date should be earlier than End Date.")
        else:
            # Save the uploaded file locally
            with open(chat_export_file.name, "wb") as file:
                file.write(chat_export_file.getbuffer())

            st.info("Generating Summary...")
            start_date_str = start_date.strftime("%m/%d/%Y")
            end_date_str = end_date.strftime("%m/%d/%Y")
            main(chat_type, chat_export_file.name, summary_file, start_date_str, end_date_str, newsletter)
            st.success("Summary generated successfully!")

# Run the app
if __name__ == "__main__":
    main_app()
