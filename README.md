# DataInsightHub
An innovative data analysis platform designed to empower data analysts with streamlined tool for processing and gaining insights from datasets. Leveraging the capabilities of Azure Function Apps, langchain, and OpenAI, this project offers a robust environment for efficient data analysis tasks.

## Project Structure

```plaintext
project-root/
|-- .github/                 # GitHub Actions workflows or CI/CD configurations
|-- azure/                   # Azure-specific configurations
|-- functions/               # Azure Function App code
|   |-- __init__.py
|   |-- requirements.txt     # Python dependencies
|   |-- host.json            # Azure Function App host configuration
|   |-- local.settings.json  # Local settings for development
|   |-- main.py              # Flask app and integration with langchain
|   |-- templates/           # HTML templates for the web UI
|       |-- index.html
|-- openai/                  # OpenAI-related configurations or helper functions
|-- .gitignore
|-- README.md
|-- requirements.txt         # Main project dependencies
|-- LICENSE
```

### Folders Overview

- **.github/**: GitHub Actions workflows or CI/CD configurations.
- **azure/**: Azure-specific configurations.
- **functions/**: Azure Function App code.
  - **\_\_init\_\_.py**: An empty file indicating that the directory should be treated as a Python package.
  - **requirements.txt**: List of Python dependencies needed for the Azure Function App.
  - **host.json**: Azure Function App host configuration.
  - **local.settings.json**: Local settings for development, such as environment variables.
  - **main.py**: Main Python script containing the Flask app and integration with the langchain code.
  - **templates/**: Directory containing HTML templates for the web UI.
    - **index.html**: HTML file for the main web interface.
- **openai/**: OpenAI-related configurations or helper functions.
- **.gitignore**: Specifies files and directories that should be ignored by version control.
- **README.md**: Project documentation, providing an overview and instructions for developers.
- **requirements.txt**: Main project dependencies, including langchain, Flask, pandas, and other required packages.
- **LICENSE**: A license file specifying the terms under which the code is distributed.


