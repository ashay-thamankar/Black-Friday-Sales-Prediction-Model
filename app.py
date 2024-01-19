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
            User_ID=int(request.form.get("User_ID")),
            Occupation=request.form.get('Occupation'),
            Stay_In_Current_City_Years = request.form.get("Stay_In_Current_City_Years"),
            Marital_Status = int(request.form.get("Marital_Status")),
            Product_Category_1 = request.form.get("Product_Category_1"),
            Product_Category_2 = request.form.get("Product_Category_2"),
            Gender = request.form.get("Gender"),
            Age=request.form.get('Age'),
            City_Category=request.form.get('City_Category')
        )

        pred_df  = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print(f"Predicted value is {results[0]}")
     
        return render_template('home.html', results=round(results[0],3))
    
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8080)
    app.run(host='0.0.0.0', port=8080, debug=True)

