import streamlit as st
import pandas as pd

# --- APP CONFIG ---
st.set_page_config(page_title="The Boys League", page_icon="⚔️")

# --- NAVIGATION ---
page = st.sidebar.radio("Go To:", ["🏆 Leaderboard", "📚 Strategy Guide", "📖 Pokedex", "💬 Message Board", "📅 Calendar"])

# --- 1. LEADERBOARD ---
if page == "🏆 Leaderboard":
    st.title("The Official Standings")
    st.write("Joshua is currently at the top! (Example)")
    # (Put your leaderboard table code here)

# --- 2. STRATEGY GUIDE ---
elif page == "📚 Strategy Guide":
    st.title("Battle Strategies")
    st.info("Tip: Use Ice-type moves against Joshua's Garchomp!")
    st.markdown("""
    * **Archie's Weakness:** His team is weak to Stealth Rock.
    * **The Meta:** Everyone is using Lucario lately—bring a Ghost-type.
    """)

# --- 3. POKEDEX ---
elif page == "📖 Pokedex":
    st.title("Group Pokédex")
    pkmn_search = st.text_input("Search for a Pokémon")
    if pkmn_search:
        st.write(f"Displaying info for {pkmn_search}...")
        st.image(f"https://img.pokemondb.net/sprites/home/normal/{pkmn_search.lower()}.png")

# --- 4. MESSAGE BOARD ---
elif page == "💬 Message Board":
    st.title("The Trash Talk Board")
    with st.form("msg_form"):
        user = st.selectbox("Who are you?", ["Joshua", "Archie", "Harry", "Leo", "Stanley"])
        msg = st.text_area("Your Message")
        if st.form_submit_button("Post"):
            st.success(f"Message Posted: {msg}")

# --- 5. CALENDAR ---
elif page == "📅 Calendar":
    st.title("Upcoming Battles")
    st.write("🗓️ **Saturday Night:** Grand Tournament @ 8 PM")
    st.write("🗓️ **Wednesday:** Harry vs. Leo - Gym Match")
