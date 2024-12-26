import streamlit as st
import sqlite3

# SQLite Database setup
conn = sqlite3.connect('contact_us.db', check_same_thread=False)
c = conn.cursor()

# Function to fetch contact details from the database
def fetch_contact_details():
    c.execute("SELECT first_name, last_name, email, phone_number, message, rating FROM contacts")
    return c.fetchall()

# Streamlit page to display the contact submissions
st.title("📋 Submitted Contact Details")

# Fetch contact details from the database
submissions = fetch_contact_details()

# Display submissions if any exist
if submissions:
    for i, submission in enumerate(submissions, 1):
        st.markdown(f"*Submission #{i}:*")
        st.write(f"*Name:* {submission[0]} {submission[1]}")
        st.write(f"*Email:* {submission[2]}")
        st.write(f"*Phone Number:* {submission[3]}")
        st.write(f"*Message:* {submission[4]}")
        st.write(f"*Rating:* {submission[5]}")
        st.markdown("---")
else:
    st.write("No submissions yet.")