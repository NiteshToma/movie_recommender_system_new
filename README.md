# 🎬 Movie Recommender System using NLP & Streamlit

This is a **Content-Based Movie Recommender System** built with **Python, NLP, and Streamlit**. It suggests movies similar to the one selected by the user, using text analysis on movie metadata like titles, overviews, and genres.

---

## 🚀 Features

- 📌 Recommends similar movies based on content
- 🧠 Uses **NLP techniques** (TF-IDF & Cosine Similarity)
- 🎭 Fetches and displays movie posters via TMDB API
- ⚡ Simple and fast web interface built with Streamlit
- ☁️ Deployable on Streamlit Cloud or Heroku

---

## 🧠 Tech Stack

- Python 3.x
- **Natural Language Processing (NLP)**
  - TF-IDF Vectorization
  - Cosine Similarity
- Pandas, NumPy
- Scikit-learn
- Pickle (for storing processed data)
- Streamlit (for UI)
- Requests (for TMDB API)

---

## 📁 Project Structure

pythonProject-movie-recommender-system/
│
├── main.py # Streamlit app script
├── movie_dict.pkl # Dictionary with movie metadata
├── similarity.pkl # Cosine similarity matrix
├── requirements.txt # All Python dependencies
├── Procfile # For Heroku deployment (optional)
├── runtime.txt # Python version for deployment
├── .gitignore # Files/folders to ignore
├── README.md # Project documentation

yaml
Copy
Edit

---

## 📚 How NLP is Used

This recommender system uses **Natural Language Processing** to understand movie descriptions and calculate similarity:

- 🧹 **Text Preprocessing**: Title, overview, genres are cleaned and combined
- 📊 **TF-IDF Vectorization**: Converts text into numerical form
- 📐 **Cosine Similarity**: Calculates similarity between movies based on TF-IDF vectors

These steps allow the system to recommend movies with similar descriptions/content.

---

## ▶️ How to Run Locally

1. **Clone the Repository**
```bash
git clone https://github.com/NiteshToma/movie-recommender-system.git
cd movie-recommender-system
Create a Virtual Environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the App

bash
Copy
Edit
streamlit run main.py
🌍 Deploy on Streamlit Cloud
Go to Streamlit Cloud
Click "New App"

Connect your GitHub repo

Set main.py as the entry point

Click "Deploy"

✅ Your app will be live in a few seconds!

📸 Sample Screenshot

👨‍💻 Author
Nitesh Tomar
📬 GitHub | LinkedIn

