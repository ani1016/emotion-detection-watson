from flask import Flask, request, jsonify
from 2a_emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text = request.args.get("text")

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return jsonify({
            "error": "Invalid text! Please try again."
        }), 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
