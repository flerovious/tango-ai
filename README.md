## Tango AI: Revolutionizing Education with AI-Driven Teaching Assistance
Tango AI is an innovative educational technology platform designed specifically for educators, aiming to revolutionize the way teaching content is delivered. At its core, Tango AI utilizes cutting-edge artificial intelligence to facilitate the creation of guided questions and answers, making it an invaluable tool in the arsenal of educators striving to enhance the learning experience for students of all ages and levels.

## Features
- **Custom Question Generation:** Generate questions based on specific topics or textbooks.
- **Intelligent Answering System:** Provides well-structured answers to assist in teaching.
- **User-Friendly Interface:** Easy to navigate and use for all levels of tech-savviness.

## Installation

### Prerequisites
- Tango AI requires Python 3.9 or later.
- Ensure you have an internet connection for downloading dependencies.

### Setting Up

1. **Install Poetry:**
   Poetry is used for dependency management. If you do not have Poetry installed, follow the installation instructions here: [Poetry Installation Guide](https://python-poetry.org/docs/#installing-with-pipx).

2. **Clone the Repository:**
   Clone the Tango AI repository to your local machine using Git:
   ```
   git clone https://github.com/gabyang/tango-ai.git
   cd tango-ai
   ```

3. **Install Dependencies:**
   Run the following command to install the required dependencies:
   ```
   poetry install
   ```

4. **Activate the Virtual Environment:**
   Enter the virtual environment created by Poetry:
   ```
   poetry shell
   ```

5. **Run Tango AI:**
   Navigate to the source directory and start the application:
   ```
   cd src
   streamlit run app.py
   ```

## Usage

After starting Tango AI, navigate to `http://localhost:8501` in your web browser to access the application. Follow the on-screen instructions to generate questions and answers.

## Support

For support, issues, or contributions, please visit the [GitHub Issues page](https://github.com/gabyang/tango-ai/issues).

## License

Tango AI is released under the MIT License. See the LICENSE file for more details.

Tango AI uses chemistry questions from chemPRIME (Moore Et. Al) for demonstration purposes. ChemPRIME is a collaborative project in which concepts and contexts can be contributed by anyone and used free of charge by anyone for non-commercial purposes.
