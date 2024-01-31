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
    
    # Check if the file is not empty
    if file.seek(0, 2) == 0:
        return "Empty file"
    
    # Rewind the file cursor before reading
    file.seek(0)
    
    # Process the uploaded CSV file
    try:
        electric_cars = pd.read_csv(file)
    except pd.errors.EmptyDataError:
        return "No data found in the CSV file"
    
    # Create a new ChatOpenAI instance for each analysis
    chat = ChatOpenAI()

    # Example: Suggest questions using langchain
    dataset_description = f"""
    You have a dataset about {electric_cars.shape[0]} rows and {electric_cars.shape[1]} columns. Analyze it accurately.
    The columns in the dataset are: {', '.join(electric_cars.columns)}.
    The first few rows of the dataset are:\n{electric_cars.head()}
    """
    suggest_questions = "Suggest some specific data analysis questions that could be answered with this dataset."
    msgs_suggest_questions = [
        SystemMessage(content="You are a data analysis expert."),
        HumanMessage(content=f"{dataset_description}\n\n{suggest_questions}")
    ]
    rsps_suggest_questions = chat(msgs_suggest_questions)
    
    # Extract questions and separate them with newline
    questions = rsps_suggest_questions.content.split('\n')

    # Return each question in a separate line
    return '<br>'.join(questions)

if __name__ == '__main__':
    app.run(debug=True)
