import streamlit as st
from PIL import Image

st.title("- WELCOME TO MY MINI QUIZ -")

image = Image.open("fael.jpg")
st.image(image, width=200)
st.write("**Nama** : M. Hanif")
st.write("**Student ID** : REAPYTHON3WVTDF")
st.write("**Class** : AI-python Bootcamp")
st.write("_________________________________")

user = st.text_input("Masukan nama anda")

st.write("Selamat datang" + " " + user + "!")
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
for q, a in qna.items():
    user_answer = st.text_input(q, key=q)
    if user_answer.lower() == a.lower():
        score += 1
        st.success("**Jawaban benar!**")
    else:
        st.warning("Coba pikir baik-baik")

# Display the final score
st.write(f"Skor akhir Anda: {score}/{len(qna)}")

#apresiasi jika semua jawaban benar 
if score == len(qna) and len(qna) == score:
        st.write("**Kamu pintar banget! dan Kamu cocok jadi Master AI!!!**")
        st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2pkN2Q1Z2Vmdm05a2g3MDd6YWxpZ3I5ZzliZ2JheWEwaDJ1MnU4bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/X9izlczKyCpmCSZu0l/giphy.gif")
else:
        st.write("Ayo semangat kamu pasti bisa!")
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHlzc3g5ZnBpMWp5bWIxZjR3bWtkcjNkeTVoZDE4ZWVrNWptdWlpayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CaiVJuZGvR8HK/giphy.gif")

st.title("terimakasih telah berpatisipasi 👍🏻")