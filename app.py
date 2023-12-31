from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)

app = application

# Route for home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education = request.form.get("parental_level_of_education"),
            lunch = request.form.get("lunch"),
            test_preparation_course = request.form.get("test_preparation_course"),
            reading_score = float(request.form.get("reading_score")),
            writing_score = float(request.form.get("writing_score"))
        )

        pred_df  = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print(f"Predicted value is {results[0]}")
     
        return render_template('home.html', results=round(results[0],3))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

