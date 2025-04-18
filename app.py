import streamlit as st
import joblib
import numpy as np

# Load the saved similarity matrix
similarity_matrix = joblib.load("food_recommendation_model.pkl")

# Full dish names list
dishes = [
    'Chole Bhature', 'Vada Pav', 'Gulab Jamun', 'Pesarettu', 'Poha', 'Pav Bhaji',
    'Chepala Pulusu', 'Kheer', 'Masala Dosa', 'Samosa', 'Biryani', 'Upma', 
    'Jalebi', 'Rajma Chawal', 'Pesarattu Upma', 'Dhokla', 'Mysore Pak', 
    'Palak Paneer', 'Khichdi', 'Rasgulla'
]

# Streamlit App UI
st.set_page_config(page_title="Food Recommendation System", layout="wide")

# Wooden-style background
wood_bg = """
<style>
body {
    background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
    background-size: cover;
    color: #ffffff;
}
.title {
    font-size: 40px;
    color: #FFDEAD;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
}
</style>
"""
st.markdown(wood_bg, unsafe_allow_html=True)
st.markdown('<div class="title">Delicious Indian Dish Recommender</div>', unsafe_allow_html=True)

# Dropdown for user input
selected_dish = st.selectbox("Choose your favorite Indian dish:", dishes)

# Recommendation logic
def recommend_dishes(selected_dish, similarity_matrix, dishes):
    index = dishes.index(selected_dish)
    scores = list(enumerate(similarity_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommended = [dishes[i[0]] for i in scores[1:6]]  # top 5 excluding selected
    return recommended

# Show recommendations
if st.button("Recommend Me!"):
    recommendations = recommend_dishes(selected_dish, similarity_matrix, dishes)
    st.success("Here are some dishes you might enjoy:")
    for i, rec in enumerate(recommendations, 1):
        st.write(f"{i}. {rec}")
