import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting the emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Format the result
    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return result

