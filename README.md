# WorkWithIsland Response Analysis

A simple Flask application for analyzing questions and responses about acoustic pods/booths, with a focus on brand mentions and content visibility for WorkWithIsland.

## Setup

1. Install the required dependencies:
```
pip install -r requirements.txt
```

2. Run the application:
```
python app_combined.py
```

3. Open your browser and navigate to:
```
http://localhost:5002
```

## Files

- `app_combined.py`: Main Flask application
- `templates/index_combined.html`: HTML template for the dashboard
- CSV files:
  - `workwithisland_questions_france_enriched.csv`: France-specific data
  - `workwithisland_questions_countries_enriched.csv`: Country-based data
  - `workwithisland_questions_personas_enriched.csv`: Persona-based data

## Features

- View statistics about brand mentions
- Filter and sort responses by country or persona
- Highlight brand mentions in responses
- Interactive table view 