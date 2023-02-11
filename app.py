import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cca1b7ef701bae29b42984953f3fdeae'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

all_movie_list = movies_list['title'].values


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movie = []
    recommend_movie_posters = []
    for i in movie_list:
        movie_id = movies_list.movie_id[i[0]]
        recommend_movie.append(movies_list.title[i[0]])
        recommend_movie_posters.append(fetch_poster(movie_id))
    return recommend_movie, recommend_movie_posters


st.title("Movie Recommender System")

selected_movie = st.selectbox(
    'How would you like to be contacted?',
    all_movie_list)

st.write('You selected:', selected_movie)

if st.button('Please Recommend'):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

