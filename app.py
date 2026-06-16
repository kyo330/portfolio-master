"""
Portfolio: Priyadharshini Ramesh Kumar
Data Scientist & Machine Learning Engineer

A single-file Streamlit portfolio. Edit the data blocks below (SOCIAL,
PROJECT_LINKS, EXPERIENCE, PROJECTS, SKILLS, EDUCATION, AWARDS) to update
content. The layout, styling, and rendering logic do not need to change.
"""

import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import pathlib

st.set_page_config(
    page_title="Priyadharshini Ramesh Kumar | Data Scientist & ML Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ════════════════════════════════════════════════════════════════════════
# 📄 RESUME PDF — resolved relative to app.py regardless of working dir
# ════════════════════════════════════════════════════════════════════════
_APP_DIR = pathlib.Path(__file__).parent
PDF_PATH = _APP_DIR / "assets" / "Priyadharshini_Ramesh_Kumar.pdf"
RESUME_URL = "?page=resume"   # all resume buttons point here

# ════════════════════════════════════════════════════════════════════════
# 🔗 EDIT ME: personal links, resume, and project URLs
# ════════════════════════════════════════════════════════════════════════
SOCIAL = {
    "email": "mailto:priyadarshini01.r@gmail.com",
    "email_display": "priyadarshini01.r@gmail.com",
    "phone": "+1 979 218 2333",
    "linkedin": "https://www.linkedin.com/in/priyadharshini-r330",
    "github": "https://github.com/kyo330",
    # Resume opens as an in-app tab (see ?page=resume routing below)
    "resume_pdf": RESUME_URL,
}

# TODO: replace these "#" placeholders with real GitHub repos / live demo
# URLs for each project. Set a value to None to hide that button entirely.
PROJECT_LINKS = {
    "energy": {"github": "#", "live": "#"},
    "depthforge": {"github": "#", "live": "#"},
    "multimodal": {"github": "#", "live": "#"},
    "customer_intel": {"github": "#", "live": "#"},
    "thunderstorm": {"github": "#", "live": "#"},
    "spotify_yt": {"github": "#", "live": "#"},
}

# ════════════════════════════════════════════════════════════════════════
# 📄 CONTENT DATA
# ════════════════════════════════════════════════════════════════════════
NAME = "Priyadharshini Ramesh Kumar"
ROLE = "Data Scientist & Machine Learning Engineer"
LOCATION = "Chennai, TN, India"

TAGLINE = (
    "I build systems that turn messy, real-world signals, like satellite lightning data, "
    "electricity markets, and a single RGB photo, into models and pipelines people can "
    "actually trust and act on."
)

ABOUT = """
I'm a data scientist with an M.S. in Data Science from <strong>Texas A&amp;M University</strong>
(GPA 3.91/4.00) and a B.E. in Computer Science &amp; Engineering from
<strong>Anna University, MIT Campus</strong>. My work sits at the intersection of
machine learning, geospatial analytics, and large-scale data engineering, spanning
clustering extreme lightning events in satellite data, building safety-critical
RAG pipelines for oil &amp; gas, and reconstructing 3D scenes from a single photo.
<br><br>
What pulls all of it together is a genuine curiosity about <em>how things work</em> and a
stubborn insistence that a model's output should be interpretable, reliable, and
genuinely useful to the person on the other end, whether that's an atmospheric
scientist, a marketing team, or a safety auditor. I'm happiest when I'm deep in a
notebook, a dashboard, or a half-broken pipeline at 11pm trying to figure out why
the numbers don't quite add up yet.
"""

CURRENTLY_EXPLORING = [
    "Agentic AI", "RAG at scale", "Geospatial ML", "3D scene understanding",
    "MLOps", "LLM evaluation", "Causal inference", "Edge deployment",
]

EXPERIENCE = [
    {
        "role": "AI Intern",
        "company": "OPX AI",
        "location": "Houston, TX",
        "dates": "Jan 2026 – Apr 2026",
        "bullets": [
            "Built a PDF ingestion pipeline for a safety-critical RAG system used in oil &amp; gas "
            "operations, turning technical and regulatory documents into structured, traceable "
            "chunks so every LLM response could be audited back to its source.",
            "Refactored the system into a clean, modular Python package (typed dataclasses, "
            "parallel UUID-based ingestion to prevent collisions, atomic writes, structured "
            "logging, and a full unit test suite) to meet the reliability bar required for "
            "regulated production environments.",
        ],
    },
    {
        "role": "Research Data Scientist",
        "company": "Texas A&amp;M University",
        "location": "College Station, TX",
        "dates": "Aug 2024 – Jan 2026",
        "bullets": [
            "Designed clustering pipelines (DBSCAN, hierarchical, sequential, and graph-based) "
            "to analyze large-scale GOES GLM satellite sensor data, sharpening how the team "
            "identified and characterized extreme lightning events.",
            "Built interactive geospatial dashboards in Python, Leaflet, and GeoPandas so "
            "researchers could explore lightning frequency, altitude, and spatial clusters "
            "visually, without needing to run scripts for routine exploration.",
            "Worked closely with atmospheric scientists to pressure-test assumptions and sharpen "
            "evaluation metrics, keeping the analysis focused on questions that genuinely "
            "mattered to the research.",
        ],
    },
    {
        "role": "Research Assistant",
        "company": "Texas A&amp;M University, SGL Lab",
        "location": "College Station, TX",
        "dates": "Feb 2024 – Apr 2024",
        "bullets": [
            "Conducted data discovery, cleaning, and preprocessing on global supply-chain "
            "datasets, including trade flow and commodity data, using Python, R, and SQL.",
            "Developed graph-based dependency models, including a 3-node semiconductor supply "
            "chain analysis, to study systemic risk propagation.",
            "Applied probabilistic and statistical modeling to evaluate uncertainty and "
            "variability across supply-chain systems, supporting reproducible research reporting.",
        ],
    },
    {
        "role": "Machine Learning Engineer",
        "company": "IIT Bombay",
        "location": "Mumbai, India",
        "dates": "Jan 2022 – Nov 2022",
        "bullets": [
            "Curated a labeled dataset of 26 Indian Sign Language gestures from video footage "
            "using Python and OpenCV, extracting per-frame features for reproducible training.",
            "Trained and systematically compared CNN architectures, including VGG16 with "
            "transfer learning, on accuracy, loss curves, and per-class metrics to select the "
            "best-performing sign language recognition model.",
            "Awarded the TIH-IoT CHANAKYA Fellowship for contributions to this AI-based sign "
            "language recognition research.",
        ],
    },
]

PROJECTS = [
    {
        "key": "energy",
        "title": "Spanish Energy Market Dashboard",
        "tags": ["Python", "Streamlit", "scikit-learn", "Plotly", "Groq API"],
        "description": (
            "A six-tab interactive dashboard analyzing four years of hourly Spanish "
            "electricity market data (~35K records), covering day-ahead prices, generation "
            "mix, and demand. Joined grid data with population-weighted city weather, modeled "
            "demand with heating/cooling degree days, and shipped a next-day demand "
            "forecast at roughly 6% MAPE. Built a day-ahead/spot trading signal engine "
            "backtested across ~7,000 trades, plus a live pipeline that turns scraped "
            "energy news into structured trading signals via an LLM."
        ),
    },
    {
        "key": "depthforge",
        "title": "DepthForge: Monocular 3D Reconstruction",
        "tags": ["PyTorch", "GLPN / DPT", "Open3D", "Hugging Face Spaces"],
        "description": (
            "A full depth-to-3D pipeline that takes a single RGB photo, runs it through a "
            "transformer depth model (GLPN-NYU or Intel DPT-Large), back-projects the depth "
            "map into a point cloud, and reconstructs a mesh via Poisson surface "
            "reconstruction. Added automated mesh-quality checks (manifold, watertight, "
            "surface area, volume) and a side-by-side GLPN vs. DPT comparison across indoor "
            "and outdoor scenes. Deployed on Hugging Face Spaces with a consent gate, EXIF "
            "privacy checks, and PLY/OBJ/STL export."
        ),
    },
    {
        "key": "multimodal",
        "title": "Multimodal Vision + Audio Digit Classifier",
        "tags": ["PyTorch", "CNN", "Optuna", "t-SNE"],
        "description": (
            "A dual-stream neural network from scratch, pairing a Conv2D encoder for "
            "handwritten digit images with a 1D CNN encoder for spoken digit audio, fused "
            "at the embedding level into a shared classification head, reaching 97.9% test "
            "accuracy and 97.8% macro F1 across 10 classes. Ran a joint Optuna "
            "hyperparameter search across both modalities, then used t-SNE + KMeans on the "
            "fused embeddings to confirm the fusion strategy genuinely improved class "
            "separation. Trained on a Tesla P100 with stratified splits and early stopping."
        ),
    },
    {
        "key": "customer_intel",
        "title": "Customer Intelligence Platform",
        "tags": ["Python", "Streamlit", "Plotly", "KMeans"],
        "description": (
            "A five-page interactive BI dashboard over a 2,000-customer dataset, giving "
            "non-technical business users a self-serve way to filter by age, income, and "
            "gender with live-updating visualizations. Used KMeans clustering on income, "
            "spending, and age to segment customers into four actionable personas: Premium "
            "Loyalists, Untapped High-Earners, Aspirational Spenders, and Budget Conscious, "
            "and translated each cluster into prioritized, plain-language marketing "
            "recommendations."
        ),
    },
    {
        "key": "thunderstorm",
        "title": "Visualizations of Thunderstorm: Capstone Project",
        "tags": ["Python", "Folium", "Geospatial Analytics"],
        "description": (
            "An interactive geospatial analytics system that converts large-scale lightning "
            "and thunderstorm datasets into dynamic, altitude-encoded map visualizations. "
            "Applied data filtering and aggregation to support exploratory analysis of "
            "extreme weather events, and built spatiotemporal tools to classify lightning "
            "strikes, turning static datasets into an interactive Folium map researchers "
            "can zoom and explore directly."
        ),
    },
    {
        "key": "spotify_yt",
        "title": "Spotify &amp; YouTube Cross-Platform Dashboard",
        "tags": ["Tableau", "Python", "Pandas", "Spotify API"],
        "description": (
            "An interactive Tableau dashboard analyzing 20,000+ tracks across 2,000+ artists, "
            "comparing Spotify streams against YouTube views, likes, and comments to surface "
            "cross-platform performance patterns. Engineered derived metrics, including "
            "engagement rate, stream-to-view ratio, and audio-feature tiering via LOD "
            "calculations, after cleaning the 20K-row dataset in Pandas, then extended the "
            "analysis with a GitHub Actions cron job pulling daily Spotify artist popularity "
            "data."
        ),
    },
]

EARLIER_PROJECTS = [
    {
        "title": "Air Pollutant Correlation: Uncovering Relationships",
        "dates": "Aug 2023 – Dec 2023",
        "description": (
            "Applied statistical modeling and feature engineering to identify correlations "
            "among environmental variables, and built ML models (R² = 0.87) to predict air "
            "quality levels from sensor data, while evaluating feature importance for "
            "interpretability."
        ),
    },
    {
        "title": "Revamping Hyperspectral Imagery via LAB Color Space Encryption",
        "dates": "Jan 2023 – Jun 2023",
        "description": (
            "Developed a Python-based color space encryption algorithm for hyperspectral "
            "data, achieving 97% security proximity while preserving data integrity, with "
            "PCA-based dimensionality reduction and Gaussian filtering for scalability."
        ),
    },
    {
        "title": "Secure Smart Cabin Using Arduino GSM Interface",
        "dates": "Jan 2022 – Apr 2022",
        "description": (
            "Designed a secure smart cabin with a team, improving environmental control "
            "efficiency by 30% and cutting energy use by 15% using GSM-based real-time "
            "monitoring. Published as \"Secure Smart Cabin Using Optimized Arduino GSM "
            "Interface\" in Springer."
        ),
    },
]

SKILLS = [
    {
        "icon": "🐍",
        "category": "Languages &amp; Frameworks",
        "items": ["Python", "R", "SQL", "Java", "C++", "PyTorch", "TensorFlow", "Keras",
                   "Scikit-learn", "NumPy", "Pandas"],
    },
    {
        "icon": "🧠",
        "category": "Machine Learning",
        "items": ["CNNs", "Transformers", "Transfer Learning", "Multimodal Architectures",
                   "Monocular Depth Estimation", "Embedding Extraction", "Optuna / HPO"],
    },
    {
        "icon": "👁️",
        "category": "Computer Vision &amp; 3D",
        "items": ["OpenCV", "Open3D", "GLPN", "DPT", "Point Cloud Processing",
                   "Poisson Surface Reconstruction", "Depth Estimation"],
    },
    {
        "icon": "💬",
        "category": "LLMs &amp; NLP",
        "items": ["HuggingFace Transformers", "RAG Pipelines", "Gradio", "LLM Fine-Tuning",
                   "Embedding Search"],
    },
    {
        "icon": "⚙️",
        "category": "Data &amp; Engineering",
        "items": ["Apache Spark", "PySpark", "Hadoop", "PostgreSQL", "MySQL", "Docker",
                   "ETL Design"],
    },
    {
        "icon": "☁️",
        "category": "Cloud &amp; Tools",
        "items": ["AWS (EC2, S3, RDS, Lambda)", "Git", "Linux", "Hugging Face Spaces",
                   "Kaggle"],
    },
]

EDUCATION = [
    {
        "degree": "M.S. in Data Science",
        "school": "Texas A&amp;M University",
        "meta": "GPA 3.91 / 4.00",
        "dates": "Aug 2023 – Dec 2024",
    },
    {
        "degree": "B.E. in Computer Science &amp; Engineering",
        "school": "Anna University, MIT Campus",
        "meta": "GPA 8.78 / 10.00",
        "dates": "Jul 2019 – May 2023",
    },
]

AWARDS = [
    {
        "icon": "🏆",
        "title": "TIH-IoT CHANAKYA Fellowship",
        "meta": "IIT Bombay",
        "description": "Awarded for significant contributions to AI-based Indian Sign "
                        "Language recognition research.",
    },
    {
        "icon": "📄",
        "title": "Springer Publication",
        "meta": "Secure Smart Cabin Using Optimized Arduino GSM Interface",
        "description": "Peer-reviewed publication on a secure, GSM-monitored smart cabin "
                        "system with measurable efficiency gains.",
    },
]

STATS = [
    {"number": "3.91", "label": "Grad GPA / 4.00"},
    {"number": "97.9%", "label": "Best Model Accuracy"},
    {"number": "9", "label": "Featured Projects"},
    {"number": "1", "label": "Springer Publication"},
]

# ════════════════════════════════════════════════════════════════════════
# 🎨 STYLES
# ════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg: #0A0E27;
    --bg-soft: #0F1530;
    --bg-card: #141B3C;
    --border: rgba(255,255,255,0.08);
    --text: #EDF1FB;
    --text-muted: #8E9AC4;
    --accent-cyan: #00E5FF;
    --accent-amber: #FFC857;
    --accent-coral: #FF6B6B;
    --accent-violet: #8B7CF6;
}

