import streamlit as st
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Smart Career Navigator", page_icon="🚀")

# ---------------- DARK + BOLD CSS ---------------- #
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}

/* HEADINGS */
h1 {
    color: #ffffff !important;
    font-weight: 800 !important;
    font-size: 40px !important;
}

h2, h3 {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* TEXT */
p, label {
    color: #f1f1f1 !important;
    font-size: 16px;
    font-weight: 500;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #1a1d24;
}

/* BUTTONS */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 8px;
}

/* INPUT */
.stTextInput input {
    background-color: #2c2f36;
    color: white;
    border-radius: 8px;
}

/* FORCE TEXT VISIBILITY */
.stMarkdown, .stText {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.title("🚀 Smart Career Navigator")
st.markdown("### Student Engagement & Career Support Platform")
st.divider()

# ---------------- SIDEBAR ---------------- #
menu = ["Home", "Events", "Clubs", "Profile", "Dashboard"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- HOME ---------------- #
if choice == "Home":
    st.subheader("🏠 Welcome")

    st.write("""
    Smart Career Navigator helps students:
    - 📅 Discover events  
    - 🎯 Join clubs  
    - 📊 Track participation  
    - 🚀 Stay engaged  
    """)

# ---------------- EVENTS ---------------- #
elif choice == "Events":
    st.subheader("📅 Upcoming Events")

    events = [
        {"name": "Hackathon 2026", "date": "10 April"},
        {"name": "AI Workshop", "date": "15 April"},
        {"name": "Tech Seminar", "date": "20 April"}
    ]

    for i, event in enumerate(events):
        st.markdown(f"### {event['name']}")
        st.info(f"📅 Date: {event['date']}")

        if st.button("Join Event", key=f"event_{i}"):
            st.success(f"You joined {event['name']}!")

# ---------------- CLUBS ---------------- #
elif choice == "Clubs":
    st.subheader("🎯 College Clubs")

    clubs = ["Coding Club", "AI Club", "Design Club", "Robotics Club"]

    for i, club in enumerate(clubs):
        st.markdown(f"### {club}")

        if st.button("Join Club", key=f"club_{i}"):
            st.success(f"You joined {club}!")

# ---------------- PROFILE ---------------- #
elif choice == "Profile":
    st.subheader("👤 Student Profile")

    name = st.text_input("Enter your name")
    branch = st.text_input("Branch")
    interests = st.text_input("Interests")

    if st.button("Save Profile"):
        st.success("Profile saved successfully!")

# ---------------- DASHBOARD ---------------- #
elif choice == "Dashboard":
    st.subheader("📊 Campus Insights Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Students", 120)
    col2.metric("Events", 15)
    col3.metric("Clubs", 6)

    categories = ["Students", "Events", "Clubs"]
    values = [120, 15, 6]

    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_title("Campus Overview")
    st.pyplot(fig)

    st.write("### 📌 Participation Overview")
    fig2, ax2 = plt.subplots()
    ax2.pie(values, labels=categories, autopct='%1.1f%%')
    st.pyplot(fig2)

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.markdown("Made by Shruti Verma 🚀")
