from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App!</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                text-align: center; 
                margin-top: 50px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
                backdrop-filter: blur(10px);
            }
            h1 {
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Hello from Flask!</h1>
            <p>This app was deployed via CI/CD pipeline</p>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return "Ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
