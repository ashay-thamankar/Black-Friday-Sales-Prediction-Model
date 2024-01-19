import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            scaled_data = preprocessor.transform(features)
            preds  = model.predict(scaled_data)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 User_ID: int,
                 Occupation: int,
                 Stay_In_Current_City_Years:int,
                 Marital_Status: int,
                 Product_Category_1:int,
                 Product_Category_2:int,
                 Gender:str,
                 Age:str,
                 City_Category:str

                 ):
        self.User_ID = User_ID
        self.Occupation = Occupation
        self.Stay_In_Current_City_Years  =Stay_In_Current_City_Years
        self.Marital_Status = Marital_Status
        self.Product_Category_1 = Product_Category_1
        self.Product_Category_2 = Product_Category_2
        self.Gender = Gender
        self.Age = Age
        self.City_Category = City_Category


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "User_ID": [self.User_ID],
                "Occupation": [self.Occupation],
                "Stay_In_Current_City_Years": [self.Stay_In_Current_City_Years],
                "Marital_Status": [self.Marital_Status],
                "Product_Category_1": [self.Product_Category_1],
                "Product_Category_2": [self.Product_Category_2],
                "Gender": [self.Gender],
                'Age': [self.Age],
                'City_Category': [self.City_Category]

            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)