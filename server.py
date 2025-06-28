"""Flask server for emotion detection web application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the input form."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """Process user input and return detected emotions."""
    text_to_analyze = request.values.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    