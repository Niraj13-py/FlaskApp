import flask
import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import kagglehub

app = flask.Flask(__name__, template_folder='templates')

# ---------- Download dataset from Kaggle ----------
print("📥 Downloading TMDb dataset from KaggleHub...")
dataset_path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
print("✅ Dataset downloaded to:", dataset_path)

# Full paths to the CSVs
movies_csv = os.path.join(dataset_path, 'tmdb_5000_movies.csv')
credits_csv = os.path.join(dataset_path, 'tmdb_5000_credits.csv')

# ---------- Load and preprocess data ----------
print("🔁 Loading and preprocessing dataset...")

movies = pd.read_csv(movies_csv)
credits = pd.read_csv(credits_csv)

# Merge datasets
movies = movies.merge(credits, on='title')

# Helper functions
def convert(obj):
    try:
        return [i['name'] for i in ast.literal_eval(obj)]
    except:
        return []

def get_director(obj):
    try:
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                return i['name']
    except:
        return ''
    return ''

# Apply processing
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert)
movies['genres'] = movies['genres'].apply(convert)
movies['crew'] = movies['crew'].apply(get_director)

# Build the 'soup'
def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + ' '.join(x['genres']) + ' ' + x['crew']

movies['soup'] = movies.apply(create_soup, axis=1)

# Handle missing fields
movies['homepage'] = movies['homepage'].fillna('#')
movies['release_date'] = movies['release_date'].fillna('Unknown')

# ---------- TF-IDF Vectorization ----------
print("📐 Vectorizing text...")
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['soup'])

# Cosine similarity
print("🔗 Calculating similarity matrix...")
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Reset index and build title mapping
movies = movies.reset_index()
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()
all_titles = movies['title'].tolist()

# ---------- Recommendation Function ----------
def get_recommendations(title):
    global sim_scores
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]

    movie_indices = [i[0] for i in sim_scores]
    return_df = pd.DataFrame({
        'Title': movies['title'].iloc[movie_indices].values,
        'Homepage': movies['homepage'].iloc[movie_indices].values,
        'ReleaseDate': movies['release_date'].iloc[movie_indices].values
    })

    return return_df

# ---------- Flask Routes ----------
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')

    if flask.request.method == 'POST':
        m_name = " ".join(flask.request.form['movie_name'].split())
        if m_name not in all_titles:
            return flask.render_template('notFound.html', name=m_name)
        else:
            result_final = get_recommendations(m_name)
            names = result_final['Title'].tolist()
            releaseDate = result_final['ReleaseDate'].tolist()
            homepage = [link if isinstance(link, str) and len(link) > 3 else '#' for link in result_final['Homepage']]

            return flask.render_template(
                'found.html',
                movie_names=names,
                movie_homepage=homepage,
                movie_releaseDate=releaseDate,
                search_name=m_name,
                movie_simScore=sim_scores
            )

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
