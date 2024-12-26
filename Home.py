import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
import sqlite3
import webbrowser  

df=pd.read_csv('d1.csv')
df1=pd.read_csv('d2.csv')

st. set_page_config(layout="wide")

p="""
⚡ Smart API Application \n
⚡ AI bot integration\n
⚡ Predict energy requirement\n
⚡ Real-time information mapping and visual representation\n
⚡ Automated database integration\n
⚡ Electric bill predictor\n
⚡ Electric connection tampering detection\n
"""
st.sidebar.header("🔖Features")
st.sidebar.write(p)

# d1=pd.DataFrame(df1)
# se=d1[['Regions','Dates','Usage']]

st.header("⚡Intelligent Energy Management System: ")
st.subheader("Optimizing Energy Distribution with AI🤖")
st.divider()
p="""
Hydro and wind energy are crucial for India to diversify its energy sources, reduce reliance on fossil fuels, and meet its growing power demands sustainably. As power consumption rises with economic growth, these renewable sources help ensure energy security while mitigating environmental impact.

"""
st.write(p)
d=pd.DataFrame(df)
a,c=st.columns(2)
# st.dataframe(df1)

map = folium.Map(location=[20.5937, 78.9629],  tiles="OpenStreetMap",zoom_start=5)

for index, row in df1.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    state_name = row['States']
    usage = row['Usage']
    

    if usage > 400:
        color = 'red'
    elif 200 < usage <= 400:
        color = 'orange'
    else:
        color = 'green'
    

    folium.CircleMarker(
        location=[lat, lon],
        radius=5,  
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        tooltip=f"{state_name}: {usage} MW"
    ).add_to(map)

    legend_html = '''
<div style="position: absolute; bottom: 60px; left: 50px; width: 200px; height: 120px;
            background-color: white; border:2px solid grey; z-index:1000; font-size:14px;
            font-family: Arial; padding: 10px; color: black;">
    <b>Electricity Usage (MW)</b><br>
    <i style="background: red; width: 15px; height: 15px; display: inline-block;"></i> > 400 MW (High)<br>
    <i style="background: orange; width: 15px; height: 15px; display: inline-block;"></i> 200 - 400 MW (Medium)<br>
    <i style="background: green; width: 15px; height: 15px; display: inline-block;"></i> < 200 MW (Low)
</div>
'''

legend = folium.map.Marker(
    location=[11.514603, 83.991748],  
    icon=folium.DivIcon(
        icon_size=(200, 120),
        icon_anchor=(0, 0),
        html=legend_html,
    )
)

map.add_child(legend)

folium.LayerControl().add_to(map)
with st.container():
    st_folium(map, width=900, height=900)


# Initialize connection to SQLite database
conn = sqlite3.connect('scam_reports.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS scam_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_address TEXT,
    state TEXT,
    photo BLOB
)
''')
conn.commit()

# Streamlit app title
st.title("Scam Report Map: Report Suspected Electricity Theft")

# Streamlit form
with st.form("scam_report_form"):
    st.write("Please fill out the details below. Your identity will remain confidential.")

    # Full address input
    full_address = st.text_area("Enter the Full Address of the Suspected Theft:")

    # Dropdown for Indian states
    states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
              "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
              "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
              "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
              "Uttarakhand", "West Bengal"]
    state = st.selectbox("Select the State:", states)

    # File uploader for photo
    photo = st.file_uploader("Upload a Photo of the Incident (optional):", type=["jpg", "jpeg", "png"])

    # Submit button
    submitted = st.form_submit_button("Submit Report")

    if submitted:
        # Handle photo upload as binary data
        photo_data = None
        if photo:
            photo_data = photo.read()

        # Store the data in SQLite database
        c.execute("INSERT INTO scam_reports (full_address, state, photo) VALUES (?, ?, ?)",
                  (full_address, state, photo_data))
        conn.commit()

        st.success("Your report has been submitted successfully. Thank you for helping us fight electricity theft!")

# Optionally, show the reports for verification (this can be removed in production)
if st.checkbox("Show Reports (for debugging)"):
    c.execute("SELECT * FROM scam_reports")
    reports = c.fetchall()
    for report in reports:
        st.write(f"ID: {report[0]}, Address: {report[1]}, State: {report[2]}")
        if report[3]:
            st.image(report[3])

css_styles = """
<style>

    {
        font-size: 40px; 
    }
    body {
        border: 50px solid #000;
        border-radius: 50px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        padding: 20px;
        border-color: white}

    
    [data-testid="stHeader"] {
        font-size: 50px; 
    }
    [data-testid="stForm"] label {
        font-size: 40px; 
    }
[data-testid="stAppViewContainer"]{
    background-color: white;
    opacity: 0.8;
    background-image: url("https://assets.science.nasa.gov/content/dam/science/esd/eo/content-feature/nightlights/images/media/BlackMarble_2016_Asia_composite.png");
    background-size: cover;
    border: 5px solid #000;
}
[data-testid="stAppViewContainer"]{
    border: 3px solid #000;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
[data-testid="stForm"] {
    color: #eae5e5;
}
[data-testid="stForm"] label {
    color: #eae5e5;
}
[data-testid="stForm"] input[type="number"] {
    color: #eae5e5;
}
[data-testid="stForm"] select {
    color: #eae5e5;
}
</style>
"""

st.markdown(css_styles, unsafe_allow_html=True)

# Close the database connection when done
conn.close()


























# st.line_chart(se)

# st.write(se)

# Allow the user to select columns for the charts
# columns = st.multiselect("Select columns for the charts:", df.columns.tolist())

# Check if the user has selected any columns
# if columns:
#     # Plotting a Line Chart
#     st.write("Line Chart:")
#     st.line_chart(df[columns])

#     # Plotting an Area Chart
#     st.write("Area Chart:")
#     st.area_chart(df[columns])

#     # Plotting a Bar Chart
#     st.write("Bar Chart:")
#     st.bar_chart(df[columns])
# else:
#     st.write("Please select at least one column to display the charts.")