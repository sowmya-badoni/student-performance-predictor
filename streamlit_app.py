import streamlit as st
import joblib
import base64

# Set page config
st.set_page_config(
    page_title="Vintage Student Predictor",
    page_icon="📜",
    layout="centered"
)

# Function to convert image to base64
def get_base64_image(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load image
bg_image = get_base64_image("vintage_bg.jpg")

# Inject CSS for background + layout
st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        font-family: 'Georgia', serif;
    }}

    .main {{
        background-color: rgba(255, 248, 220, 0.85);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        color: #3e2f1c;
    }}

    .stButton>button {{
        background-color: #7b4b3a;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }}
    .stButton>button:hover {{
        background-color: #5e3629;
        cursor: pointer;
    }}

    .prediction-box {{
        background-color: #f6eee3;
        border: 2px dashed #7b4b3a;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 1rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load the model
model = joblib.load("model.pkl")

# Main UI
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>📜 Student Performance Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict if a student will pass based on attendance, marks, and hours studied.</p>", unsafe_allow_html=True)
st.markdown("")

# Sliders in columns
col1, col2, col3 = st.columns(3)
with col1:
    hours = st.slider("🕒 Hours Studied", 0.0, 10.0, 3.0, 0.5)
with col2:
    attendance = st.slider("📅 Attendance (%)", 0, 100, 75, 5)
with col3:
    marks = st.slider("🧪 Internal Marks", 0, 100, 60, 5)

# Prediction
if st.button("🔮 Predict"):
    prediction = model.predict([[hours, attendance, marks]])
    result = "🎉 Pass" if prediction[0] == 1 else "❌ Fail"
    color = "green" if prediction[0] == 1 else "red"

    st.markdown(
        f"<div class='prediction-box'><h2 style='color:{color};'>Prediction: {result}</h2></div>",
        unsafe_allow_html=True
    )



st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:13px;'>Made with ❤️ by <b>Sowmya</b> in vintage mode 🕰️</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
