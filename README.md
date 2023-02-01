# Steam Charts Dash App

This is a simple web app created using Dash that displays interactive graphs and dropdown menus for data obtained from [Steam Charts](https://steamcharts.com/). The data was obtained from a previous web scraping project and is stored on Google Drive.

## Features

- Three interactive graphs: 
  - A bar graph showing the number of players in the Top 25 games.
  - A bar graph showing the games that are trending and have the largest playerbase growth in the last 24 hours.
  - A bar graph showing the top 5 games that hold records for peak players and the date acheived.
- Dropdown menus to select the game to display data for.

## Installation

1. Clone the repository: `git clone https://github.com/Kvikvne/Steam-charts-dashboard.git`
2. Install the requirements: `pip install -r requirements.txt`
3. Run the app: `python main.py`
4. Access the app in your browser at http://127.0.0.1:8050/

## Data

The data used in this app was obtained from Steam Charts using a web scraping script and is stored in a Google Drive folder. The data was cleaned and preprocessed before being used in the app. 

## Dependencies

- certifi==2022.12.7
- charset-normalizer==3.0.1
- click==8.1.3
- colorama==0.4.6
- dash==2.7.1
- dash-bootstrap-components==1.3.0
- dash-core-components==2.0.0
- dash-html-components==2.0.0
- dash-table==5.0.0
- docopt==0.6.2
- Flask==2.2.2
- idna==3.4
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.2
- numpy==1.24.1
- pandas==1.5.3
- pipreqs==0.4.11
- plotly==5.12.0
- python-dateutil==2.8.2
- pytz==2022.7.1
- requests==2.28.2
- six==1.16.0
- tenacity==8.1.0
- urllib3==1.26.14
- Werkzeug==2.2.2
- yarg==0.1.9

## Note

- I am still working on how I am going to keep the data more current. So the data may not exaclty match steam charts.
