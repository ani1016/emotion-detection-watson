import requests

def emotion_detector(text_to_analyze):

    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

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
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    emotions = response.json()["emotion"]["document"]["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
  
