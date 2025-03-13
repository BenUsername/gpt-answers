from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Read the enriched CSV
    df = pd.read_csv('workwithisland_questions_france_enriched.csv')
    
    # Convert Boolean columns to more readable format
    df['brand_mentioned'] = df['brand_mentioned'].map({True: 'Yes', False: 'No'})
    df['visibule'] = df['visibule'].map({True: 'Yes', False: 'No'})
    df['branded'] = df['branded'].map({True: 'Yes', False: 'No'})
    
    # Convert DataFrame to dictionary for JSON serialization
    data = df.to_dict(orient='records')
    
    # Prepare statistics
    stats = {
        'total_questions': len(df),
        'brand_mentioned_count': (df['brand_mentioned'] == 'Yes').sum(),
        'visibule_count': (df['visibule'] == 'Yes').sum(),
        'branded_count': (df['branded'] == 'Yes').sum(),
    }
    
    return render_template('index.html', data=data, stats=stats)

if __name__ == '__main__':
    app.run(debug=True) 