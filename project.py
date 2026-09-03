import os
import subprocess
import sys
from flask import Flask, render_template, request, jsonify

# 1. ABSOLUTE PATH CONFIGURATION (Place it right here)
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'))

# 2. ROUTES
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    code = data.get('code', '')

    if not code.strip():
        return jsonify({'output': 'No code provided.'})

    try:
        result = subprocess.run(
            [sys.executable, '-c', code],
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout if result.stdout else result.stderr
        return jsonify({'output': output if output else 'Code executed successfully with no output.'})
    except subprocess.TimeoutExpired:
        return jsonify({'output': 'Error: Code execution timed out (5s limit).'})
    except Exception as e:
        return jsonify({'output': f'Error: {str(e)}'})

# 3. APP RUNNER
if __name__ == '__main__':
    app.run(debug=True, port=8000)