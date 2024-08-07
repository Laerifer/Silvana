from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
def serve_static(path=''):
    # Sirve archivos desde el directorio actual
    return send_from_directory(os.getcwd(), path) if path else send_from_directory(os.getcwd(), 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
