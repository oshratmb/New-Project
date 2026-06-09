# New Project

A small Python utility that scaffolds a sample project directory structure on disk.

## Overview

Running `test.py` creates a `project_name` folder with a minimal layout suitable for a Python application: source code, tests, and a starter README.

## Requirements

- Python 3.x
- No third-party dependencies

## Usage

From the project root:

```bash
python test.py
```

You should see:

```
hi
Sample project structure created.
```

## Generated Structure

After running the script, the following files and folders are created:

```
project_name/
├── src/
│   └── main.py          # Prints "Hello, World!"
├── tests/
│   └── test_main.py     # Simple example test
└── README.md            # Placeholder project README
```

## How It Works

`test.py` defines a nested dictionary representing the desired directory tree. The `create_structure` function walks that dictionary recursively:

- **Dictionary values** become subdirectories (created with `os.makedirs`).
- **String values** become files, with the string written as file contents.

To customize the scaffold, edit the `project_structure` dictionary in `test.py`.

## License

No license specified.
