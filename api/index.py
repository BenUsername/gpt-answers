from flask import Flask, Response, jsonify
from data import get_data
import json

app = Flask(__name__)

# HTML template for the main page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WorkWithIsland Analysis</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .card {{ margin-bottom: 20px; }}
        .brand-mention {{ background-color: #e7f3fe; padding: 0 3px; border-radius: 3px; }}
    </style>
</head>
<body>
    <div class="container mt-4">
        <h1 class="mb-4">WorkWithIsland Response Analysis</h1>
        
        <div class="alert alert-info">
            This is a simplified version for sharing. For the full interactive dashboard, please run the app locally.
        </div>
        
        <ul class="nav nav-tabs mb-4" id="mainTab" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="france-tab" data-bs-toggle="tab" data-bs-target="#france" type="button" role="tab">France</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="countries-tab" data-bs-toggle="tab" data-bs-target="#countries" type="button" role="tab">Countries</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="personas-tab" data-bs-toggle="tab" data-bs-target="#personas" type="button" role="tab">Personas</button>
            </li>
        </ul>
        
        <div class="tab-content" id="mainTabContent">
            <!-- France Tab -->
            <div class="tab-pane fade show active" id="france" role="tabpanel">
                <div class="row">
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Total Questions</h5>
                                <p class="card-text display-4">{france_count}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Brand Mentions</h5>
                                <p class="card-text display-4">{france_brand}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Visibility</h5>
                                <p class="card-text display-4">{france_visibility}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Branded Questions</h5>
                                <p class="card-text display-4">{france_branded}</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="mt-4">
                    <h3>API Access</h3>
                    <a href="/api/france" class="btn btn-outline-primary">Get France Data (JSON)</a>
                </div>
            </div>
            
            <!-- Countries Tab -->
            <div class="tab-pane fade" id="countries" role="tabpanel">
                <div class="row">
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Total Questions</h5>
                                <p class="card-text display-4">{countries_count}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Brand Mentions</h5>
                                <p class="card-text display-4">{countries_brand}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Visibility</h5>
                                <p class="card-text display-4">{countries_visibility}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Branded Questions</h5>
                                <p class="card-text display-4">{countries_branded}</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="mt-4">
                    <h3>Countries</h3>
                    <div class="mb-3">
                        {country_badges}
                    </div>
                </div>
                
                <div class="mt-4">
                    <h3>API Access</h3>
                    <a href="/api/countries" class="btn btn-outline-primary">Get Countries Data (JSON)</a>
                </div>
            </div>
            
            <!-- Personas Tab -->
            <div class="tab-pane fade" id="personas" role="tabpanel">
                <div class="row">
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Total Questions</h5>
                                <p class="card-text display-4">{personas_count}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Brand Mentions</h5>
                                <p class="card-text display-4">{personas_brand}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Visibility</h5>
                                <p class="card-text display-4">{personas_visibility}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card text-center bg-light">
                            <div class="card-body">
                                <h5 class="card-title">Branded Questions</h5>
                                <p class="card-text display-4">{personas_branded}</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="mt-4">
                    <h3>Personas</h3>
                    <div class="mb-3">
                        {persona_badges}
                    </div>
                </div>
                
                <div class="mt-4">
                    <h3>API Access</h3>
                    <a href="/api/personas" class="btn btn-outline-primary">Get Personas Data (JSON)</a>
                </div>
            </div>
        </div>
    </div>
    
    <footer class="container mt-5 mb-3 text-center text-muted">
        <hr>
        <p>WorkWithIsland Analysis Dashboard © 2023</p>
    </footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

def generate_html():
    """Generate the HTML for the dashboard"""
    france_data, countries_data, personas_data = get_data()
    
    # Get unique countries and personas
    countries = sorted(list(set(item['country'].strip() for item in countries_data)))
    personas = sorted(list(set(item['persona'] for item in personas_data if 'persona' in item)))
    
    # Generate country badges HTML
    country_badges = ' '.join([
        f'<span class="badge bg-primary me-2 mb-2">{country}</span>' 
        for country in countries
    ])
    
    # Generate persona badges HTML
    persona_badges = ' '.join([
        f'<span class="badge bg-success me-2 mb-2">{persona}</span>' 
        for persona in personas
    ])
    
    # Calculate statistics
    stats_france = {
        'total': len(france_data),
        'brand': sum(1 for item in france_data if item['brand_mentioned'] == 'Yes'),
        'visibility': sum(1 for item in france_data if item['visibule'] == 'Yes'),
        'branded': sum(1 for item in france_data if item['branded'] == 'Yes'),
    }
    
    stats_countries = {
        'total': len(countries_data),
        'brand': sum(1 for item in countries_data if item['brand_mentioned'] == 'Yes'),
        'visibility': sum(1 for item in countries_data if item['visibule'] == 'Yes'),
        'branded': sum(1 for item in countries_data if item['branded'] == 'Yes'),
    }
    
    stats_personas = {
        'total': len(personas_data),
        'brand': sum(1 for item in personas_data if item['brand_mentioned'] == 'Yes'),
        'visibility': sum(1 for item in personas_data if item['visibule'] == 'Yes'),
        'branded': sum(1 for item in personas_data if item['branded'] == 'Yes'),
    }
    
    # Fill in the template
    html = HTML_TEMPLATE.format(
        france_count=stats_france['total'],
        france_brand=stats_france['brand'],
        france_visibility=stats_france['visibility'],
        france_branded=stats_france['branded'],
        countries_count=stats_countries['total'],
        countries_brand=stats_countries['brand'],
        countries_visibility=stats_countries['visibility'],
        countries_branded=stats_countries['branded'],
        personas_count=stats_personas['total'],
        personas_brand=stats_personas['brand'],
        personas_visibility=stats_personas['visibility'],
        personas_branded=stats_personas['branded'],
        country_badges=country_badges,
        persona_badges=persona_badges
    )
    
    return html

def handle_api_request(path):
    """Handle API requests"""
    france_data, countries_data, personas_data = get_data()
    
    if path == 'france':
        return {'data': france_data}
    elif path == 'countries':
        return {'data': countries_data}
    elif path == 'personas':
        return {'data': personas_data}
    else:
        return {
            'error': 'Invalid API endpoint',
            'available_endpoints': ['/api/france', '/api/countries', '/api/personas']
        }

# This is the handler function for Vercel serverless
def handler(request, context):
    path = request.get('path', '')
    
    # Handle API requests
    if path.startswith('/api/'):
        api_path = path[5:]  # Remove '/api/'
        result = handle_api_request(api_path)
        
        # Return JSON response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(result)
        }
    
    # For all other paths, return the HTML dashboard
    html = generate_html()
    
    # Return HTML response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html
    } 