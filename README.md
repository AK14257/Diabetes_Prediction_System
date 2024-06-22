Welcome to the Diabetes Prediction System repository.
This project is designed to predict the likelihood of diabetes in patients based on various medical parameters. 
The system utilizes HTML and CSS for the frontend, Jupyter Notebook for model development and analysis and the Django framework for backend deployment.

Project Overview
The Diabetes Prediction System aims to provide an easy-to-use web interface where users can input medical data and receive predictions about their risk of diabetes.
The system uses a machine learning model trained on a dataset of medical records to make predictions.

Features
User-friendly web interface for inputting medical data
Real-time diabetes risk prediction
Data visualization and model insights through Jupyter Notebooks
Secure and scalable backend powered by Django

Tech Stack
Frontend: HTML, CSS
Backend: Python, Django
Machine Learning: Jupyter Notebook, Pandas, Scikit-learn
Data Storage: CSV file


Installation
To run this project locally, follow these steps:

Clone the repository:

sh
Copy code
git clone https://github.com/your-username/diabetes-prediction-system.git
cd diabetes-prediction-system
Set up a virtual environment:

sh
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the dependencies:
pip install -r requirements.txt
Set up the Django project:
cd diabetes_prediction
python manage.py runserver
Access the web application:
Open your web browser and go to http://127.0.0.1:8000/.

Usage
Frontend:

Navigate to the web application and input the required medical data into the form.
Submit the form to receive a diabetes risk prediction.
Backend:

The Django server handles the form submission, processes the input data, and uses the trained machine learning model to generate a prediction.
The result is then displayed to the user.

Model Development:

Use the diabetes_model.ipynb Jupyter Notebook for data analysis and model training.
The dataset (dataset.csv) is used for training and evaluating the machine learning model.
Dataset
The dataset used in this project is provided as dataset.csv. It contains medical records with features such as age, blood pressure, BMI, and other relevant parameters. The dataset is used to train and test the machine learning model.

Contributing
Contributions are welcome! Please follow these steps to contribute:
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Feel free to reach out if you have any questions or need further assistance. Happy coding!
