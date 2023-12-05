# Aspire AI / Tango Tutor
First iteration and public repository of Aspire AI - a program designated to output guiding questions and references to textbooks

# First time Setup
## Option 1: Pipenv
Run these command to set up your virtual environment
```
pipenv shell
pipenv install
```
Done! Easy!

## Option 2: Poetry
1. Install poetry if you don't have it installed already. See https://python-poetry.org/docs/#installing-with-pipx
2. Install dependencies
```
poetry install
```
3. Activate the virtual environment
```
poetry shell
```
Done! Easy!

# Troubleshooting
If you encounter an error message while installing the package tiktoken or llama-index
```
[pipenv.exceptions.InstallError]:   note: This error originates from a subprocess, and is likely not a problem with pip.
[pipenv.exceptions.InstallError]:   ERROR: Failed building wheel for tiktoken
[pipenv.exceptions.InstallError]: ERROR: Could not build wheels for tiktoken, which is required to install pyproject.toml-based projects
```

You are missing a rust compiler
Install the Rust compiler: You can install the Rust compiler on your macOS machine using the following command:
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
Don't forget to restart your shell!
