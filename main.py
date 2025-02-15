from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain import LLMChain
import streamlit as st
import os

# Set your Google API key using Streamlit secrets
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Streamlit App Title with Emojis and Colors
st.markdown(
    """
    <style>
    .title {
        font-size: 40px !important;
        color: #FF4B4B !important;
        text-align: center;
    }
    .subheader {
        font-size: 20px !important;
        color: #1F51FF !important;
        text-align: center;
    }
    .lyrics-output {
        background-color: #F0F2F6;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        white-space: pre-line; /* Preserve line breaks in lyrics */
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">🎵 Hindi Song Lyrics Generator - VK 🎵</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subheader">Create beautiful Hindi song lyrics with AI 🌟</p>',
    unsafe_allow_html=True
)

# Create prompt template for generating Hindi song lyrics
lyrics_template = """
Write {length} lines of Hindi song lyrics in the style of {artist} about {theme}. 
The mood of the song should be {mood}.
"""

lyrics_prompt = PromptTemplate(
    template=lyrics_template,
    input_variables=['length', 'artist', 'theme', 'mood']
)

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Create LLM chain using the prompt template and model
lyrics_chain = LLMChain(llm=gemini_model, prompt=lyrics_prompt)

# Streamlit UI
st.markdown("### 🎨 Customize Your Hindi Song Lyrics")
theme = st.text_input("Enter the theme of the song (e.g., pyaar, dosti, zindagi): 🌸")
mood = st.selectbox(
    "Choose the mood of the song: 🎭",
    ["Romantic", "Sad", "Happy", "Motivational", "Devotional"]
)
artist = st.selectbox(
    "Choose the artist's style: 🎤",
    ["Arijit Singh", "Kishore Kumar", "Lata Mangeshkar", "A.R. Rahman", "Custom"]
)
length = st.slider("Number of lines in the song: 📏", min_value=4, max_value=20, value=8, step=2)

if st.button("Generate Hindi Song Lyrics 🎶", key="generate_button"):
    if theme and mood and artist and length:
        # Invoke the chain to generate the Hindi song lyrics
        with st.spinner("Generating your Hindi song lyrics... 🎵"):
            hindi_lyrics = lyrics_chain.run({
                "length": length,
                "artist": artist,
                "theme": theme,
                "mood": mood
            })
        
        # Display the generated Hindi song lyrics with styling
        st.markdown("### 🎤 Your Generated Hindi Song Lyrics:")
        st.markdown(f'<div class="lyrics-output">{hindi_lyrics}</div>', unsafe_allow_html=True)
    else:
        st.error("❌ Please provide a theme, mood, artist, and length.")