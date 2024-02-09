import os

def get_dataset_path(emotion):
  emotions_data = {
      "angry": "../datasets/angry_songs.csv",
      "disgust": "../datasets/disgust_songs.csv",
      "fear": "../datasets/fear_songs.csv",
      "happy": "../datasets/happy_songs.csv",
      "sad": "../datasets/sad_songs.csv",
      "surprise": "../datasets/surprise_songs.csv",
      "neutral": "../datasets/neutral_songs.csv",
  }
  return os.path.join(os.path.dirname(__file__), emotions_data.get(emotion))

def find_dataset(emotion):
  return get_dataset_path(emotion)
