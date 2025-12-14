from langchain_core.prompts import PromptTemplate

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def generate_feedback(repo_name, tree_structure, complexity_score, health_score, health_details, readme_snippet):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    template = """
You are a Senior Software Engineer mentoring a student.

Project: {repo_name}

Complexity Score: {complexity_score}
Health Score: {health_score}
Health Details: {health_details}

Structure:
{tree_structure}

README:
{readme_snippet}

Tasks:
1. Give a 2-line summary
2. Give 3 improvement steps
3. Be professional and encouraging

Use Markdown.
"""

    prompt = PromptTemplate(
        input_variables=[
            "repo_name", "tree_structure", "complexity_score",
            "health_score", "health_details", "readme_snippet"
        ],
        template=template
    )

    response = (prompt | llm).invoke({
        "repo_name": repo_name,
        "tree_structure": tree_structure,
        "complexity_score": complexity_score,
        "health_score": health_score,
        "health_details": health_details,
        "readme_snippet": readme_snippet
    })

    return response.content
