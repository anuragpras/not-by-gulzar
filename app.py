import streamlit as st
import random

# Define lists of words for generating poetry
oscillations = ["Thiraktey", "Simat-tey", "Jhulastey", "Duur jaana", "Paas aana", "Roshni phailana", "Gumm ho jaana"]
facial_features = ["Nazron", "Hothon", "Nainon", "Gaalon", "Maathey"]
natural_phenomena = ["Boond Oas", "Baarish", "Hawa"]
bathroom_activities = ["Phisalna", "Girna", "Tapakna", "Ulajhna", "Sulajhna", "Nikalna", "Sawarna"]
emotions = ["Yaad", "Darata", "Hasata", "Rulata"]
ufo_movements = ["Duur jaana", "Paas aana", "Roshni phailana", "Gumm ho jaana"]

# Function to generate random poetry with English and Hindi translations
def generate_poetry():
    line1_en = f"{random.choice(oscillations)} hue {random.choice(facial_features)} se {random.choice(natural_phenomena)} ka {random.choice(bathroom_activities)}."
    line1_hi = f"{random.choice(oscillations)} हुए {random.choice(facial_features)} से {random.choice(natural_phenomena)} का {random.choice(bathroom_activities)}।"

    line2_en = f"{random.choice(emotions)} hai mujhe tera wahi {random.choice(ufo_movements)}"
    line2_hi = f"{random.choice(emotions)} है मुझे तेरा वही {random.choice(ufo_movements)}"

    return (line1_en, line1_hi), (line2_en, line2_hi)

# Streamlit app UI
def main():
    st.title("Gulzar-Inspired Poetry Generator)")
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
        (poem1_en, poem1_hi), (poem2_en, poem2_hi) = generate_poetry()
        st.markdown(f"### English:\n```\n{poem1_en}\n{poem2_en}\n```")
        st.markdown(f"### Hindi Translation:\n```\n{poem1_hi}\n{poem2_hi}\n```")

    # Footer with heart emoji
    st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add some space for the footer
    st.markdown("Made by Anurag ❤️", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
