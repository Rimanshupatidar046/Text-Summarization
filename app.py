import streamlit as st
from summarizer import summarize_text
from PyPDF2 import PdfReader

# ---------------- SESSION INIT ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }
    .login-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 15px;
        width: 350px;
        margin: auto;
        margin-top: 120px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        text-align: center;
    }
    .login-title {
        font-size: 28px;
        color: white;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">🔐 AI Summarizer Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        if username.strip() == "Rimanshu" and password.strip() == "7804":
            st.session_state.logged_in = True
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

# ---------------- MAIN APP ----------------
st.set_page_config(page_title="AI Summarizer", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Settings")

summary_length = st.sidebar.slider(
    "Summary Length", 20, 100, 40, key="summary_slider"
)

language = st.sidebar.selectbox(
    "Language", ["English", "Hindi"], key="language_select"
)

menu = st.sidebar.radio(
    "📂 Navigation", ["Home", "About"], key="menu_nav"
)

# ---------------- HOME ----------------
if menu == "Home":

    st.title("🧠 AI Text Summarizer")
    st.caption("Transform long content into meaningful insights 🚀")

    # FILE UPLOAD (ONLY ONE)
    uploaded_file = st.file_uploader(
        "📂 Upload TXT or PDF",
        type=["txt", "pdf"],
        key="main_file_upload"
    )

    input_text = ""

    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                input_text += page.extract_text()
        else:
            input_text = uploaded_file.read().decode("utf-8")

   # ---------------- TEXT INPUT ----------------
st.subheader("✍️ Or Enter Text Manually")

text = st.text_area("Enter your text here:")

# 👇 YAHI ADD KIYA (important)
if len(text) > 1000:
    st.warning("Text too long! Max 1000 characters allowed.")

    # BUTTON
    if st.button("✨ Summarize", key="summarize_btn"):

        if user_input.strip():

            with st.spinner("Generating summary..."):
                summary = summarize_text(user_input)

            words = summary.split()
            summary = " ".join(words[:summary_length])

            st.success("✅ Summary Generated")
            st.subheader("📄 Summary")
            st.write(summary)

            # DOWNLOAD
            st.download_button(
                "📥 Download Summary",
                summary,
                file_name="summary.txt",
                key="download_btn"
            )

            st.balloons()

        else:
            st.warning("⚠️ Enter text first")

# ---------------- ABOUT ----------------
elif menu == "About":

    st.title("📌 About Project")

    st.markdown("""
### 🚀 AI Text Summarizer

This project uses **NLP & BART Transformer** to convert long text into short summaries.

### ✨ Features
- 📄 Text Summarization  
- 📂 File Upload (TXT, PDF)  
- 🌐 Multi-language Support  
- ⚡ Fast Processing  
- 📥 Download Summary  

### 💡 Use Cases
- Students notes summary  
- Article summarization  
- Research papers  
""")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("Made with ❤️ using BART Transformer")
