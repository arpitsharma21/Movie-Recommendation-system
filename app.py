from cgitb import reset
from turtle import width
from requests.api import post
import streamlit as st
import pickle
import pandas as pd
import requests

def movie_details(movie):
    index = movies.loc[movies['title'] == movie].iloc[0][0]
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(index))
    data = response.json()
    
    poster = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    title = movies.loc[movies['title'] == movie].iloc[0][1]

    return poster,title,data['overview'],data['release_date'],data['runtime']

def fetch_profile_path(path):
    return "https://image.tmdb.org/t/p/w500/"+ path

def get_crew(movie):
    index = movies.loc[movies['title'] == movie].iloc[0][0]
    response = requests.get("https://api.themoviedb.org/3/movie/{}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(index))
    data = response.json()
    profile_path = []
    character_name = []
    original_name = []
    counter = 0
    for i in (data['cast']):
        if counter < 6:
            profile_path.append(fetch_profile_path(i['profile_path']))
            original_name.append(i['name'])
            character_name.append(i['character'])
        counter += 1
    return profile_path,original_name,character_name
  

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),
                        reverse=True,key = lambda x: x[1])[1:6]
    # It provides 2 things one index and other distance of that movie from others
   
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.set_page_config(layout='wide')
with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html = True)

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox('Enter Movie Name',movies['title'].values)
st.write("")

if st.button('Enter'):

# *********** Movie Details ************************************************
    col1, col2 = st.columns([1,3])
    pos,titl,over,date,run = movie_details(selected_movie_name)
 
    with col1:
        st.image(pos,width = 240)

    with col2:
       st.header(titl)
       st.markdown("<h5>Overview</h5>",unsafe_allow_html=True)
       st.write(over)
       st.write("Release_date:  ",date)
       st.write("Runtime in minutes : ",run)

# *************** Cast ******************************************************
    profile_path, original_name,character_name = get_crew(selected_movie_name)
    _, a = st.columns([2,2])
    with a:
        st.header("Cast")
   
    counter = 0 
    for i in range(2):
        c1,c2,c3 = st.columns(3)
        for j in [c1,c2,c3]:
            if counter <=4:
                with j:
                    st.image(profile_path[counter],width=310)
                    st.write(original_name[counter])
                    st.write("Character Name:",character_name[counter])
                    counter += 1
        st.subheader(" ")

# **************** Recommended ********************************************
    st.write("")
    names,poster = recommend(selected_movie_name)
    
    _, a = st.columns([1,2])
    with a:
        st.header("Recommended Movies")

    counter = 0 
    for i in range(2):
        c1,c2,c3 = st.columns(3)
        for j in [c1,c2,c3]:
            if counter <=4:
                with j:
                    st.image(poster[counter],width=310)
                    counter += 1
        st.subheader(" ")






