import requests

def emotion_detector(text_to_analyze):

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again."

    url = "YOUR_URL"
    headers = {"Content-Type": "application/json"}

    payload = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        auth=("apikey", "YOUR_API_KEY")
    )

    if response.status_code != 200:
        return "Error in API call."

    emotions = response.json()["emotion"]["document"]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    dominant_emotion = max(emotions, key=emotions.get)

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
