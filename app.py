import streamlit as st
import pickle
import requests

tab1, tab2 = st.tabs(["Home","About"])
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values
st.header("Movie Recommender System")
selectvalue=st.selectbox("Select movie from dropdown",movies_list)
def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path
import streamlit as st

st.sidebar.title("Top 10 Highest-Grossing Movies")

top_10_movies = [
    "Avatar (2009)",
    "Avengers: Endgame (2019)",
    "Titanic (1997)",
    "Star Wars: The Force Awakens (2015)",
    "Avengers: Infinity War (2018)",
    "The Lion King (2019)",
    "The Avengers (2012)",
    "Avengers: Age of Ultron (2015)",
    "The Incredibles 2 (2018)",
    "Beauty and the Beast (2017)",
]

for movie in top_10_movies:
    st.sidebar.text(movie)
with tab1:
  
    def recommend(movie):
        index=movies[movies['title']==movie].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
        recommend_movie=[]
        recommend_poster=[]
        for i in distance[1:6]:
            movies_id=movies.iloc[i[0]].id
            recommend_movie.append(movies.iloc[i[0]].title)
            recommend_poster.append(fetch_poster(movies_id))
        return recommend_movie, recommend_poster



if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])

with tab2:
    st.text("About")
    st.image("ml_project_image.jpg")
    st.write("Welcome to our innovative movie recommendation system, where we leverage Support Vector Machines (SVM) for content-based filtering. Our journey begins with meticulous data collection, encompassing a rich array of movie details, from genres and actors to directors and user ratings. In the realm of data preprocessing, we ensure a seamless and consistent experience by addressing any inconsistencies or missing values. We then transition into the art of feature extraction, shaping movie characteristics into dynamic vectors that spotlight genre, cast, and director. The magic unfolds through TF-IDF vectorization, translating textual data like movie descriptions into numerical vectors. Our SVM algorithm takes center stage, calculating the nuanced similarity between movies based on their thoughtfully crafted feature vectors. With the SVM model gracefully trained on preprocessed data, the system orchestrates recommendations by identifying akin movies for a given selection, anchored in SVM similarity scores. As the curtain falls, we meticulously evaluate our system's performance, employing metrics such as precision, recall, and mean squared error. Join us on this cinematic journey, where every recommendation is a curated masterpiece.")
    st.text("Made By:")
    st.code("Amitesh Jha ")
   
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)