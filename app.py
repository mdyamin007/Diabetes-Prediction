from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

def predict():
    set_env(title='Diabetes Prediction')
    age = input('Enter your age', type=NUMBER)
    bmi = input('Enter your BMI(Body Mass Index)', type=FLOAT)
    pregnancies = input('Number of Pregnancies', type=NUMBER)
    glucose = input('Please enter Plasma glucose concentration', input=NUMBER)
    blood_pressure = input('Enter your diastolic blood pressure (mm Hg)', input=NUMBER)
    skin_thickness = input('Triceps skin fold thickness (mm)')
    insulin = input('2-Hour serum insulin (mu U/ml)', type=NUMBER)
    dpf = input('Diabetes pedigree function', type=FLOAT)
    prediction = model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    if prediction[0] == 1:
        put_markdown('# You might have diabetes')
    else:
        put_markdown('# You might not have diabetes')


app.add_url_rule('/', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])

if __name__ == '__main__':
    app.run()