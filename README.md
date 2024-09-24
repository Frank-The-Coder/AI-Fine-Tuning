# Chatbot Application with OpenAI API

This is a simple web-based chatbot application built using Flask and the OpenAI API. The chatbot allows users to ask questions, and it returns responses powered by OpenAI's `gpt-3.5-turbo` (or `gpt-4`) model. This project uses fine-tuned models to provide more tailored responses based on your custom data.

## Features

- Flask backend to serve the chatbot and handle requests
- Custom responses using OpenAI's fine-tuned model
- Simple web interface with real-time user interaction
- Responses returned in real-time from OpenAI's API

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/Frank-The-Coder/AI-Fine-Tuning.git
cd AI-Fine-Tuning
```

### 2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up the OpenAI API key:

You will need an OpenAI API key to run this project. Create a `.env` file in the root of your project and add the following line, replacing `<YOUR_API_KEY>` with your actual key.

```
OPENAI_API_KEY=<YOUR_API_KEY>
```

Alternatively, you can set the `OPENAI_API_KEY` environment variable directly in your shell.

## Running the Application

Once everything is set up, you can run the Flask application:

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`. Open this address in your browser to interact with the chatbot.

## Usage

- After running the app, go to `http://127.0.0.1:5000`.
- You will see a simple interface with a text input box and a send button.
- Type a message or question in the input box and press enter or click "Send."
- The chatbot will reply based on the fine-tuned OpenAI model.

### Example interaction:

1. **User:** _What is OpenAI?_
2. **Chatbot:** _OpenAI is an artificial intelligence research organization..._

## Project Structure

```
your_project/
│
├── app.py                   # Main Flask app
├── templates/
│   └── index.html            # Frontend HTML file
├── static/
│   ├── chatbot.css           # Frontend CSS file
│   └── chatbot.js            # Frontend JavaScript file
├── venv/                     # Virtual environment
├── .gitignore                # Ignored files
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation (this file)
└── .env                      # OpenAI API key (optional)
```

### `app.py`

- This file contains the main Flask app which serves the chatbot interface and communicates with the OpenAI API.
- API requests are sent from the frontend and processed by OpenAI's `gpt-3.5-turbo` model (or your fine-tuned model).

### `static/`

- Contains static assets like CSS and JavaScript.
- The `chatbot.js` script handles frontend functionality like sending user messages and displaying responses.

### `templates/`

- Contains HTML templates. `index.html` is the main page that users interact with.

### `.env`

- A hidden file containing sensitive environment variables like your OpenAI API key.

## Environment Variables

This project requires an OpenAI API key to function. Ensure that the following environment variable is set:

- `OPENAI_API_KEY`: Your OpenAI API key. Set it in `.env` or export it as an environment variable.

Example `.env` file:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Alternatively, you can export the variable directly from your terminal:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

## Contributing

Feel free to contribute to this project by forking the repository and submitting pull requests. You can also open issues for feature requests or bugs.

### To contribute:

1. Fork the project.
2. Create a new branch for your feature: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
