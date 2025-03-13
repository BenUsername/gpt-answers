# WorkWithIsland Response Analysis

## Overview
This project processes CSV files containing questions and responses about acoustic pods/booths, enriches the data with brand mention analysis, and visualizes the results in a web interface.

## Features
- **Data Processing:** Process CSV files with questions and responses about acoustic solutions
- **Brand Mention Analysis:** Track mentions of "workwithisland" in responses and questions
- **Multi-dimensional Analysis:** View data by country or persona
- **Interactive Visualization:** Filter and sort responses with an intuitive web interface

## Dashboard Structure
The dashboard has three tabs:
1. **Default:** Original data focusing on France
2. **Countries:** Data organized by countries (France, UK, Spain, Switzerland, Benelux)
3. **Personas:** Data organized by target personas (CEO, HR Manager, etc.)

## Installation and Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app_combined.py`
4. Access the dashboard at http://127.0.0.1:5002/

## Files
- `app_combined.py` - Main Flask application
- `query_openai_simple.py` - Script to process questions for France
- `query_openai_countries.py` - Script to process questions for all countries
- `query_openai_personas.py` - Script to process questions by persona
- `enrich_csv_*.py` - Scripts to add brand mention analysis

## Technologies Used
- Python (pandas, Flask)
- OpenAI API (GPT-4o-mini)
- Bootstrap for responsive UI
- JavaScript for interactive filtering 