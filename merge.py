import nbformat

def merge_notebooks(notebook_paths, output_path):
    merged_nb = nbformat.v4.new_notebook()

    for path in notebook_paths:
        with open(path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            merged_nb.cells.extend(nb.cells)

    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(merged_nb, f)

if __name__ == "__main__":
    notebook_paths = ["Project_Proposal.ipynb", "Project_Cleaning.ipynb", "Exploratory_Analysis.ipynb", "random_forest.ipynb", "regression.ipynb"]
    output_path = "Final_Submission.ipynb"
    merge_notebooks(notebook_paths, output_path)