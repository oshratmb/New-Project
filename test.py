print("hi")
import os

# Define a sample project directory with some subfolders and files
project_structure = {
    "project_name": {
        "src": {
            "main.py": "print('Hello, World!')\n"
        },
        "tests": {
            "test_main.py": "def test_example():\n    assert 1 + 1 == 2\n"
        },
        "README.md": "# Sample Project\n\nThis is a sample project structure.\n"
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            if not os.path.exists(path):
                os.makedirs(path)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

create_structure('.', project_structure)
print("Sample project structure created.")