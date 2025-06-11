import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests


def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Check if 'poster_path' exists and is not None
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return None  # Return None if no poster path is available
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster for movie ID {movie_id}: {e}")
        return None


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distance = similarity[movie_index]
        movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        for i in movie_list:
            movie_id = movies.iloc[i[0]].movie_id  # Assuming 'movie_id' is the correct column name

            recommended_movies.append(movies.iloc[i[0]].title)
            poster_url = fetch_poster(movie_id)
            if poster_url:  # Only append if poster_url is not None
                recommended_movies_posters.append(poster_url)
            else:
                recommended_movies_posters.append("https://via.placeholder.com/500x750?text=No+Poster+Available")

        return recommended_movies, recommended_movies_posters
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
        return [], []


# Load movie data and similarity matrix
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    if names and posters:  # Only display if recommendations are found
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.header(names[0])
            st.image(posters[0])

        with col2:
            st.header(names[1])
            st.image(posters[1])

        with col3:
            st.header(names[2])
            st.image(posters[2])

        with col4:
            st.header(names[3])
            st.image(posters[3])

        with col5:
            st.header(names[4])
            st.image(posters[4])
    else:
        st.warning("No recommendations found or an error occurred.")