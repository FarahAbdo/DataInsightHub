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
        df = pd.read_csv(file)
    except pd.errors.EmptyDataError:
        return "No data found in the CSV file"
    
    # Create a new ChatOpenAI instance for each analysis
    chat_instance = ChatOpenAI()

    # Generate dataset description dynamically with additional context
    dataset_description = f"""
    You have a dataset with {df.shape[0]} rows and {df.shape[1]} columns.
    Here is some additional information about the dataset:\n
    - Column names: {', '.join(df.columns)}\n
    - Data types: {', '.join(df.dtypes.astype(str))}\n
    - Unique values per column:\n{df.nunique()}\n
    - Summary statistics:\n{df.describe()}
    """

    # Example: Suggest questions using langchain
    suggest_questions = "Suggest some specific data analysis questions that could be answered with this dataset."
    msgs_suggest_questions = [
        SystemMessage(content="You are a data analysis expert."),
        HumanMessage(content=f"{dataset_description}\n\n{suggest_questions}")
    ]
    
    rsps_suggest_questions = chat_instance(msgs_suggest_questions)
    
    # Extract questions and separate them with newline
    questions = rsps_suggest_questions.content.split('\n')

    # Return each question in a separate line
    return render_template('analyze.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
