![movie](https://github.com/user-attachments/assets/ff97f81b-901c-4ab2-a467-30934145af8c)
![Screenshot 2025-06-25 193256](https://github.com/user-attachments/assets/761c7195-0b9f-4171-82bc-afb99842c9e8)
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








