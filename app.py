import streamlit as st
import random

# Lists of words for each category (English and Hindi)
osc = {
    "English": ["Thiraktey", "Simat-tey", "Jhulastey", "Laharatey", "Khanaktey"],
    "Hindi": ["थिरकते", "सिमट-ते", "झुलसते", "लहराते", "खनकते"]
}

facial = {
    "English": ["Nazron", "Hothon", "Nainon", "Gaalon", "Maathey"],
    "Hindi": ["नजरों", "होठों", "नैनों", "गालों", "माथे"]
}

nature = {
    "English": ["Boond", "Oas", "Baarish", "Hawa"],
    "Hindi": ["बूंद", "ओस", "बारिश", "हवा"]
}

bath = {
    "English": ["Phisalna", "Girna", "Tapakna", "Ulajhna", "Sulajhna", "Nikalna", "Sawarna"],
    "Hindi": ["फिसलना", "गिरना", "टपकना", "उलझना", "सुलझना", "निकलना", "सवारना"]
}

emotions = {
    "English": ["Yaad", "Darata", "Hasata", "Rulata"],
    "Hindi": ["याद", "डराता", "हँसाता", "रुलाता"]
}

ufo = {
    "English": ["Duur jaana", "Paas aana", "Roshni phailana", "Gumm ho jaana"],
    "Hindi": ["दूर जाना", "पास आना", "रोशनी फैलाना", "गुम हो जाना"]
}

# Function to generate random poetry with English and Hindi translations
def gen_poetry():
    osc_en = random.choice(osc["English"])
    osc_hi = osc["Hindi"][osc["English"].index(osc_en)]

    facial_en = random.choice(facial["English"])
    facial_hi = facial["Hindi"][facial["English"].index(facial_en)]

    nature_en = random.choice(nature["English"])
    nature_hi = nature["Hindi"][nature["English"].index(nature_en)]

    bath_en = random.choice(bath["English"])
    bath_hi = bath["Hindi"][bath["English"].index(bath_en)]

    emo_en = random.choice(emotions["English"])
    emo_hi = emotions["Hindi"][emotions["English"].index(emo_en)]

    ufo_en = random.choice(ufo["English"])
    ufo_hi = ufo["Hindi"][ufo["English"].index(ufo_en)]
    
    poem_en = f"{osc_en} hue {facial_en} se {nature_en} ka {bath_en}.\n"
    poem_en += f"{emo_en} hai mujhe tera wahi {ufo_en}."

    poem_hi = f"{osc_hi} हुए {facial_hi} से {nature_hi} का {bath_hi}।\n"
    poem_hi += f"मुझे तेरा वही {ufo_hi} है।"
    
    return poem_en, poem_hi

# Streamlit app UI
def main():
    st.title("Gulzar Inspired Poetry Generator")
    st.subheader("Generate poetry inspired by a poetic formula")

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
        poem_en, poem_hi = gen_poetry()
        st.markdown(f"### English:\n```\n{poem_en}\n```")
        st.markdown(f"### Hindi Translation:\n```\n{poem_hi}\n```")

    # Footer with heart emoji
    st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add some space for the footer
    st.markdown("Created by Anurag ❤️", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
