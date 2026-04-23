import streamlit as st
from summarizer import summarize_text
from PyPDF2 import PdfReader

# ---------------- LOGIN SYSTEM ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align:center;'>🔐 AI Summarizer Login</h2>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "Rimanshu" and password == "7804":
            st.session_state.logged_in = True
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

    st.stop()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Summarizer", layout="wide")

# ---------------- THEME ----------------
theme = st.sidebar.selectbox("🎨 Theme", ["Light", "Dark"])

if theme == "Dark":
    bg = "#0f172a"
    text_color = "white"
else:
    bg = "#F1EDEC"
    text_color = "#111"

st.markdown(f"""
<style>
.stApp {{
    background: {bg};
    color: {text_color};
}}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Settings")

summary_length = st.sidebar.slider("Summary Length", 20, 100, 40)

menu = st.sidebar.radio("📂 Navigation", ["Home", "About"])

# ---------------- HOME ----------------
if menu == "Home":

    st.title("🧠 AI Text Summarizer")
    st.caption("Transform long content into meaningful insights 🚀")

    # FILE UPLOAD
    uploaded_file = st.file_uploader("📂 Upload TXT or PDF", type=["txt", "pdf"])

    # TEXT INPUT
    text = st.text_area("✍️ Enter your text")

    # WARNING (no stop here)
    if len(text) > 1000:
        st.warning("Text too long! Max 1000 characters allowed.")

    # BUTTON
    if st.button("✨ Summarize"):

        final_text = ""

        if uploaded_file is not None:
            if uploaded_file.type == "application/pdf":
                reader = PdfReader(uploaded_file)
                for page in reader.pages:
                    final_text += page.extract_text()
            else:
                final_text = uploaded_file.read().decode("utf-8")

        elif text:
            final_text = text

        else:
            st.warning("Enter text or upload file")
            st.stop()

        if len(final_text) > 2000:
            final_text = final_text[:2000]

        # 🔥 ANIMATION
        with st.spinner("Generating summary... ⏳"):
            summary = summarize_text(final_text, max_len=summary_length // 20)

        st.success("Summary generated ✅")

        st.subheader("📄 Summary")
        st.write(summary)

        # 🔥 DOWNLOAD
        st.download_button(
            "📥 Download Summary",
            summary,
            file_name="summary.txt"
        )

        st.balloons()

# ---------------- ABOUT ----------------
elif menu == "About":

    st.title("📌 About Project")

    st.write("""
    🚀 AI Text Summarizer using Python

    Features:
    - 📄 Text summarization  
    - 📂 File upload (TXT/PDF)  
    - 🎨 Light/Dark theme  
    - ⚡ Fast processing  
    - 📥 Download summary  
    - 🔐 Login system  

    Designed for students & productivity 💡
    """)
st.markdown("Made with ❤️ using BART Transformer")
