#from sklearn.metrics.pairwise import cosine_similarity
#from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import os
import random

SONG_DIR = "data"
    
def load_data(fileName):
    data = pd.read_csv(os.path.join(SONG_DIR,fileName))
    return data

def filterGenre(data):
    if data[0]=='[':
        data = data.strip('[]').replace(' ','').replace("'",'')
        return data.split(',')
    else:
        return list(data)
    
def selectRandom(category,recommendedEmotion):
    if category == 'mood':
        data = load_data("spotify_songs.csv")
        yourRecommendation = data[data[category] == recommendedEmotion]
        choose = 50
        returnList = ['name','album','artist']
    else:
        data = load_data("AnimeWorld.csv")
        data.Genre = data[category].apply(filterGenre)
        yourRecommendation = data[data.Genre.map(lambda x:recommendedEmotion in x)]
        choose = 10
        returnList = ['Anime','Description']
    
    value = random.randint(0,choose)
    yourRecommendation = yourRecommendation[returnList].iloc[value:value+6]
    return yourRecommendation
    
def songRecommendation(predictedEmotion):
    predictedEmotion = predictedEmotion.lower()
    if predictedEmotion == 'happy':
        choice = random.choice(['Calm','Sad'])
        yourRecommendation = selectRandom('mood',choice)
            
    elif predictedEmotion in ['sad','fear']:
        yourRecommendation = selectRandom('mood',"Happy") 
        
    elif predictedEmotion in ["angry","disgust"]:
        yourRecommendation = selectRandom('mood',"Calm")
        
    elif predictedEmotion in ['surprised','neutral']:
        yourRecommendation = selectRandom('mood',"Energetic")
    
    else:
        return("Invalid")
    
    return yourRecommendation
    
def movieRecommendation(predictedEmotion):
    predictedEmotion = predictedEmotion.lower()
    if predictedEmotion == 'happy':
        choice = random.choice(['Action','Horror','Adventure'])
        yourRecommendation = selectRandom('Genre',choice)
            
    elif predictedEmotion in ['sad','fear']:
        choice = random.choice(['Comedy','Sci-Fi','Romance'])
        yourRecommendation = selectRandom('Genre',choice) 
        
    elif predictedEmotion in ["angry","disgust"]:
        yourRecommendation = selectRandom('Genre',"Comedy")
        
    elif predictedEmotion in ['surprised','neutral']:
        choice = random.choice(['Drama','Sci-Fi','Fantasy','Mystery'])
        yourRecommendation = selectRandom('Genre',choice)
    
    else:
        return("Invalid")
    
    return yourRecommendation

def contentBasedRecommendation():
    pass