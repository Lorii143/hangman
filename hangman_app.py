import streamlit as st
import random

st.title("🎯 Hangman Game")

# Word list
words = ["python", "streamlit", "notebook", "sudoku", "hangman", "developer", "science", "statistics", "function", "variable", "array", "matrix", "pandas", "numpy", "visualization", "machine", "learning",
         "artificial", "trials", "errors", "testing"]

# Hangman stages (ASCII art drawings)
stages = [
     """
       ------
       |    
       |   
       |    
       |    
       |    
    ---------
    """,
     """
       ------
       |    |
       |    
       |    
       |    
       |    
    ---------
    """,
     """
       ------
       |    |
       |    🙂
       |    
       |    
       |    
    ---------
    """,
   """
       ------
       |    |
       |    😕
       |    |
       |    |
       |    
    ---------
    """,
     """
       ------
       |    |
       |    😟
       |   /|
       |    |
       |    
    ---------
    """,
     """
       ------
       |    |
       |    😧
       |   /|\\
       |    |
       |    
    ---------
    """,
    """
       ------
       |    |
       |    😨
       |   /|\\
       |    |
       |   / 
    ---------
    """,

    """
       ------
       |    |
       |    😵
       |   /|\\
       |    |
       |   / \\
    ---------
    """,
    
   
   
   
]

if "word" not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed = set()
    st.session_state.lives = 8


display_word = "".join([letter if letter in st.session_state.guessed else "_" for letter in st.session_state.word])
st.subheader("Word: " + " ".join(display_word))


st.text(stages[8 - st.session_state.lives])

# Guess input
guess = st.text_input("Enter a letter:", max_chars=1)

if st.button("Submit Guess"):
    if guess:
        guess = guess.lower()
        if guess in st.session_state.word:
            if guess in st.session_state.guessed:
                st.warning(f"⚠️ You already guessed '{guess}'")
            else:
                st.success(f"✅ Correct! '{guess}' is in the word.")
                st.session_state.guessed.add(guess)
        else:
            st.error(f"❌ Wrong! '{guess}' is not in the word.")
            st.session_state.lives -= 1

# Display lives left
st.write(f"❤️ Lives left: {st.session_state.lives}")

# Check for win/lose
if all(letter in st.session_state.guessed for letter in st.session_state.word):
    st.success(f"🥳 You won! The word was '{st.session_state.word}'.")
    if st.button("Play Again"):
        st.session_state.word = random.choice(words)
        st.session_state.guessed = set()
        st.session_state.lives = 8

elif st.session_state.lives <= 0:
    st.error(f"💀 You lost! The word was '{st.session_state.word}'.")
    if st.button("Play Again"):
        st.session_state.word = random.choice(words)
        st.session_state.guessed = set()
        st.session_state.lives = 8
