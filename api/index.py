from flask import Flask, render_template, request, jsonify
import json
import os
from data import get_data

# Create Flask app for serverless environment
app = Flask(__name__)

# Copy templates to the api directory for Vercel
templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
if not os.path.exists(templates_dir):
    try:
        os.makedirs(templates_dir, exist_ok=True)
    except:
        pass

# Define a simple route for Vercel
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    try:
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
        
        # For Vercel, we'll return JSON data instead of rendering a template
        # since we're having issues with template rendering in serverless
        if request.headers.get('Accept') == 'application/json':
            return jsonify({
                'data_france': france_data,
                'data_countries': countries_data,
                'data_personas': personas_data,
                'stats_france': stats_france,
                'stats_countries': stats_countries,
                'stats_personas': stats_personas,
                'countries': countries,
                'personas': personas,
                'country_stats': country_stats,
                'persona_stats': persona_stats
            })
        
        # Simple HTML response for debugging
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>WorkWithIsland Analysis Dashboard</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-4">
                <h1>WorkWithIsland Analysis Dashboard</h1>
                <p>The server is running! This is a simplified view.</p>
                <p>For full functionality, please run the app locally.</p>
                <p>API endpoint available at <a href="/api/data">/api/data</a></p>
                <div class="mt-4">
                    <h2>Sample Statistics</h2>
                    <ul>
                        <li>France Questions: """ + str(stats_france['total_questions']) + """</li>
                        <li>Countries Questions: """ + str(stats_countries['total_questions']) + """</li>
                        <li>Personas Questions: """ + str(stats_personas['total_questions']) + """</li>
                    </ul>
                </div>
            </div>
        </body>
        </html>
        """
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add a simple API endpoint
@app.route('/api/data')
def api_data():
    france_data, countries_data, personas_data = get_data()
    return jsonify({
        'france_data': france_data[:5],  # Limit to 5 items
        'countries_data': countries_data[:5],  # Limit to 5 items
        'personas_data': personas_data[:5]  # Limit to 5 items
    })

# Vercel serverless function handler
def handler(request, context):
    with app.request_context(request):
        return app.full_dispatch_request()

# For local testing
if __name__ == '__main__':
    app.run(debug=True, port=5002) 