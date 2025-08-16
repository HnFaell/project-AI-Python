import streamlit as st
from PIL import Image
import time

# Set page config
st.set_page_config(
    page_title="AI Quiz Mini",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #2E86AB;
        font-size: 2.5em;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .profile-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .quiz-section {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        border-left: 5px solid #2E86AB;
    }
    .score-display {
        text-align: center;
        font-size: 1.5em;
        padding: 20px;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 15px;
        color: white;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .question-container {
        background: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Main title with custom styling
st.markdown('<h1 class="main-title">🤖 WELCOME TO MY MINI AI QUIZ 🤖</h1>', unsafe_allow_html=True)

# Profile section
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            image = Image.open("fael.jpg")
            st.image(image, width=200, caption="Profile Picture")
        except:
            st.image("https://via.placeholder.com/200x200/667eea/white?text=Profile", width=200, caption="Profile Picture")
    
    with col2:
        st.markdown("""
        <div class="profile-section">
            <h3>👨‍🎓 Profile Information</h3>
            <p><strong>📝 Nama:</strong> M. Hanif</p>
            <p><strong>🆔 Student ID:</strong> REAPYTHON3WVTDF</p>
            <p><strong>🎯 Class:</strong> AI-python Bootcamp</p>
            <p><strong>📅 Quiz Date:</strong> {}</p>
        </div>
        """.format(time.strftime("%B %d, %Y")), unsafe_allow_html=True)

st.markdown("---")

# User input section
st.markdown("### 👋 Mari Berkenalan!")
user = st.text_input("🏷️ Masukkan nama Anda:", placeholder="Ketik nama Anda di sini...")

if user:
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%); 
                padding: 15px; border-radius: 10px; text-align: center; margin: 10px 0;">
        <h3>🎉 Selamat datang, {user}! 🎉</h3>
        <p><strong>Jawablah pertanyaan di bawah ini dengan benar!</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress bar placeholder
    progress_bar = st.progress(0)
    
    # Initialize score
    score = 0
    
    # Quiz section
    st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
    st.markdown("## 🧠 Quiz: AI Acronyms")
    st.markdown("*Jawab semua pertanyaan dengan benar untuk mendapatkan skor sempurna!*")
    
    qna = {
        "🤖 Apa kepanjangan dari AI?": "artificial intelligence",
        "🔬 Apa kepanjangan dari ML?": "machine learning", 
        "🧠 Apa kepanjangan dari DL?": "deep learning",
        "💬 Apa kepanjangan dari NLP?": "natural language processing",
        "👁️ Apa kepanjangan dari CV?": "computer vision",
    }
    
    # Display questions with enhanced styling
    answered_questions = 0
    for i, (q, a) in enumerate(qna.items()):
        st.markdown(f'<div class="question-container">', unsafe_allow_html=True)
        st.markdown(f"**Pertanyaan {i+1}/5:**")
        
        user_answer = st.text_input(
            q, 
            key=q,
            placeholder="Ketik jawaban Anda di sini...",
            help="Jawaban tidak case-sensitive"
        )
        
        if user_answer:
            answered_questions += 1
            if user_answer.lower().strip() == a.lower():
                score += 1
                st.success("✅ **Jawaban benar! Excellent!**")
            else:
                st.error("❌ **Jawaban kurang tepat, coba lagi!**")
                st.info(f"💡 **Hint:** Jawaban dimulai dengan huruf '{a[0].upper()}'")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Update progress bar
    progress_percentage = answered_questions / len(qna)
    progress_bar.progress(progress_percentage)
    
    # Display score if all questions answered
    if answered_questions == len(qna):
        st.markdown("---")
        
        # Score display with enhanced styling
        percentage = (score / len(qna)) * 100
        st.markdown(f"""
        <div class="score-display">
            <h2>🎯 Hasil Quiz Anda</h2>
            <h1>{score}/{len(qna)} ({percentage:.0f}%)</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # Performance feedback with animations
        if score == len(qna):
            st.balloons()
            st.markdown("""
            <div style="background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%); 
                        padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0;">
                <h2>🏆 PERFECT SCORE! 🏆</h2>
                <h3>Kamu pintar banget! dan Kamu cocok jadi Master AI!!!</h3>
            </div>
            """, unsafe_allow_html=True)
            st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2pkN2Q1Z2Vmdm05a2g3MDd6YWxpZ3I5ZzliZ2JheWEwaDJ1MnU4bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/X9izlczKyCpmCSZu0l/giphy.gif", 
                     caption="Congratulations! 🎉")
        
        elif score >= len(qna) * 0.8:  # 80% or more
            st.markdown("""
            <div style="background: linear-gradient(135deg, #a8e6cf 0%, #88d8a3 100%); 
                        padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0;">
                <h2>🌟 GREAT JOB! 🌟</h2>
                <h3>Kamu hampir sempurna! Terus belajar ya!</h3>
            </div>
            """, unsafe_allow_html=True)
            st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHlzc3g5ZnBpMWp5bWIxZjR3bWtkcjNkeTVoZDE4ZWVrNWptdWlpayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CaiVJuZGvR8HK/giphy.gif",
                     caption="Keep it up! 💪")
        
        elif score >= len(qna) * 0.6:  # 60% or more
            st.markdown("""
            <div style="background: linear-gradient(135deg, #ffd89b 0%, #19547b 100%); 
                        padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0; color: white;">
                <h2>👍 GOOD EFFORT! 👍</h2>
                <h3>Lumayan bagus! Ayo belajar lagi untuk hasil yang lebih baik!</h3>
            </div>
            """, unsafe_allow_html=True)
            st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHlzc3g5ZnBpMWp5bWIxZjR3bWtkcjNkeTVoZDE4ZWVrNWptdWlpayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CaiVJuZGvR8HK/giphy.gif",
                     caption="You can do it! 🎯")
        
        else:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); 
                        padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0;">
                <h2>💪 JANGAN MENYERAH! 💪</h2>
                <h3>Ayo semangat, kamu pasti bisa lebih baik!</h3>
            </div>
            """, unsafe_allow_html=True)
            st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHlzc3g5ZnBpMWp5bWIxZjR3bWtkcjNkeTVoZDE4ZWVrNWptdWlpayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CaiVJuZGvR8HK/giphy.gif",
                     caption="Never give up! 🚀")
        
        # Fun facts section
        st.markdown("---")
        st.markdown("### 🔍 **Fun Facts tentang AI:**")
        
        facts = [
            "🤖 AI pertama kali diperkenalkan pada tahun 1956 di Dartmouth Conference",
            "🧠 Deep Learning terinspirasi dari cara kerja otak manusia",
            "👁️ Computer Vision memungkinkan komputer 'melihat' seperti manusia",
            "💬 NLP membantu komputer memahami bahasa manusia",
            "📱 AI sekarang ada di smartphone, mobil, dan perangkat rumah pintar kita!"
        ]
        
        for fact in facts:
            st.markdown(f"• {fact}")
        
        # Retry button
        if st.button("🔄 Ulangi Quiz", type="primary"):
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("👆 Silakan masukkan nama Anda untuk memulai quiz!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            border-radius: 15px; color: white; margin: 20px 0;">
    <h2>🙏 Terima kasih telah berpartisipasi! 👍🏻</h2>
    <p>Semoga quiz ini bermanfaat untuk pembelajaran AI Anda!</p>
    <p><em>Created with ❤️ using Streamlit</em></p>
</div>
""", unsafe_allow_html=True)