# electricity_Management_system
The Electricity Management System is a Streamlit-based web application designed to monitor, analyze, and visualize energy consumption data. It provides users with insights into energy usage trends, highlights the most energy-consuming appliances, and offers recommendations for energy conservation.

## Features

- **Real-time Energy Monitoring:-**
  - Displays energy consumption of household appliances.
  - Highlights the most energy-consuming appliance in a month.

- **Data Visualization:**
  - Trend graphs showing daily and monthly energy consumption.
  - Appliance-wise consumption data presented with charts.

- **Predictive Analysis:**
  - Predicts real-time energy consumption using a linear regression model.
  - Detects unusual energy consumption patterns.

- **Energy Saving Recommendations:**
  - Offers actionable tips to reduce energy usage.

- **Theft Reporting Form:**
  - A form integrated with an SQLite database to report suspected electricity theft.

- **Enhanced User Experience:**
  - Interactive user interface built with Streamlit.
  - Customizable map markers and energy data visualization using Folium.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/UR295/electricity_Management_system
   ```

2. Navigate to the project directory:
   ```bash
   cd electricity-management
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the application in your browser using the URL provided by Streamlit.
2. Navigate through the different sections:
   - View energy consumption trends.
   - Analyze appliance-wise data.
   - Report electricity theft through the form.
3. Use predictive analysis to monitor and manage your energy usage.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Database:** SQLite
- **Data Visualization Libraries:** Matplotlib, Plotly, Folium
- **Machine Learning Model:** Linear Regression (scikit-learn)

## Directory Structure

```
project-directory/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── data/                # Data files and SQLite database
├── models/              # Machine learning models
├── static/              # Static assets (e.g., images, CSS)
├── templates/           # HTML templates (if any)
└── utils/               # Utility scripts
```

## Future Enhancements

- Integrate additional machine learning models for more accurate predictions.
- Add support for multiple users with role-based access.
- Implement notifications for unusual consumption patterns via email or SMS.
- Expand the application to support renewable energy management.

## Contributors
- Urbi Purohit

## Acknowledgments
- Streamlit documentation
- OpenAI for providing assistance
- Community contributors
