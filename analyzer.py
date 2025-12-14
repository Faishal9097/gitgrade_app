import os
import shutil
import tempfile
import glob
import lizard
import pandas as pd


class RepositoryAnalyzer:
    def __init__(self, project_path):
        self.project_path = project_path
        self.repo_name = os.path.basename(project_path)

    def get_file_tree(self, limit=50):
        tree_str = ""
        count = 0

        for root, dirs, files in os.walk(self.project_path):
            level = root.replace(self.project_path, "").count(os.sep)
            indent = " " * 4 * level
            tree_str += f"{indent}{os.path.basename(root)}/\n"

            for f in files:
                tree_str += f"{indent}    {f}\n"
                count += 1
                if count > limit:
                    tree_str += "... (truncated)\n"
                    return tree_str
        return tree_str

    def calculate_complexity(self):
        analysis = lizard.analyze([self.project_path])

        file_data = []
        total_ccn = 0
        file_count = 0

        for file in analysis:
            if not file.function_list:
                continue

            rel_path = file.filename.replace(self.project_path, "")

            file_data.append({
                "filename": rel_path,
                "nloc": file.nloc,
                "ccn": file.average_cyclomatic_complexity,
                "functions": len(file.function_list)
            })

            total_ccn += file.average_cyclomatic_complexity
            file_count += 1

        avg_ccn = round(total_ccn / file_count, 2) if file_count else 0
        return avg_ccn, pd.DataFrame(file_data)

    def health_check(self):
        checks = {
            "README": False,
            "Tests": False,
            "Docker/Deployment": False,
            "Dependencies": False
        }

        if glob.glob(os.path.join(self.project_path, "README*")):
            checks["README"] = True

        if glob.glob(os.path.join(self.project_path, "**/*test*"), recursive=True):
            checks["Tests"] = True

        if os.path.exists(os.path.join(self.project_path, "Dockerfile")):
            checks["Docker/Deployment"] = True

        if os.path.exists(os.path.join(self.project_path, "requirements.txt")):
            checks["Dependencies"] = True

        score = sum(v for v in checks.values()) * 25
        return score, checks

    def get_readme_content(self):
        readmes = glob.glob(os.path.join(self.project_path, "README*"))
        if readmes:
            with open(readmes[0], "r", encoding="utf-8", errors="ignore") as f:
                return f.read()[:2000]
        return "No README found."
