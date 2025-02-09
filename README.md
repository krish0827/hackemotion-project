Emotion Detection Using Text:

This is a  web application that utilizes a Hugging Face model to detect emotions from user-provided text. Based on the detected emotion, the app displays a mood-enhancing message to improve the user's emotional well-being.

Features:

Emotion Detection: The app uses a pre-trained Hugging Face model (j-hartmann/emotion-english-distilroberta-base) to classify the emotion behind the input text.
Mood Enhancement: Displays a motivational message based on the detected emotion to help uplift the user’s mood.

Installation:

Clone this repository to your local machine:
git clone https://github.com/yourusername/emotion-detection-web.git
cd emotion-detection-web

Set up a Python environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required Python libraries:
pip install transformers flask  # Flask is optional for serving API

The requirements.txt file should include the following dependencies:

transformers==4.9.2
flask==2.0.1  # Optional if you want to serve the app via Flask
Start the Python backend script (app.py) to load the Hugging Face model and handle API requests:
python app.py

Open index.html in your browser to interact with the app. The frontend is built using HTML, CSS, and JavaScript.

How It Works

The user is presented with a text input field on the web page.
After submitting the text, the app uses the Hugging Face emotion classification model to analyze the emotion in the input text.
A relevant mood-enhancing message is displayed based on the detected emotion.

License
This project is licensed under the MIT License - see the LICENSE file for details.
