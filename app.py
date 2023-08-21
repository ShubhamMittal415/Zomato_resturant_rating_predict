from flask import Flask, render_template, request
import joblib  # Or your preferred library for loading the model

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        name = request.form['name']
        # Get other input values similarly

        # Use your model to make a prediction based on the input
        # Replace this with your actual prediction code
        input_data = [name, ...]  # Collect other input values into a list
        predicted_rating = model.predict([input_data])[0]

        prediction = round(predicted_rating, 2)  # Round the prediction to 2 decimal places

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
