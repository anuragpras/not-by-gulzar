import streamlit as st
import random

# Lists of words for each category (English and Hindi)
oscillations = {
    "English": ["Thiraktey", "Simat-tey", "Jhulastey", "Laharatey", "Khanaktey"],
    "Hindi": ["थिरकते", "सिमट-ते", "झुलसते", "लहराते", "खनकते"]
}

facial_features = {
    "English": ["Nazron", "Hothon", "Nainon", "Gaalon", "Maathey"],
    "Hindi": ["नजरों", "होठों", "नैनों", "गालों", "माथे"]
}

natural_phenomena = {
    "English": ["Boond", "Oas", "Baarish", "Hawa"],
    "Hindi": ["बूंद", "ओस", "बारिश", "हवा"]
}

bathroom_activities = {
    "English": ["Phisalna", "Girna", "Tapakna", "Ulajhna", "Sulajhna", "Nikalna", "Sawarna"],
    "Hindi": ["फिसलना", "गिरना", "टपकना", "उलझना", "सुलझना", "निकलना", "सवारना"]
}

random_emotions = {
    "English": ["Yaad", "Darata", "Hasata", "Rulata"],
    "Hindi": ["याद", "डराता", "हँसाता", "रुलाता"]
}

ufo_movements = {
    "English": ["Duur jaana", "Paas aana", "Roshni phailana", "Gumm ho jaana"],
    "Hindi": ["दूर जाना", "पास आना", "रोशनी फैलाना", "गुम हो जाना"]
}

# Function to generate random poetry with English and Hindi translations
def generate_random_poetry():
    # Select random words from each category
    oscillation_en = random.choice(oscillations["English"])
    oscillation_hi = oscillations["Hindi"][oscillations["English"].index(oscillation_en)]

    facial_feature_en = random.choice(facial_features["English"])
    facial_feature_hi = facial_features["Hindi"][facial_features["English"].index(facial_feature_en)]

    natural_phenomenon_en = random.choice(natural_phenomena["English"])
    natural_phenomenon_hi = natural_phenomena["Hindi"][natural_phenomena["English"].index(natural_phenomenon_en)]

    bathroom_activity_en = random.choice(bathroom_activities["English"])
    bathroom_activity_hi = bathroom_activities["Hindi"][bathroom_activities["English"].index(bathroom_activity_en)]

    random_emotion_en = random.choice(random_emotions["English"])
    random_emotion_hi = random_emotions["Hindi"][random_emotions["English"].index(random_emotion_en)]

    ufo_movement_en = random.choice(ufo_movements["English"])
    ufo_movement_hi = ufo_movements["Hindi"][ufo_movements["English"].index(ufo_movement_en)]
    
    # Create the poem in English
    poem_en = f"{oscillation_en} hue {facial_feature_en} se {natural_phenomenon_en} ka {bathroom_activity_en}.\n"
    poem_en += f"{random_emotion_en} hai mujhe tera wahi {ufo_movement_en}."

    # Create the poem in Hindi
    poem_hi = f"{oscillation_hi} हुए {facial_feature_hi} से {natural_phenomenon_hi} का {bathroom_activity_hi}।\n"
    poem_hi += f"मुझे तेरा वही {ufo_movement_hi} है।"
    
    return poem_en, poem_hi

# Streamlit app UI
def main():
    st.title("Virtual Gulzar")
    st.subheader("Generate poetry inspired by a poetic formula!")
    
    # Add CSS for dark background color
    st.markdown(
        """
        <style>
        body {
            background-color: #1a1a1a; /* Dark background color */
            color: white; /* Text color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Button to generate poem
    if st.button("Generate Poetry"):
        poem_en, poem_hi = generate_random_poetry()
        st.markdown(f"### English :\n```\n{poem_en}\n```")
        st.markdown(f"### Hindi :\n```\n{poem_hi}\n```")
        
    # Footer with heart emoji
    st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add some space for the footer
    st.markdown("Made by Anurag ❤️", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
