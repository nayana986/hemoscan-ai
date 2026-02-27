from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        gender = int(request.form['gender'])
        hb = float(request.form['hemoglobin'])

        # Simple logic: Hemoglobin < 13.5 (Male) or < 12.0 (Female)
        is_anemic = 1 if hb < (13.5 if gender == 1 else 12.0) else 0
        
        if is_anemic == 1:
            result = "Positive for Anemia"
            color = "red"
        else:
            result = "Negative for Anemia"
            color = "green"

        return render_template('index.html', 
                               prediction_text=f'Result: {result}', 
                               result_color=color)
    except Exception as e:
        return render_template('index.html', 
                               prediction_text=f'Error: Please enter valid numbers')

if __name__ == '__main__':
    app.run(debug=True, port=5000)