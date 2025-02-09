from flask import Flask, render_template, request
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Load the Hugging Face model for emotion detection
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Dictionary for mood enhancement messages based on emotions
mood_messages = {
    'anger': "Take a deep breath and relax. You've got this!",
    'fear': "It's okay to feel scared, but remember, you're stronger than you think.",
    'joy': "Keep smiling, you're doing amazing!",
    'sadness': "It's okay to feel sad sometimes. Take care of yourself, and things will get better.",
    'surprise': "Embrace the unexpected! You might be in for a pleasant change.",
    'disgust': "It's okay to feel disgusted. Focus on the positive around you!",
    'neutral': "Take a moment to relax and enjoy the little things around you."
}

# Home route to render the webpage
@app.route('/', methods=['GET', 'POST'])
def index():
    emotion = ""
    mood_message = ""
    if request.method == 'POST':
        text = request.form['text']  # Get the text input from the form
        if text:
            # Use the Hugging Face model to detect the emotion
            result = emotion_classifier(text)
            # The result is a list of dictionaries with 'label' (emotion)
            emotion = result[0]['label'].lower()  # Convert to lowercase for matching
            # Get the mood enhancement message based on the emotion
            mood_message = mood_messages.get(emotion, "Stay positive!")
    
    return render_template('index.html', emotion=emotion, mood_message=mood_message)

if __name__ == '__main__':
    app.run(debug=True)
