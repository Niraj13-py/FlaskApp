# 🎬  Movie Recommender (Flask App)

This is a Flask-based web application that recommends similar movies using metadata from TMDb (The Movie Database). It uses **TF-IDF** and **cosine similarity** on combined textual features (like cast, genres, keywords, and director) to find the top 10 similar movies.

---

## 🚀 Features

- Search any movie from TMDb
- Get top 10 similar movies
- View homepage links and release dates
- Built-in Kaggle dataset downloader via `kagglehub`
- Bootstrap 5-based responsive UI (dark mode)

---

## 📂 Folder Structure

project/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│ ├── index.html
│ ├── found.html
│ └── notFound.html

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
2. Create a Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set up Kaggle API Authentication
Go to: https://www.kaggle.com/account

Click "Create API Token"

Move kaggle.json to:

bash
Copy
Edit
Windows: C:\Users\<your-username>\.kaggle\kaggle.json
Or set environment variables:

bash
Copy
Edit
export KAGGLE_USERNAME=your_username
export KAGGLE_KEY=your_api_key
▶️ Run the App
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:8080






![image](https://github.com/user-attachments/assets/9111a6f2-ea2e-4c1c-86f3-c78428f9cf73)









![image](https://github.com/user-attachments/assets/f64de916-138b-4708-95c8-07b58bf76161)

