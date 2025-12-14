import streamlit as st
from analyzer import RepositoryAnalyzer
from ai_agent import generate_feedback

st.set_page_config(page_title="GitGrade (Local)", page_icon="🚀", layout="wide")

st.title("🚀 GitGrade – Local Project Analyzer")
st.markdown("Analyze any **local project folder**.")

with st.sidebar:
    project_path = st.text_input(
        "Project Folder Path",
        placeholder="C:/Users/Faishal/my_project"
    )
    analyze_btn = st.button("Analyze", type="primary")

if analyze_btn and project_path:
    if not project_path or not project_path.strip():
        st.error("Please provide a valid folder path.")
    else:
        analyzer = RepositoryAnalyzer(project_path)

        with st.spinner("Analyzing project..."):
            tree = analyzer.get_file_tree()
            complexity, file_df = analyzer.calculate_complexity()
            health_score, health_checks = analyzer.health_check()
            readme = analyzer.get_readme_content()

            ai_feedback = generate_feedback(
                analyzer.repo_name,
                tree,
                complexity,
                health_score,
                health_checks,
                readme
            )

        col1, col2, col3 = st.columns(3)
        col1.metric("Health Score", f"{health_score}/100")
        col2.metric("Avg Complexity", complexity)
        col3.metric("Files Analyzed", len(file_df))
