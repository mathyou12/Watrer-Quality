from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained models
model_potable = pickle.load(open('model_potable.pkl', 'rb'))
model_agri = pickle.load(open('model_agri.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from JSON
        data = request.get_json()

        # Convert input to a 2D NumPy array
        features = [
            float(data['ph']),
            float(data['hardness']),
            float(data['solids']),
            float(data['chloramines']),
            float(data['sulfate']),
            float(data['organic_carbon']),
            float(data['turbidity'])
        ]
        input_array = np.array([features])

        # Use models to predict (do NOT overwrite model variables!)
        pred_potable = model_potable.predict(input_array)[0]
        pred_agri = model_agri.predict(input_array)[0]

        # Return result as JSON
        return jsonify({
            'potable': "Yes" if pred_potable == 1 else "No",
            'agriculture': "Suitable" if pred_agri == 1 else "Not Suitable"
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
