import streamlit as st
import pandas as pd

# 1. SETUP MEMORY (Fixes the AttributeError)
if 'auth' not in st.session_state:
    st.session_state.auth = False

# 2. THE GATEKEEPER (The Login Screen)
if not st.session_state.auth:
    st.title("🛡️ Poke-Discord Entrance")
    st.write("Joshua's Private League. Enter your Master Key.")
    
    key_input = st.text_input("Access Key", type="password")
    
    if st.button("Connect"):
        # This is your secret backdoor!
        if key_input == "JOSHUA_MASTER_99":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Invalid Key. Message Joshua on WhatsApp.")
    st.stop()

# 3. THE MAIN APP (Only shows after you log in)
st.sidebar.title("🎮 POKE-DISCORD")
channel = st.sidebar.radio("Channels", ["🏆-leaderboard", "📖-pokedex", "🧠-strategy-guide"])

if channel == "🏆-leaderboard":
    st.title("🏆 Hall of Fame")
    st.write("Current Standings:")
    # Sample data - we can connect this to your Google Sheet later!
    df = pd.DataFrame({"Trainer": ["Joshua", "Archie"], "Wins": [10, 8]})
    st.table(df)

elif channel == "📖-pokedex":
    st.title("📖 Group Pokédex")
    pkmn = st.text_input("Search Pokémon Name").lower()
    if pkmn:
        st.image(f"https://img.pokemondb.net/sprites/home/normal/{pkmn}.png")

elif channel == "🧠-strategy-guide":
    st.title("🧠 Battle Intel")
    st.info("Tip: Joshua's Garchomp is weak to Ice!")

