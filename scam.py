import streamlit as st
import sqlite3

# Initialize connection to SQLite database
conn = sqlite3.connect('scam_reports.db')
c = conn.cursor()

# Streamlit app title
st.title("Reported Suspected Electricity Theft")

# Fetch the reports from the database
c.execute("SELECT id, full_address, state, photo FROM scam_reports")
reports = c.fetchall()

# Display the reports
if reports:
    for report in reports:
        st.write(f"**Report ID:** {report[0]}")
        st.write(f"**Address:** {report[1]}")
        st.write(f"**State:** {report[2]}")
        if report[3]:
            st.image(report[3], caption="Uploaded Photo", use_column_width=True)
        st.write("---")
else:
    st.write("No reports found.")

# Close the database connection when done
conn.close()
