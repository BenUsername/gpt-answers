from flask import Flask, render_template, request
import json
import os
from .data import get_data

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates'))

@app.route('/')
def index():
    # Get data (sample data for Vercel)
    france_data, countries_data, personas_data = get_data()
    
    # Clean country names
    for item in countries_data:
        item['country'] = item['country'].strip()
    for item in personas_data:
        if 'country' in item:
            item['country'] = item['country'].strip()
    
    # Get unique countries for filtering
    countries = sorted(list(set(item['country'] for item in countries_data)))
    
    # Get unique personas for filtering
    personas = sorted(list(set(item['persona'] for item in personas_data if 'persona' in item)))
    
    # Prepare statistics for france-only data
    stats_france = {
        'total_questions': len(france_data),
        'brand_mentioned_count': sum(1 for item in france_data if item['brand_mentioned'] == 'Yes'),
        'visibule_count': sum(1 for item in france_data if item['visibule'] == 'Yes'),
        'branded_count': sum(1 for item in france_data if item['branded'] == 'Yes'),
    }
    
    # Prepare statistics for countries data
    stats_countries = {
        'total_questions': len(countries_data),
        'brand_mentioned_count': sum(1 for item in countries_data if item['brand_mentioned'] == 'Yes'),
        'visibule_count': sum(1 for item in countries_data if item['visibule'] == 'Yes'),
        'branded_count': sum(1 for item in countries_data if item['branded'] == 'Yes'),
    }
    
    # Prepare statistics for personas data
    stats_personas = {
        'total_questions': len(personas_data),
        'brand_mentioned_count': sum(1 for item in personas_data if item['brand_mentioned'] == 'Yes'),
        'visibule_count': sum(1 for item in personas_data if item['visibule'] == 'Yes'),
        'branded_count': sum(1 for item in personas_data if item['branded'] == 'Yes'),
    }
    
    # Add country-specific statistics
    country_stats = {}
    for country in countries:
        country_items = [item for item in countries_data if item['country'] == country]
        country_stats[country] = {
            'total': len(country_items),
            'brand_mentioned': sum(1 for item in country_items if item['brand_mentioned'] == 'Yes'),
            'visibule': sum(1 for item in country_items if item['visibule'] == 'Yes'),
            'branded': sum(1 for item in country_items if item['branded'] == 'Yes'),
        }
    
    # Add persona-specific statistics
    persona_stats = {}
    for persona in personas:
        persona_items = [item for item in personas_data if item.get('persona') == persona]
        persona_stats[persona] = {
            'total': len(persona_items),
            'brand_mentioned': sum(1 for item in persona_items if item['brand_mentioned'] == 'Yes'),
            'visibule': sum(1 for item in persona_items if item['visibule'] == 'Yes'),
            'branded': sum(1 for item in persona_items if item['branded'] == 'Yes'),
        }
    
    return render_template('index_combined.html', 
                          data_france=france_data,
                          data_countries=countries_data,
                          data_personas=personas_data,
                          stats_france=stats_france,
                          stats_countries=stats_countries,
                          stats_personas=stats_personas,
                          countries=countries,
                          personas=personas,
                          country_stats=country_stats,
                          persona_stats=persona_stats)

if __name__ == '__main__':
    app.run(debug=True, port=5002) 