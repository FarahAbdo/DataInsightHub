from flask import Flask, request, render_template
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

app = Flask(__name__)
chat = ChatOpenAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'csvFile' not in request.files:
        return "No file part"
    
    file = request.files['csvFile']
    
    if file.filename == '':
        return "No selected file"
    
    # Process the uploaded CSV file
    electric_cars = pd.read_csv(file)
    
    # Perform data analysis using your existing code

    # Example: Suggest questions using langchain
    dataset_description = """
    You have a dataset about electric cars registered in Washington state, USA in 2020. It is available as a pandas DataFrame named `electric_cars`.
    Each row in the dataset represents the count of the number of cars registered within a city, for a particular model.
    """
    suggest_questions = "Suggest some data analysis questions that could be answered with this dataset."
    msgs_suggest_questions = [
        SystemMessage(content="You are a data analysis expert."),
        HumanMessage(content=f"{dataset_description}\n\n{suggest_questions}")
    ]
    rsps_suggest_questions = chat(msgs_suggest_questions)
    analysis_results = rsps_suggest_questions.content

    # Return the analysis results or questions to the user
    return analysis_results

if __name__ == '__main__':
    app.run()
