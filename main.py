from flask import Flask, render_template, request, jsonify
from number import generate_random_number

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    upper_bound = data.get('upperBound')
    
    if upper_bound is not None:
        try:
            upper_bound = int(upper_bound)
        except ValueError:
            return jsonify({'error': 'Upper bound must be a valid integer'}), 400
    
    try:
        random_num = generate_random_number(upper_bound)
        return jsonify({'number': random_num})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    