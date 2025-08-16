import streamlit as st
from PIL import Image

st.set_page_config(page_title="Mini Quiz AI Acronyms", page_icon="🧠")

st.title("- WELCOME TO MY MINI QUIZ -")

# Load and display image
try:
    image = Image.open("fael.jpg")
    st.image(image, width=200)
except FileNotFoundError:
    st.warning("Gambar 'fael.jpg' tidak ditemukan. Pastikan gambar berada di direktori yang sama.")
    st.image("https://via.placeholder.com/200", width=200, caption="Placeholder Image")

st.write("**Nama** : M. Hanif")
st.write("**Student ID** : REAPYTHON3WVTDF")
st.write("**Class** : AI-python Bootcamp")
st.write("_________________________________")

user_name = st.text_input("Masukan nama anda")

if user_name:
    st.write(f"Selamat datang {user_name}!")
    st.write("**Jawablah pertanyaan di bawah ini dengan benar!**")

    score = 0

    # Fun Project 1: Quiz on AI Acronyms
    st.title("Quiz: AI Acronyms 🤖👾🦾")
    qna = {
        "apa kepanjangan dari AI?": "artificial intelligence",
        "apa kepanjangan dari ML?": "machine learning",
        "apa kepanjangan dari DL?": "deep learning",
        "apa kepanjangan dari NLP?": "natural language processing",
        "apa kepanjangan dari CV?": "computer vision",
    }

    # Display the questions and collect answers
    for i, (question, correct_answer) in enumerate(qna.items()):
        st.subheader(f"Pertanyaan {i+1}:")
        user_answer = st.text_input(question, key=f"q_{i}")

        if user_answer:
            if user_answer.lower() == correct_answer.lower():
                score += 1
                st.success("**Jawaban benar!**")
            else:
                st.warning("Coba pikir baik-baik")

    # Display the final score
    st.write(f"### Skor akhir Anda: {score}/{len(qna)}")

    # Apresiasi jika semua jawaban benar
    if score == len(qna):
        st.write("**Kamu pintar banget! dan Kamu cocok jadi Master AI!!!**")
        st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2pkN2Q1Z2Vmdm05a2g3MDd6YWxpZ3I5ZzliZ2JheWEwaDJ1MnU4bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/X9izlczKyCpmCSZu0l/giphy.gif")
    else:
        st.write("Ayo semangat kamu pasti bisa!")
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHlzc3g5ZnBpMWp5bWIxZjR3bWtkcjNkeTVoZDE4ZWVrNWptdWlpayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CaiVJuZGvR8HK/giphy.gif")

st.title("terimakasih telah berpatisipasi 👍🏻")

