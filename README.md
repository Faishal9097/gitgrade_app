GitGrade – Local Project Analyzer

AI-powered local repository analyzer designed to assess code complexity, project health, and overall structure of software projects. By combining static analysis with large language models, it generates mentor-style, actionable feedback and clear improvement steps to help students and developers enhance code quality, maintainability, and real-world production readiness.


Features

- Visualizes project file structure
- Calculates cyclomatic complexity using Lizard
- Performs repository health checks:
  - README presence
  - Tests
  - Dependencies
  - Docker/Deployment files
- AI-generated feedback using OpenAI via LangChain
- lean Streamlit-based UI



Tech Stack

- Python
- Streamlit – Frontend UI
- Lizard – Code complexity analysis
- Pandas – Data handling
- LangChain + OpenAI – AI feedback generation



Installation

1. Clone the repository https://github.com/Faishal9097/gitgrade_app

git clone 
cd gitgrade-local-analyzer

2. Create a virtual environment

python -m venv .venv

Activate the environment:
- Windows: .venv\Scripts\activate
- Linux or macOS: source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt


Running the Application

streamlit run app.py

After running the command, open the link shown in the terminal to access the application in your browser.


How It Works

1. Enter the path of a local project folder
2. Click Analyze
3. The tool scans the project structure
4. Code complexity is calculated for source files
5. Basic health checks are performed
6. A summary and improvement suggestions are displayed


Use Cases

- Students reviewing academic projects
- Developers evaluating personal or practice projects
- Quick health checks before project submission
- Learning better project organization and coding habits


Limitations

- Works only with local project folders
- Focuses on basic static analysis
- Does not execute or test the code


Future Enhancements

- Support for remote repositories
- More detailed test and documentation checks
- Exportable analysis reports
- Language-specific insights


Author

Faishal Abrar  
B.Tech (CSE) Student  
Institute of Engineering and Management, Kolkata


License

This project is licensed under the MIT License.