html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }

.stApp {
    background: radial-gradient(circle at 12% -10%, #18204c 0%, var(--bg) 45%) fixed,
                var(--bg);
    color: var(--text);
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { background: transparent; }

.block-container {
    max-width: 1080px;
    padding-top: 1.5rem;
    padding-bottom: 5rem;
}

h1, h2, h3, h4 { font-family: 'Space Grotesk', sans-serif; color: var(--text); }
a { color: var(--accent-cyan); }

/* ── Sidebar ───────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: var(--bg-soft);
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] > div { padding-top: 1.5rem; }

.sidebar-avatar {
    width: 76px; height: 76px; border-radius: 50%;
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-violet));
    display: flex; align-items: center; justify-content: center;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.7rem; font-weight: 700; color: #08101F;
    margin: 0 auto 1rem auto;
    box-shadow: 0 0 24px rgba(0,229,255,0.25);
}
.sidebar-name {
    text-align: center; font-family: 'Space Grotesk', sans-serif;
    font-weight: 600; font-size: 1.05rem; color: var(--text); line-height: 1.3;
}
.sidebar-title {
    text-align: center; color: var(--text-muted); font-size: .78rem;
    margin: .35rem 0 1.4rem 0; font-family: 'JetBrains Mono', monospace;
}
.sidebar-nav a {
    display: block; padding: .5rem .9rem; border-radius: 8px;
    color: var(--text-muted) !important; text-decoration: none !important;
    font-size: .92rem; margin-bottom: .15rem; transition: all .2s ease;
}
.sidebar-nav a:hover { background: var(--bg-card); color: var(--accent-cyan) !important; }
.sidebar-divider { border-top: 1px solid var(--border); margin: 1.3rem 0; }
.sidebar-socials { display: flex; gap: .5rem; justify-content: center; flex-wrap: wrap; }
.sidebar-socials a {
    font-family: 'JetBrains Mono', monospace; font-size: .72rem;
    border: 1px solid var(--border); border-radius: 8px; padding: .35rem .65rem;
    color: var(--text-muted) !important; text-decoration: none !important;
    transition: all .2s ease;
}
.sidebar-socials a:hover { border-color: var(--accent-cyan); color: var(--accent-cyan) !important; }
.sidebar-foot {
    text-align: center; color: var(--text-muted); font-size: .72rem;
    margin-top: 1.4rem; font-family: 'JetBrains Mono', monospace; line-height: 1.6;
}

/* ── Hero ──────────────────────────────────────────────────────────── */
.section-anchor { position: relative; top: -0.5rem; scroll-margin-top: 1rem; }

.status-badge {
    display: inline-flex; align-items: center; gap: .5rem;
    background: rgba(0,229,255,0.08); border: 1px solid rgba(0,229,255,0.25);
    border-radius: 99px; padding: .35rem .9rem; font-size: .8rem;
    font-family: 'JetBrains Mono', monospace; color: var(--accent-cyan);
    margin-bottom: 1.3rem;
}
.status-dot {
    width: 8px; height: 8px; border-radius: 50%; background: var(--accent-cyan);
    animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(0,229,255,0.45); }
    50% { box-shadow: 0 0 0 6px rgba(0,229,255,0); }
}

.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace; color: var(--accent-amber);
    letter-spacing: .25em; font-size: .8rem; text-transform: uppercase;
    margin-bottom: .6rem;
}
.hero-name {
    font-family: 'Space Grotesk', sans-serif; font-weight: 700;
    font-size: 3.4rem; line-height: 1.1; margin: 0;
    background: linear-gradient(135deg, #ffffff 15%, var(--accent-cyan) 65%, var(--accent-amber) 100%);
    -webkit-background-clip: text; background-clip: text; color: transparent;
}
.hero-role {
    font-size: 1.25rem; color: var(--text-muted); font-weight: 500;
    margin-top: .5rem; font-family: 'Space Grotesk', sans-serif;
}
.signal-wave { width: 100%; max-width: 460px; height: 38px; display: block; margin: 1rem 0 1.3rem 0; }
.signal-path {
    stroke-dasharray: 22 10;
    animation: signal-flow 2.6s linear infinite;
}
@keyframes signal-flow { to { stroke-dashoffset: -320; } }

.hero-tagline { font-size: 1.06rem; line-height: 1.75; max-width: 660px; color: var(--text); }

.cta-row { display: flex; gap: .8rem; margin: 1.6rem 0 0.4rem 0; flex-wrap: wrap; }

/* ── Buttons / tags ────────────────────────────────────────────────── */
.btn {
    font-family: 'JetBrains Mono', monospace; font-size: .82rem;
    padding: .6rem 1.3rem; border-radius: 8px; text-decoration: none !important;
    border: 1px solid var(--border); color: var(--text) !important;
    transition: all .2s ease; display: inline-block;
}
.btn-primary { background: var(--accent-cyan); color: #08101F !important; border-color: var(--accent-cyan); font-weight: 600; }
.btn-primary:hover { background: var(--accent-amber); border-color: var(--accent-amber); }
.btn-secondary:hover { border-color: var(--accent-cyan); color: var(--accent-cyan) !important; }
.btn-sm { font-size: .74rem; padding: .42rem .9rem; }

/* ── Stats row ─────────────────────────────────────────────────────── */
.stats-row { display: flex; gap: 1rem; margin: 2rem 0 1.6rem 0; flex-wrap: wrap; }
.stat-card {
    background: var(--bg-card); border: 1px solid var(--border); border-radius: 14px;
    padding: 1rem 1.3rem; flex: 1; min-width: 130px; transition: all .2s ease;
}
.stat-card:hover { transform: translateY(-3px); border-color: var(--accent-cyan); }
.stat-number { font-family: 'Space Grotesk', sans-serif; font-size: 1.7rem; font-weight: 700; color: var(--accent-cyan); }
.stat-label { font-size: .78rem; color: var(--text-muted); margin-top: .15rem; }

/* ── Marquee ───────────────────────────────────────────────────────── */
.marquee-wrap {
    overflow: hidden; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
    padding: .75rem 0; margin: 0 0 2.6rem 0; white-space: nowrap;
}
.marquee-track { display: inline-flex; gap: 2.6rem; animation: marquee 30s linear infinite; }
.marquee-wrap:hover .marquee-track { animation-play-state: paused; }
@keyframes marquee { from { transform: translateX(0); } to { transform: translateX(-50%); } }
.marquee-item { font-family: 'JetBrains Mono', monospace; font-size: .85rem; color: var(--text-muted); }
.marquee-item b { color: var(--accent-amber); font-weight: 600; }

/* ── Section headers ───────────────────────────────────────────────── */
.section-eyebrow {
    font-family: 'JetBrains Mono', monospace; color: var(--accent-amber);
    text-transform: uppercase; letter-spacing: .25em; font-size: .75rem; margin-bottom: .4rem;
}
.section-title { font-size: 1.9rem; font-weight: 700; margin: 0 0 1.3rem 0; }

/* ── About ─────────────────────────────────────────────────────────── */
.about-text { font-size: 1.02rem; line-height: 1.85; color: var(--text); }
.about-text strong { color: var(--accent-cyan); }
.about-text em { color: var(--accent-amber); font-style: normal; }

/* ── Timeline ──────────────────────────────────────────────────────── */
.timeline { position: relative; padding-left: 2rem; border-left: 2px solid var(--border); margin-top: .5rem; }
.timeline-item { position: relative; padding-bottom: 2.1rem; }
.timeline-item:last-child { padding-bottom: 0; }
.timeline-dot {
    position: absolute; left: -2.46rem; top: .35rem; width: 14px; height: 14px;
    border-radius: 50%; background: var(--bg); border: 3px solid var(--accent-cyan);
    box-shadow: 0 0 0 4px rgba(0,229,255,0.10);
}
.timeline-date { font-family: 'JetBrains Mono', monospace; font-size: .8rem; color: var(--accent-amber); margin-bottom: .25rem; }
.timeline-role { font-size: 1.15rem; font-weight: 600; color: var(--text); }
.timeline-company { color: var(--text-muted); font-size: .9rem; margin-bottom: .65rem; }
.timeline-bullets { margin: 0; padding-left: 1.2rem; color: var(--text); font-size: .94rem; line-height: 1.7; }
.timeline-bullets li { margin-bottom: .4rem; }

/* ── Project cards ─────────────────────────────────────────────────── */
.project-card {
    background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px;
    padding: 1.5rem; height: 100%; display: flex; flex-direction: column;
    transition: all .25s ease; margin-bottom: 1.2rem;
}
.project-card:hover { transform: translateY(-4px); border-color: var(--accent-cyan); box-shadow: 0 14px 30px rgba(0,229,255,0.07); }
.project-title { font-size: 1.12rem; font-weight: 600; margin-bottom: .55rem; color: var(--text); line-height: 1.35; }
.project-tags { display: flex; flex-wrap: wrap; gap: .4rem; margin-bottom: .85rem; }
.tag {
    font-family: 'JetBrains Mono', monospace; font-size: .68rem; padding: .22rem .58rem;
    border-radius: 99px; background: rgba(0,229,255,0.08); color: var(--accent-cyan);
    border: 1px solid rgba(0,229,255,0.2);
}
.project-desc { font-size: .9rem; line-height: 1.7; color: var(--text-muted); flex-grow: 1; }
.project-links { margin-top: 1.1rem; display: flex; gap: .6rem; flex-wrap: wrap; }

/* ── Earlier projects ──────────────────────────────────────────────── */
.mini-project {
    border-top: 1px solid var(--border); padding: 1rem 0;
}
.mini-project:first-child { border-top: none; padding-top: 0; }
.mini-title { font-weight: 600; color: var(--text); font-size: .98rem; }
.mini-date { font-family: 'JetBrains Mono', monospace; color: var(--accent-amber); font-size: .75rem; float: right; margin-top: .15rem; }
.mini-desc { color: var(--text-muted); font-size: .88rem; line-height: 1.65; margin-top: .35rem; clear: both; }

/* ── Skills ────────────────────────────────────────────────────────── */
.skill-category { margin-bottom: 1.5rem; }
.skill-category-title {
    font-family: 'JetBrains Mono', monospace; font-size: .85rem; text-transform: uppercase;
    letter-spacing: .12em; color: var(--accent-amber); margin-bottom: .65rem;
}
.skill-pills { display: flex; flex-wrap: wrap; gap: .5rem; }
.skill-pill {
    background: var(--bg-card); border: 1px solid var(--border); padding: .38rem .9rem;
    border-radius: 99px; font-size: .85rem; color: var(--text); transition: all .2s ease;
}
.skill-pill:hover { border-color: var(--accent-cyan); color: var(--accent-cyan); transform: translateY(-2px); }

/* ── Education / Awards ────────────────────────────────────────────── */
.edu-card, .award-card {
    background: var(--bg-card); border: 1px solid var(--border); border-radius: 14px;
    padding: 1.3rem 1.5rem; height: 100%;
}
.edu-degree, .award-title { font-weight: 600; font-size: 1.05rem; color: var(--text); }
.edu-school { color: var(--accent-cyan); font-size: .9rem; margin-top: .2rem; }
.edu-meta, .award-meta {
    color: var(--text-muted); font-size: .8rem; margin-top: .5rem;
    font-family: 'JetBrains Mono', monospace;
}
.award-icon { font-size: 1.6rem; margin-bottom: .5rem; display: block; }
.award-desc { color: var(--text-muted); font-size: .88rem; margin-top: .55rem; line-height: 1.65; }

/* ── Contact ───────────────────────────────────────────────────────── */
.contact-card {
    background: linear-gradient(135deg, var(--bg-card), var(--bg-soft));
    border: 1px solid var(--border); border-radius: 18px;
    padding: 2.4rem 2rem; text-align: center; margin-top: .5rem;
}
.contact-card h3 { margin-top: 0; font-size: 1.5rem; }
.contact-card p { color: var(--text-muted); max-width: 520px; margin: .5rem auto 1.5rem auto; line-height: 1.7; }
.contact-links { display: flex; gap: .9rem; justify-content: center; flex-wrap: wrap; }

/* ── Footer ────────────────────────────────────────────────────────── */
.footer-note {
    text-align: center; color: var(--text-muted); font-size: .82rem;
    margin-top: 3rem; font-family: 'JetBrains Mono', monospace; line-height: 1.8;
}
.footer-note .heart { color: var(--accent-coral); }
.footer-note a { color: var(--accent-cyan); text-decoration: none; }

/* ── Animations ────────────────────────────────────────────────────── */
@keyframes fadeInUp { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: translateY(0); } }
.fade-in { animation: fadeInUp .7s ease both; }
.fade-in-1 { animation: fadeInUp .7s ease .12s both; }
.fade-in-2 { animation: fadeInUp .7s ease .24s both; }
.fade-in-3 { animation: fadeInUp .7s ease .36s both; }

@media (prefers-reduced-motion: reduce) {
    * { animation: none !important; transition: none !important; }
}
@media (max-width: 640px) {
    .hero-name { font-size: 2.3rem; }
    .stats-row { flex-direction: column; }
    .mini-date { float: none; display: block; margin-top: .2rem; }
}
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# 🧩 RENDER HELPERS
# ════════════════════════════════════════════════════════════════════════

def project_card_html(p):
    tags = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
    links = PROJECT_LINKS.get(p["key"], {})
    buttons = ""
    if links.get("live"):
        buttons += (f'<a class="btn btn-primary btn-sm" href="{links["live"]}" '
                     f'target="_blank">▶ Live Demo</a>')
    if links.get("github"):
        buttons += (f'<a class="btn btn-secondary btn-sm" href="{links["github"]}" '
                     f'target="_blank">⌥ Code</a>')
    return (
        '<div class="project-card">'
        f'<div class="project-title">{p["title"]}</div>'
        f'<div class="project-tags">{tags}</div>'
        f'<div class="project-desc">{p["description"]}</div>'
        f'<div class="project-links">{buttons}</div>'
        '</div>'
    )


def timeline_html():
    items = ""
    for e in EXPERIENCE:
        bullets = "".join(f"<li>{b}</li>" for b in e["bullets"])
        items += (
            '<div class="timeline-item">'
            '<div class="timeline-dot"></div>'
            f'<div class="timeline-date">{e["dates"]}</div>'
            f'<div class="timeline-role">{e["role"]}</div>'
            f'<div class="timeline-company">{e["company"]} · {e["location"]}</div>'
            f'<ul class="timeline-bullets">{bullets}</ul>'
            '</div>'
        )
    return f'<div class="timeline">{items}</div>'


def skills_html():
    out = ""
    for s in SKILLS:
        pills = "".join(f'<span class="skill-pill">{i}</span>' for i in s["items"])
        out += (
            '<div class="skill-category">'
            f'<div class="skill-category-title">{s["icon"]}  {s["category"]}</div>'
            f'<div class="skill-pills">{pills}</div>'
            '</div>'
        )
    return out


def marquee_html():
    items = "".join(
        f'<div class="marquee-item">⚡ <b>{topic}</b></div>' for topic in CURRENTLY_EXPLORING
    )
    return f'<div class="marquee-wrap"><div class="marquee-track">{items}{items}</div></div>'


def signal_wave_svg():
    return """
    <svg class="signal-wave" viewBox="0 0 460 40" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <defs>
            <linearGradient id="sigGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#00E5FF"/>
                <stop offset="50%" stop-color="#FFC857"/>
                <stop offset="100%" stop-color="#FF6B6B"/>
            </linearGradient>
        </defs>
        <path d="M0,20 L60,20 L80,4 L100,36 L120,20 L460,20"
              stroke="url(#sigGrad)" stroke-width="3" fill="none"
              stroke-linecap="round" stroke-linejoin="round" class="signal-path"/>
    </svg>
    """


# ════════════════════════════════════════════════════════════════════════
# 📍 PAGE ROUTING — ?page=resume shows the embedded resume viewer
# ════════════════════════════════════════════════════════════════════════
_current_page = st.query_params.get("page", "main")

if _current_page == "resume":

    # ── Shared sidebar (resume view) ─────────────────────────────────
    with st.sidebar:
        st.markdown('<div class="sidebar-avatar">PR</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sidebar-name">{NAME}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sidebar-title">{ROLE}</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sidebar-nav">
            <a href="/">🏠 &nbsp; Portfolio Home</a>
            <a href="#resume-top">📄 &nbsp; Resume</a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="sidebar-socials">
            <a href="{SOCIAL['github']}" target="_blank">GitHub</a>
            <a href="{SOCIAL['linkedin']}" target="_blank">LinkedIn</a>
            <a href="{SOCIAL['email']}">Email</a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(
            '<div class="sidebar-foot">📍 ' + LOCATION + '<br>Built with Python + Streamlit</div>',
            unsafe_allow_html=True,
        )

    # ── Resume viewer ────────────────────────────────────────────────
    st.markdown('<div id="resume-top" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-eyebrow">// Resume</div>', unsafe_allow_html=True)

    r_col1, r_col2 = st.columns([3, 1])
    with r_col1:
        st.markdown(f'<div class="section-title">{NAME}</div>', unsafe_allow_html=True)
    with r_col2:
        st.markdown("""
        <div style="display:flex; justify-content:flex-end; align-items:center; height:100%; padding-top:0.6rem;">
        """, unsafe_allow_html=True)
        st.markdown(f'<a class="btn btn-secondary" href="/">← Back to Portfolio</a>',
                    unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    _pdf_exists = PDF_PATH.exists()
    if _pdf_exists:
        _pdf_bytes = PDF_PATH.read_bytes()
        _b64 = base64.b64encode(_pdf_bytes).decode()

        # Use components.html + JS blob URL — avoids browser data: URI iframe blocks
        _viewer_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ background: transparent; }}
            embed {{
                display: block;
                width: 100%;
                height: 920px;
                border: none;
                border-radius: 8px;
            }}
        </style>
        </head>
        <body>
        <embed id="pdf-viewer" type="application/pdf" />
        <script>
            (function() {{
                var b64 = '{_b64}';
                var binary = atob(b64);
                var bytes = new Uint8Array(binary.length);
                for (var i = 0; i < binary.length; i++) {{
                    bytes[i] = binary.charCodeAt(i);
                }}
                var blob = new Blob([bytes], {{ type: 'application/pdf' }});
                var url  = URL.createObjectURL(blob);
                document.getElementById('pdf-viewer').src = url;
            }})();
        </script>
        </body>
        </html>
        """
        components.html(_viewer_html, height=940, scrolling=False)

        st.markdown("<br>", unsafe_allow_html=True)

        dl_col, back_col, _ = st.columns([1, 1, 3])
        with dl_col:
            st.download_button(
                label="⬇ Download PDF",
                data=_pdf_bytes,
                file_name="Priyadharshini_Ramesh_Kumar_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        with back_col:
            st.markdown(
                '<a class="btn btn-secondary" href="/" style="display:block;text-align:center;padding:.6rem 0;">← Portfolio</a>',
                unsafe_allow_html=True,
            )

    else:
        st.markdown(f"""
        <div class="contact-card" style="text-align:left; padding: 2rem;">
            <h3>📄 Resume PDF not found</h3>
            <p>
                Push <code>assets/Priyadharshini_Ramesh_Kumar_Resume.pdf</code>
                to the repo root so Streamlit can find and embed it here.
                Once it's there, this page will render the full resume inline.
            </p>
            <a class="btn btn-secondary" href="/">← Back to Portfolio</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="footer-note">
        © 2026 {NAME} &nbsp;·&nbsp;
        <a href="/">Back to Portfolio ↑</a>
    </div>
    """, unsafe_allow_html=True)

    st.stop()   # don't render the portfolio below

# ════════════════════════════════════════════════════════════════════════
# 🧭 SIDEBAR
# ════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown('<div class="sidebar-avatar">PR</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sidebar-name">{NAME}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sidebar-title">{ROLE}</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-nav">
        <a href="#top">🏠 &nbsp; Home</a>
        <a href="#about">🙋 &nbsp; About</a>
        <a href="#experience">💼 &nbsp; Experience</a>
        <a href="#projects">🚀 &nbsp; Projects</a>
        <a href="#skills">🛠️ &nbsp; Skills</a>
        <a href="#education">🎓 &nbsp; Education</a>
        <a href="#awards">🏆 &nbsp; Awards</a>
        <a href="#contact">✉️ &nbsp; Contact</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="sidebar-socials">
        <a href="{SOCIAL['github']}" target="_blank">GitHub</a>
        <a href="{SOCIAL['linkedin']}" target="_blank">LinkedIn</a>
        <a href="{SOCIAL['email']}">Email</a>
        <a href="?page=resume">Resume 📄</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-foot">📍 ' + LOCATION + '<br>Built with Python + Streamlit</div>',
        unsafe_allow_html=True,
    )

# ════════════════════════════════════════════════════════════════════════
# 🚀 HERO
# ════════════════════════════════════════════════════════════════════════
st.markdown('<div id="top" class="section-anchor"></div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="fade-in">
    <div class="status-badge"><span class="status-dot"></span> Open to Data Science / ML Engineering roles</div>
    <div class="hero-eyebrow">// Data Scientist · ML Engineer · Builder</div>
    <h1 class="hero-name">{NAME}</h1>
    <div class="hero-role">{ROLE}</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<div class="fade-in-1">{signal_wave_svg()}</div>', unsafe_allow_html=True)

st.markdown(f'<div class="hero-tagline fade-in-1">{TAGLINE}</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="cta-row fade-in-2">
    <a class="btn btn-primary" href="#projects">🚀 View Projects</a>
    <a class="btn btn-secondary" href="#contact">✉️ Get in Touch</a>
    <a class="btn btn-secondary" href="?page=resume">📄 Resume</a>
</div>
""", unsafe_allow_html=True)

