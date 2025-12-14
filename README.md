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

Clone the repository
```bash
[git clone https://github.com/your-username/gitgrade-local-analyzer.git](https://github.com/Faishal9097/gitgrade_app)
cd gitgrade-local-analyzer
