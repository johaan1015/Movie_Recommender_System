import pandas as pd
import streamlit as st
import pickle
import requests

def recommend_movie(option):
    movie_index = movies[movies["title"] == option].index[0]
    distances = similarity[movie_index]
    movies_list_index = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_list=[]
    recommended_movies_poster=[]
    for i in movies_list_index:
        recommended_movies_list.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))

    return recommended_movies_list,recommended_movies_poster

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=67ddd6bbee0592ea4cd707c65e0aabc6&language=en-US%27".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original"+data["poster_path"]
movies_dict = pickle.load(open("movies.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
movies=pd.DataFrame(movies_dict)


st.title("Movie Recommender System")
option = st.selectbox(
    'Select a movie',
    movies["title"].values)
if st.button('Recommend'):
    movies, poster = recommend_movie(option)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(movies[0])
        st.image(poster[0])

    with col2:
        st.text(movies[1])
        st.image(poster[1])

    with col3:
        st.text(movies[2])
        st.image(poster[2])
    with col4:
        st.text(movies[3])
        st.image(poster[3])
    with col5:
        st.text(movies[4])
        st.image(poster[4])