from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """Simple endpoint that returns a JSON response"""
    return jsonify({
        'status': 'success',
        'message': 'WorkWithIsland Analysis API is working!',
        'version': '1.0.0'
    })

# Vercel serverless function handler
def handler(request, context):
    """Handle a request to the Vercel serverless function"""
    return app

# For local testing
if __name__ == '__main__':
    app.run(debug=True, port=5002) 