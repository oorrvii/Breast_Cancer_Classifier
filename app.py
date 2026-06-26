import streamlit as st
import pickle
import numpy as np

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Tumor Classifier",
    page_icon="🎗️",
    layout="centered"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=DM+Serif+Display&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #0f1117;
    color: #e8eaf0;
}

.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}

.hero-badge {
    display: inline-block;
    background: rgba(220, 80, 100, 0.15);
    border: 1px solid rgba(220, 80, 100, 0.4);
    color: #f28b9a;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 0.3rem 0.9rem;
    border-radius: 20px;
    margin-bottom: 1rem;
}

.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2.6rem;
    font-weight: 400;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 0.6rem;
}

.hero-subtitle {
    color: #8b90a0;
    font-size: 0.95rem;
    font-weight: 400;
    max-width: 480px;
    margin: 0 auto 0.5rem;
    line-height: 1.6;
}

.divider {
    border: none;
    border-top: 1px solid #1e2130;
    margin: 1.5rem 0;
}

.section-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #555a70;
    margin-bottom: 1.2rem;
    margin-top: 1.5rem;
}

.result-box-malignant {
    background: linear-gradient(135deg, rgba(200, 40, 60, 0.18), rgba(200, 40, 60, 0.05));
    border: 1px solid rgba(200, 40, 60, 0.45);
    border-radius: 12px;
    padding: 1.6rem 2rem;
    text-align: center;
    margin-top: 1rem;
}

.result-box-benign {
    background: linear-gradient(135deg, rgba(40, 180, 120, 0.18), rgba(40, 180, 120, 0.05));
    border: 1px solid rgba(40, 180, 120, 0.45);
    border-radius: 12px;
    padding: 1.6rem 2rem;
    text-align: center;
    margin-top: 1rem;
}

.result-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.result-label-mal { color: #f28b9a; }
.result-label-ben { color: #5ecfa0; }

.result-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.9rem;
    font-weight: 400;
    margin-bottom: 0.4rem;
}

.result-title-mal { color: #ff6b7a; }
.result-title-ben { color: #3ddba0; }

.result-desc {
    font-size: 0.85rem;
    color: #8b90a0;
    line-height: 1.5;
}

.stats-row {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
}

.stat-card {
    flex: 1;
    background: #161825;
    border: 1px solid #1e2130;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    text-align: center;
}

.stat-value {
    font-size: 1.5rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1;
    margin-bottom: 0.3rem;
}

.stat-label {
    font-size: 0.7rem;
    color: #555a70;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.accent { color: #f28b9a; }

.disclaimer {
    font-size: 0.72rem;
    color: #3a3f52;
    text-align: center;
    margin-top: 2rem;
    line-height: 1.6;
    padding: 0 1rem;
}

/* Slider overrides */
.stSlider > div > div > div > div {
    background: #dc5064 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    with open('classifier.pkl', 'rb') as f:
        return pickle.load(f)

try:
    model = load_model()
    model_loaded = True
except:
    model_loaded = False

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">🎗️ Breast Cancer Detection</div>
    <div class="hero-title">Tumor Classifier</div>
    <div class="hero-subtitle">
        Enter cytology findings from a Fine Needle Aspirate (FNA) to classify a breast tumor as benign or malignant.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Model stats ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
    <div class="stat-card">
        <div class="stat-value accent">96.70<span style="font-size:1rem">%</span></div>
        <div class="stat-label">Model Accuracy</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">±1.97<span style="font-size:1rem">%</span></div>
        <div class="stat-label">Std Deviation</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">10<span style="font-size:1rem">-fold</span></div>
        <div class="stat-label">Cross Validation</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">LR</div>
        <div class="stat-label">Algorithm</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Input features ────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Cytology Features</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    clump          = st.slider("Clump Thickness",              1, 10, 5)
    cell_size      = st.slider("Uniformity of Cell Size",      1, 10, 5)
    cell_shape     = st.slider("Uniformity of Cell Shape",     1, 10, 5)
    adhesion       = st.slider("Marginal Adhesion",            1, 10, 5)
    epithelial     = st.slider("Single Epithelial Cell Size",  1, 10, 5)

with col2:
    nuclei         = st.slider("Bare Nuclei",                  1, 10, 5)
    chromatin      = st.slider("Bland Chromatin",              1, 10, 5)
    nucleoli       = st.slider("Normal Nucleoli",              1, 10, 5)
    mitoses        = st.slider("Mitoses",                      1, 10, 1)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Predict ───────────────────────────────────────────────────────────────────
predict_btn = st.button("Run Classification →", use_container_width=True, type="primary")

if predict_btn:
    if not model_loaded:
        st.error("Model file not found. Make sure classifier.pkl is in the same folder.")
    else:
        features = np.array([[clump, cell_size, cell_shape,
                               adhesion, epithelial, nuclei,
                               chromatin, nucleoli, mitoses]])
        result = model.predict(features)

        if result[0] == 4:
            st.markdown("""
            <div class="result-box-malignant">
                <div class="result-label result-label-mal">Classification Result</div>
                <div class="result-title result-title-mal">Malignant</div>
                <div class="result-desc">
                    The model predicts this tumor is <strong>malignant</strong>. 
                    Please consult an oncologist for further evaluation and diagnosis.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-box-benign">
                <div class="result-label result-label-ben">Classification Result</div>
                <div class="result-title result-title-ben">Benign</div>
                <div class="result-desc">
                    The model predicts this tumor is <strong>benign</strong>. 
                    Regular monitoring is still recommended as a precaution.
                </div>
            </div>
            """, unsafe_allow_html=True)

# ── Disclaimer ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="disclaimer">
    ⚠️ This tool is built for educational purposes only and is not a substitute 
    for professional medical diagnosis. Always consult a qualified healthcare provider.
</div>
""", unsafe_allow_html=True)