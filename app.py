import streamlit as st
import pandas as pd
# --- JOSHUA'S ADMIN PANEL (Only you see this) ---
if st.sidebar.checkbox("Admin Login"):
    admin_pass = st.sidebar.text_input("Master Password", type="password")
    if admin_pass == "YOUR_SECRET_BOSS_CODE":
        st.title("👨‍💻 Joshua's Control Panel")
        
        # 1. Generate a Code
        target_email = st.text_input("Enter Friend's Email")
        if st.button("Generate & Email Key"):
            new_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            
            # Send the email (using the email code I gave you before)
            send_access_email(target_email, new_key)
            
            # SAVE TO GOOGLE SHEET (Crucial step!)
            # conn.write_to_sheet(target_email, new_key) 
            st.success(f"Key {new_key} sent to {target_email}!")
            import streamlit as st
import pandas as pd
import random
import string
import smtplib
from email.message import EmailMessage

# --- SENDER CONFIG (Use your App Password here) ---
EMAIL_ADDRESS = "your-league-email@gmail.com"
EMAIL_PASSWORD = "your-16-char-app-password"

# --- HELPER FUNCTIONS ---
def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def send_access_email(receiver_email, code):
    msg = EmailMessage()
    msg['Subject'] = "Your Pokémon League Access Key 🗝️"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = receiver_email
    msg.set_content(f"Welcome to the League! Your 6-character access key is: {code}")
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# --- LOGIN LOGIC ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# AUTO-LOGIN FOR YOU (JOSHUA)
# Streamlit can check your specific URL parameters or you can just use a "Master Key"
if not st.session_state.authenticated:
    st.title("🛡️ Pokémon League Gatekeeper")
    
    tab1, tab2 = st.tabs(["Login", "Request Access"])
    
    with tab1:
        user_key = st.text_input("Enter your 6-character key", type="password")
        if st.button("Enter League"):
            # Master key for Joshua, or check against a list
            if user_key == "JOSHUA_BOSS_99" or user_key in st.sidebar.get("generated_keys", []):
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid key.")

    with tab2:
        st.write("New here? Enter your email and Joshua will approve your code.")
        new_email = st.text_input("Your Email Address")
        if st.button("Request Key"):
            new_code = generate_code()
            try:
                send_access_email(new_email, new_code)
                st.success(f"Key sent to {new_email}! Check your inbox.")
                # Note: In a real app, you'd save 'new_code' to a database/Google Sheet here
            except Exception as e:
                st.error("Failed to send email. Check your Gmail App Password settings.")
    st.stop()

# --- THE ACTUAL APP STARTS HERE ---
st.title("🏆 Welcome to the League, Joshua!")
import streamlit as st

# --- USER ACCESS KEYS ---
# You can change these to any random strings/numbers you want
access_keys = {
    "Joshua": "J882",
    "Archie": "A192",
    "Harry": "H773",
    "Leo": "L004",
    "Stanley": "S551"
}

# --- THE LOGIN SCREEN ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🛡️ The Boys Pokémon League")
    st.write("This site is private. Please enter your Access Key to enter.")
    
    user_input = st.text_input("Access Key", type="password")
    
    if st.button("Unlock App"):
        if user_input in access_keys.values():
            st.session_state.authenticated = True
            st.success("Access Granted! Welcome to the League.")
            st.rerun() # Refresh the page to show the app
        else:
            st.error("Invalid Key. Message Joshua on WhatsApp to get yours.")
    st.stop() # Stops the rest of the app from loading until they log in

# --- EVERYTHING BELOW THIS ONLY SHOWS AFTER LOGIN ---
st.sidebar.title(f"Welcome back!")
# ... (Rest of your Leaderboard, Strategy Guide, and Pokedex code goes here)import streamlit as st
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
