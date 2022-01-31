# Movie-Recommendation-system

This application provides all the details of the requested movie such as overview, genre, release date, runtime, top cast, recommended movies, etc.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API.
This is a Streamlit based app which takes a movie and by the help of **Content Based Filtering** recommend five other movies.

# Similarity Score
How does it decide which item is most similar to the item user likes? Here we use the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

# How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![image](https://user-images.githubusercontent.com/84233710/151780428-5e49342f-14da-487b-946e-34ac92870df2.png)

More about Cosine Similarity : https://www.machinelearningplus.com/nlp/cosine-similarity/

# Link for Similarity.pkl :
https://drive.google.com/file/d/1nD8_DTsFeWAtfogU6YBAy0L9gncF4q1E/view?usp=sharing

# Source of Dataset:
https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv
