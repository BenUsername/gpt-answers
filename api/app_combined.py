from flask import Flask, render_template, request
import pandas as pd
import json
import os
from .data import get_data

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates'))

@app.route('/')
def index():
    # Get data (either from real CSV files or sample data)
    df_france, df_countries, df_personas = get_data()
    
    # Clean country names (strip whitespace) to avoid duplicates
    df_countries['country'] = df_countries['country'].str.strip()
    df_personas['country'] = df_personas['country'].str.strip()
    
    # Convert Boolean columns to more readable format for all datasets
    for df in [df_france, df_countries, df_personas]:
        df['brand_mentioned'] = df['brand_mentioned'].map({True: 'Yes', False: 'No'})
        df['visibule'] = df['visibule'].map({True: 'Yes', False: 'No'})
        df['branded'] = df['branded'].map({True: 'Yes', False: 'No'})
    
    # Get unique countries for filtering
    countries = sorted(df_countries['country'].unique().tolist())
    
    # Get unique personas for filtering
    personas = sorted(df_personas['persona'].dropna().unique().tolist())
    
    # Convert DataFrames to dictionaries for JSON serialization
    data_france = df_france.to_dict(orient='records')
    data_countries = df_countries.to_dict(orient='records')
    data_personas = df_personas.to_dict(orient='records')
    
    # Prepare statistics for france-only data
    stats_france = {
        'total_questions': len(df_france),
        'brand_mentioned_count': (df_france['brand_mentioned'] == 'Yes').sum(),
        'visibule_count': (df_france['visibule'] == 'Yes').sum(),
        'branded_count': (df_france['branded'] == 'Yes').sum(),
    }
    
    # Prepare statistics for countries data
    stats_countries = {
        'total_questions': len(df_countries),
        'brand_mentioned_count': (df_countries['brand_mentioned'] == 'Yes').sum(),
        'visibule_count': (df_countries['visibule'] == 'Yes').sum(),
        'branded_count': (df_countries['branded'] == 'Yes').sum(),
    }
    
    # Prepare statistics for personas data
    stats_personas = {
        'total_questions': len(df_personas),
        'brand_mentioned_count': (df_personas['brand_mentioned'] == 'Yes').sum(),
        'visibule_count': (df_personas['visibule'] == 'Yes').sum(),
        'branded_count': (df_personas['branded'] == 'Yes').sum(),
    }
    
    # Add country-specific statistics
    country_stats = {}
    for country in countries:
        country_df = df_countries[df_countries['country'] == country]
        country_stats[country] = {
            'total': len(country_df),
            'brand_mentioned': (country_df['brand_mentioned'] == 'Yes').sum(),
            'visibule': (country_df['visibule'] == 'Yes').sum(),
            'branded': (country_df['branded'] == 'Yes').sum(),
        }
    
    # Add persona-specific statistics
    persona_stats = {}
    for persona in personas:
        persona_df = df_personas[df_personas['persona'] == persona]
        persona_stats[persona] = {
            'total': len(persona_df),
            'brand_mentioned': (persona_df['brand_mentioned'] == 'Yes').sum(),
            'visibule': (persona_df['visibule'] == 'Yes').sum(),
            'branded': (persona_df['branded'] == 'Yes').sum(),
        }
    
    return render_template('index_combined.html', 
                          data_france=data_france,
                          data_countries=data_countries,
                          data_personas=data_personas,
                          stats_france=stats_france,
                          stats_countries=stats_countries,
                          stats_personas=stats_personas,
                          countries=countries,
                          personas=personas,
                          country_stats=country_stats,
                          persona_stats=persona_stats)

if __name__ == '__main__':
    app.run(debug=True, port=5002) 