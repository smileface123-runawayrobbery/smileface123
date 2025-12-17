import streamlit as st
import random
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(page_title="Global Happiness Engine", page_icon="🌍")

# --- Databases ---
GLOBAL_WISDOM = [
    "Happiness is not something readymade. It comes from your own actions. — Dalai Lama",
    "The most beautiful way to start the day is with a grateful heart.",
    "A surprise is the greatest gift which life can grant us. — Boris Pasternak",
    "Spread love everywhere you go. Let no one ever come to you without leaving happier. — Mother Teresa",
    "The secret of happiness is not in doing what one likes, but in liking what one does. — James M. Barrie"
]

MUSIC_MOODS = {
    "Energetic": ["'Don't Stop Me Now' by Queen", "Upbeat Jazz Fusion", "High-tempo Samba"],
    "Relaxed": ["'Weightless' by Marconi Union", "Lo-fi Hip Hop Beats", "Nature Sounds & Piano"],
    "Inspired": ["'Ode to Joy' by Beethoven", "Epic Cinematic Orchestral", "Soulful Gospel Highlights"]
}

# --- Sidebar: User Info ---
st.sidebar.header("👤 Your Profile")
user_name = st.sidebar.text_input("What is your name?", "Guest")
interest = st.sidebar.selectbox("What brings you joy?", ["Astronomy", "Gardening", "Coding", "Music", "General"])

# --- Main Website UI ---
st.title("🌍 Global Happiness & Surprise Engine")
st.write(f"Welcome, **{user_name}**! This system is designed to spread positivity across the world.")

# 1. Wisdom Section
if st.button("✨ Get Daily Wisdom"):
    st.info(random.choice(GLOBAL_WISDOM))

# 2. Wellbeing Simulation
st.divider()
st.subheader("📊 Global Wellbeing Status")
if st.button("Run Global Analysis"):
    col1, col2, col3 = st.columns(3)
    # Simulate some data
    hunger = random.randint(70, 95)
    edu = random.randint(60, 85)
    mental = random.randint(80, 99)
    
    col1.metric("Hunger Alleviation", f"{hunger}%", "+2%")
    col2.metric("Education Access", f"{edu}%", "+5%")
    col3.metric("Mental Health Index", f"{mental}%", "+1%")
    st.success("Global resources are being optimized for maximum happiness!")

# 3. The Big Surprise
st.divider()
st.subheader("🎁 Your Personalized Surprise")
if st.button("Surprise Me!"):
    st.balloons() # This adds a fun animation!
    st.snow()     # Why not both? 
    
    if interest == "Astronomy":
        res = "We've reserved a telescope slot for you to view the rings of Saturn tonight!"
    elif interest == "Gardening":
        res = "A digital seed packet for 'Rainbow Roses' has been sent to your email."
    elif interest == "Coding":
        res = "You've been granted access to a secret developer community for social good."
    else:
        res = "A stranger in another part of the world just received a digital flower because of you!"
    
    st.header(res)

# 4. Music Recommendation
st.divider()
mood = st.selectbox("How are you feeling?", list(MUSIC_MOODS.keys()))
if st.button("Suggest a Song"):
    song = random.choice(MUSIC_MOODS[mood])
    st.write(f"🎵 You should listen to: **{song}**")

# Footer
st.caption(f"Engine Last Synced: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")