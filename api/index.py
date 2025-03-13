import json
from data import get_data

def generate_html():
    """Generate a simple HTML page with the data"""
    france_data, countries_data, personas_data = get_data()
    
    # Calculate statistics
    france_count = len(france_data)
    france_brand = sum(1 for item in france_data if item['brand_mentioned'] == 'Yes')
    france_visibility = sum(1 for item in france_data if item['visibule'] == 'Yes')
    france_branded = sum(1 for item in france_data if item['branded'] == 'Yes')
    
    countries_count = len(countries_data)
    countries_brand = sum(1 for item in countries_data if item['brand_mentioned'] == 'Yes')
    countries_visibility = sum(1 for item in countries_data if item['visibule'] == 'Yes')
    countries_branded = sum(1 for item in countries_data if item['branded'] == 'Yes')
    
    personas_count = len(personas_data)
    personas_brand = sum(1 for item in personas_data if item['brand_mentioned'] == 'Yes')
    personas_visibility = sum(1 for item in personas_data if item['visibule'] == 'Yes')
    personas_branded = sum(1 for item in personas_data if item['branded'] == 'Yes')
    
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
    
    # Create HTML
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WorkWithIsland Analysis</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
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
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Total Questions</h5>
                                    <p class="card-text display-4">{france_count}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Brand Mentions</h5>
                                    <p class="card-text display-4">{france_brand}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Visibility</h5>
                                    <p class="card-text display-4">{france_visibility}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Branded Questions</h5>
                                    <p class="card-text display-4">{france_branded}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Countries Tab -->
                <div class="tab-pane fade" id="countries" role="tabpanel">
                    <div class="row">
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Total Questions</h5>
                                    <p class="card-text display-4">{countries_count}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Brand Mentions</h5>
                                    <p class="card-text display-4">{countries_brand}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Visibility</h5>
                                    <p class="card-text display-4">{countries_visibility}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
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
                </div>
                
                <!-- Personas Tab -->
                <div class="tab-pane fade" id="personas" role="tabpanel">
                    <div class="row">
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Total Questions</h5>
                                    <p class="card-text display-4">{personas_count}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Brand Mentions</h5>
                                    <p class="card-text display-4">{personas_brand}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Visibility</h5>
                                    <p class="card-text display-4">{personas_visibility}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card text-center bg-light mb-3">
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
    
    return html

# This is the handler function for Vercel serverless
def handler(request, context):
    """A minimal handler that just returns static HTML"""
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WorkWithIsland Analysis</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <div class="row">
                <div class="col-12 text-center">
                    <h1>WorkWithIsland Analysis Dashboard</h1>
                    <div class="alert alert-success mt-4">
                        Server is working!
                    </div>
                    <p class="mt-4">
                        This is a minimal version of the dashboard to confirm that the serverless function is working.
                    </p>
                    <div class="mt-4">
                        <h3>Statistics</h3>
                        <p>Total France Questions: 100+</p>
                        <p>Total Countries Questions: 200+</p>
                        <p>Total Personas Questions: 50+</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html
    } 