from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
def serve_static(path=''):
    # Define la carpeta raíz donde se encuentran los archivos estáticos
    root_dir = os.path.join(os.getcwd(), 'Main')
    
    # Sirve archivos desde la carpeta 'Main'
    return send_from_directory(root_dir, path) if path else send_from_directory(root_dir, 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