stat_cards = "".join(
    f'<div class="stat-card"><div class="stat-number">{s["number"]}</div>'
    f'<div class="stat-label">{s["label"]}</div></div>'
    for s in STATS
)
st.markdown(f'<div class="stats-row fade-in-3">{stat_cards}</div>', unsafe_allow_html=True)

st.markdown(marquee_html(), unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# 🙋 ABOUT
# ════════════════════════════════════════════════════════════════════════
st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">// 01 · About</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">A bit about me</div>', unsafe_allow_html=True)
st.markdown(f'<div class="about-text">{ABOUT}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# 💼 EXPERIENCE
# ════════════════════════════════════════════════════════════════════════
st.markdown('<div id="experience" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">// 02 · Experience</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Where I\'ve been building</div>', unsafe_allow_html=True)
st.markdown(timeline_html(), unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# 🚀 PROJECTS
# ════════════════════════════════════════════════════════════════════════
st.markdown('<div id="projects" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">// 03 · Projects</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Things I\'ve built</div>', unsafe_allow_html=True)

cols = st.columns(2)
for i, p in enumerate(PROJECTS):
    with cols[i % 2]:
        st.markdown(project_card_html(p), unsafe_allow_html=True)

with st.expander("🗂️  Earlier projects & publications"):
    for ep in EARLIER_PROJECTS:
        st.markdown(f"""
        <div class="mini-project">
            <span class="mini-date">{ep['dates']}</span>
            <div class="mini-title">{ep['title']}</div>
            <div class="mini-desc">{ep['description']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# 🛠️ SKILLS
# ════════════════════════════════════════════════════════════════════════
st.markdown('<div id="skills" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">// 04 · Skills</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">My toolbox</div>', unsafe_allow_html=True)

skill_cols = st.columns(2)
for i, s in enumerate(SKILLS):
    with skill_cols[i % 2]:
        pills = "".join(f'<span class="skill-pill">{item}</span>' for item in s["items"])
        st.markdown(f"""
        <div class="skill-category">
            <div class="skill-category-title">{s['icon']}&nbsp;&nbsp;{s['category']}</div>
            <div class="skill-pills">{pills}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# 🎓 EDUCATION
# ════════════════════════════════════════════════════════════════════════
st.markdown('<div id="education" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">// 05 · Education</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Academic background</div>', unsafe_allow_html=True)

edu_cols = st.columns(2)
for i, e in enumerate(EDUCATION):
    with edu_cols[i % 2]:
        st.markdown(f"""
        <div class="edu-card">
            <div class="edu-degree">{e['degree']}</div>
            <div class="edu-school">{e['school']}</div>
            <div class="edu-meta">{e['meta']} &nbsp;·&nbsp; {e['dates']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# 🏆 AWARDS
# ════════════════════════════════════════════════════════════════════════
st.markdown('<div id="awards" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">// 06 · Recognition</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Awards &amp; publications</div>', unsafe_allow_html=True)

award_cols = st.columns(2)
for i, a in enumerate(AWARDS):
    with award_cols[i % 2]:
        st.markdown(f"""
        <div class="award-card">
            <span class="award-icon">{a['icon']}</span>
            <div class="award-title">{a['title']}</div>
            <div class="award-meta">{a['meta']}</div>
            <div class="award-desc">{a['description']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# ✉️ CONTACT
# ════════════════════════════════════════════════════════════════════════
st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">// 07 · Contact</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Let\'s build something</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="contact-card">
    <h3>Got a problem worth digging into?</h3>
    <p>
        I'm always up for talking about data pipelines, geospatial ML, RAG systems, or
        why a model's validation curve looks a little too good to be true. Reach out,
        I'd love to hear from you.
    </p>
    <div class="contact-links">
        <a class="btn btn-primary" href="{SOCIAL['email']}">✉️ {SOCIAL['email_display']}</a>
        <a class="btn btn-secondary" href="{SOCIAL['linkedin']}" target="_blank">in LinkedIn</a>
        <a class="btn btn-secondary" href="{SOCIAL['github']}" target="_blank">⌥ GitHub</a>
        <a class="btn btn-secondary" href="?page=resume">📄 Resume</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="footer-note">
    Designed &amp; built with Python, Streamlit, and an unreasonable amount of curiosity about how things work
    <span class="heart">⚡</span>
    <br>
    © 2026 {NAME} &nbsp;·&nbsp; <a href="#top">Back to top ↑</a>
</div>
""", unsafe_allow_html=True)
