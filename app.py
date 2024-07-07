import streamlit as st
import random

# Function to generate random poetry with English and Hindi translations
def generate_random_poetry():
    # Your existing code for generating poetry
    pass

# Streamlit app UI
def main():
    st.title("Random Poetry Generator (Not by Gulzar)")
    st.subheader("Generate poetry inspired by a poetic formula!")

    # Apply dark mode styles
    st.markdown(
        """
        <style>
        body {
            background-color: #000000; /* Black background color */
            color: white; /* Text color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Button to generate poem
    if st.button("Generate Poetry"):
        poem_en, poem_hi = generate_random_poetry()
        st.markdown(f"### English:\n```\n{poem_en}\n```")
        st.markdown(f"### Hindi Translation:\n```\n{poem_hi}\n```")

    # Footer with heart emoji
    st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add some space for the footer
    st.markdown("Made by Anurag ❤️", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
