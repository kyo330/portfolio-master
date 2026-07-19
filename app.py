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
# 📄 RESUME PDF: resolved relative to app.py regardless of working dir
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
    "phone": "+91 89760 66703",
    "linkedin": "https://www.linkedin.com/in/priyadharshini-r330",
    "github": "https://github.com/kyo330",
    # Resume opens as an in-app tab (see ?page=resume routing below)
    "resume_pdf": RESUME_URL,
}

# TODO: replace these "#" placeholders with real GitHub repos / live demo
# URLs for each project. Set a value to None to hide that button entirely.
PROJECT_LINKS = {
    "energy": {"github": "https://github.com/kyo330/SEMD", "live": "https://spain-energy-hourly.streamlit.app"},
    "depthforge": {"live": "https://huggingface.co/spaces/Tohru127/DepthForge"},
    "multimodal": {"github": "https://github.com/kyo330/Multimodal-Digits-MNIST"},
    "customer_intel": {"github": "https://github.com/kyo330/custintelli", "live": "https://customeriltel.streamlit.app"},
    "thunderstorm": {"github": "https://github.com/kyo330/HLMA-website", "live": "https://hlma-website.streamlit.app"},
    "spotify_yt": {"github": "https://github.com/kyo330/Spotify", "live": "https://us-east-1.online.tableau.com/#/site/priyadharshinir-62119495e6/views/SpotifyYoutubeCrossPlatformPerformanceAnalysis/PerformanceDashboard?:iid=1"},
    "hyperspectral": {"github": "https://github.com/kyo330/Hyperspectral-Image-Encryption-and-Decryption"},
    "smart_cabin": {"paper": "https://link.springer.com/chapter/10.1007/978-981-99-7622-5_20"},
}

# ════════════════════════════════════════════════════════════════════════
# 📄 CONTENT DATA
# ════════════════════════════════════════════════════════════════════════
NAME = "Priyadharshini Ramesh Kumar"
ROLE = "Data Scientist & Machine Learning Engineer"
LOCATION = "Chennai, TN, India"

TAGLINE = (
    "I build things like RAG pipelines that make oil & gas documents auditable, "
    "algorithms that stitch satellite data into lightning flashes, and a pipeline "
    "that turns one RGB photo into a 3D mesh. I like problems messy enough to be "
    "interesting, and I'm always up for learning something new, so if you're "
    "building something too, let's talk!"
)

ABOUT = """
I'm a data scientist with an M.S. in Data Science from <strong>Texas A&amp;M University</strong>
(GPA 3.91/4.00) and a B.E. in Computer Science &amp; Engineering from
<strong>Anna University, MIT Campus</strong>. My work spans machine learning,
geospatial analytics, and large-scale data engineering, clustering extreme lightning
events in satellite data, building safety-critical RAG pipelines for oil &amp; gas, and
reconstructing 3D scenes from a single photo, and honestly, I enjoy every bit of the
range.
<br><br>
I learn best by doing. Hand me a new dataset, a new tool, or a domain I've never
touched before, and I'll happily lose a weekend figuring out how it all fits
together. I'm currently <strong>open to new data science and ML engineering
opportunities</strong>, and always genuinely excited to connect, whether that's about
a role, a collaboration, or just a good problem worth digging into. If you're
working on something interesting, <em>I'd love to hear about it</em>.
"""

CURRENTLY_LEARNING = [
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
            "Built a multi-stage pipeline converting raw oil &amp; gas technical PDFs into a "
            "structured, RAG-ready knowledge base, domain discovery, GPT-4o scenario "
            "extraction and playbook generation, batch domain reclassification, and "
            "rule-based governance validation, processing batches of 3,000+ chunks per run.",
            "Designed a two-stage GPT-4o extraction process over overlapping ~20k-character "
            "document windows: detecting operational scenarios per section, then generating "
            "structured playbooks (trigger conditions, decision points, diagnostics, "
            "escalation paths) traceable back to source file and page range.",
            "Built a governance validator enforcing an 8-section compliance checklist via "
            "regex-based content rules, cutting a batch of 483 chunks down to 256 "
            "auto-approved, with the remainder routed to rewrite or rejection with itemized "
            "reasons.",
        ],
    },
    {
        "role": "Research Data Scientist",
        "company": "Texas A&amp;M University",
        "location": "College Station, TX",
        "dates": "Aug 2024 – Jan 2026",
        "bullets": [
            "Implemented and benchmarked four lightning \"flash-stitching\" algorithms "
            "(sequential threshold-based, DBSCAN, hierarchical agglomerative, "
            "graph-based/NetworkX) to group raw GLM satellite detections into discrete "
            "flash events, following the Peterson (2023) spatiotemporal methodology.",
            "Quantitatively compared algorithm outputs using flash count, megaflash count, "
            "and extent distributions, then measured pairwise agreement via Adjusted Rand "
            "Index (e.g. DBSCAN vs. graph-based: 0.875) to identify where methods diverged.",
            "Built a Streamlit/Leaflet tool parsing raw HLMA sensor exports with a generic "
            "fallback parser for malformed files, overlaying altitude-tiered lightning "
            "clusters with NOAA storm-event reports; also supported the group's data "
            "cleaning and visualization needs, and prototyped FloodSense, an exploratory "
            "flood-risk tool, at the professor's suggestion.",
        ],
    },
    {
        "role": "Research Assistant",
        "company": "Texas A&amp;M University, SGL Lab",
        "location": "College Station, TX",
        "dates": "Feb 2024 – Apr 2024",
        "bullets": [
            "Conducted initial data discovery on global wood trade-flow data (import/export "
            "volumes by wood type, production drivers, and downstream industries) before "
            "the team's focus shifted to causal/probabilistic modeling.",
            "Built a 3-node Bayesian network analysis of a semiconductor supply chain "
            "(government funding → chip manufacturing → exports), discretizing each "
            "variable via empirical CDF-based tercile thresholds and constructing joint "
            "probability tables to trace how upstream funding risk propagated downstream.",
            "Ran time-series diagnostics on the underlying data, an Augmented Dickey-Fuller "
            "test and an ARCH test on regression residuals, to test modeling assumptions, "
            "then communicated the risk-propagation findings and tradeoffs to non-technical "
            "stakeholders.",
        ],
    },
    {
        "role": "Research Assistant",
        "company": "Anna University, MIT Campus &nbsp;·&nbsp; TIH-IoT CHANAKYA Fellowship (IIT Bombay)",
        "location": "Chennai, India",
        "dates": "Jan 2022 – Nov 2022",
        "bullets": [
            "Curated a labelled dataset of 26 Indian Sign Language gestures from simple- "
            "and complex-background video footage using Python and OpenCV, extracting "
            "per-frame features and integrating them into a larger, existing 41-class "
            "gesture recognition dataset used to train the project's models.",
            "Built and trained a CNN and a VGG16 transfer-learning model for gesture "
            "classification, comparing architectures on accuracy, loss curves, and "
            "per-class precision/recall/F1 across training.",
            "Part of a four-person student research team under Dr. Ponsy R.K. Sathia "
            "Bhama, working toward an ISL recognition system for educational-domain signs, "
            "funded through the TIH-IoT CHANAKYA Fellowship (IIT Bombay's DST-sponsored IoT "
            "research hub).",
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
            "surface area, volume) and a side-by-side GLPN vs. DPT sample comparison across "
            "indoor and outdoor scenes. Deployed on Hugging Face Spaces with a consent "
            "gate, EXIF privacy checks, and PLY/OBJ/STL export."
        ),
    },
    {
        "key": "multimodal",
        "title": "Multimodal Fusion Network (Vision + Audio)",
        "tags": ["Python", "Keras", "Optuna", "t-SNE"],
        "description": (
            "A dual-stream neural network built from scratch, pairing a three-layer Conv2D "
            "encoder for handwritten digit images with a three-layer Conv1D encoder for "
            "spoken digit audio, concatenated through a dropout-regularised dense head into "
            "a 10-class softmax output, reaching 98.9% accuracy and 98.9% F1 on the "
            "validation split. Tuned both branches jointly with Optuna across filter counts, "
            "dense units, dropout rate, and learning rate, searching the modalities together "
            "rather than optimizing each in isolation. Applied t-SNE with KMeans to the "
            "fused image-audio embeddings to inspect class separation in the learned "
            "representation space."
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
        "title": "4D Thunderstorm Visualization: HLMA Capstone",
        "tags": ["Python", "Leaflet", "Streamlit", "Team of 2"],
        "description": (
            "An interactive lightning visualization platform built on Houston Lightning "
            "Mapping Array data (~150,000 new points per minute), replacing a static 2D "
            "map with altitude-based filtering, colour-coded risk tiers, and zoom/pan "
            "interaction. Evaluated Bokeh, D3.js, and Leaflet, and prototyped a full 3D view "
            "before deliberately rejecting it for occlusion, misleading depth perception, "
            "and rendering cost under high-density real-time data, choosing Leaflet for "
            "rendering performance and GeoJSON support instead. Defined danger zones from "
            "lightning frequency and altitude thresholds (below 12 km low-risk, 12–14 km "
            "overshooting tops, above 14 km severe) so responders could read storm severity "
            "at a glance. Supervised by Dr. Timothy Logan, Dept. of Atmospheric Sciences."
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
    {
        "key": "hyperspectral",
        "title": "Hyperspectral Image Security via LAB Colour Space Encryption",
        "tags": ["Python", "PCA", "OpenCV", "B.E. Final Year Project"],
        "description": (
            "Designed a chaotic encryption algorithm (pseudorandom chaotic image scrambling) "
            "for hyperspectral images in the CIELAB colour space, applying channel-independent "
            "permutation matrices across the L, a, and b channels with per-channel "
            "pseudorandom generators to improve robustness against statistical and "
            "brute-force attacks. Built a preprocessing pipeline with PCA (reduced to 30 "
            "components) and Gaussian filtering to denoise the AVIRIS Indian Pines dataset "
            "(224 bands, 145×145 px) before encryption, achieving a PSNR of 49.9 dB and SSIM "
            "of 0.9998 on decrypted images, with encrypted-image histograms showing "
            "near-uniform distribution."
        ),
    },
    {
        "key": "smart_cabin",
        "title": "Secure Smart Cabin Using Optimized Arduino GSM Interface",
        "tags": ["Arduino", "GSM", "RFID", "IoT", "Team of 4", "Published in Springer"],
        "description": (
            "A smart-office IoT system on Arduino UNO integrating six functional modules: "
            "environmental sensing (temperature, humidity, smoke/gas via DHT11 and MQ-series "
            "sensors), motion detection (PIR), dual-mode secure entry (RFID + keypad lock), a "
            "monitoring dashboard, GSM/Wi-Fi connectivity (ESP32), and cloud data storage "
            "(Adafruit IO, Arduino IoT Cloud). Implemented an IFTTT-based automation layer "
            "triggering multi-channel emergency alerts (SMS, email, and Discord) on "
            "smoke/fire detection, alongside a remote dashboard for real-time temperature and "
            "humidity monitoring and appliance control. This work has been published as a "
            "peer-reviewed Springer book chapter (DOI: 10.1007/978-981-99-7622-5_20)."
        ),
    },
]

EARLIER_PROJECTS = [
    {
        "title": "Air Pollutant Prediction from Multisensor Data",
        "dates": "Aug 2023 – Dec 2023 &nbsp;·&nbsp; Team of 3",
        "description": (
            "Cleaned a 9,357-row UCI air quality dataset to 6,095 usable rows (missing-value "
            "handling, a >90%-null column dropped, 846 outliers removed via a conservative "
            "IQR threshold), then benchmarked six regressors (MLP, Random Forest, Gradient "
            "Boosting, Linear Regression, Decision Tree, SVR) to predict CO sensor response "
            "from four co-located pollutant sensors. Tuned an MLP with 5-fold GridSearchCV "
            "to R&sup2; 0.876 (RMSE 64.9), but recommended Random Forest (R&sup2; 0.872) "
            "instead for its interpretability via feature importance and lower compute cost; "
            "the O&#8323; sensor dominated feature importance at ~0.69."
        ),
    },
]

SKILLS = [
    {
        "icon": "🐍",
        "category": "Languages",
        "items": ["Python", "SQL", "R"],
    },
    {
        "icon": "🧠",
        "category": "Machine Learning",
        "items": ["Regression", "Classification", "Ensemble Methods", "Clustering",
                   "Bayesian Modeling", "Hyperparameter Optimisation"],
    },
    {
        "icon": "🔥",
        "category": "Deep Learning",
        "items": ["PyTorch", "TensorFlow/Keras", "CNNs", "Transfer Learning",
                   "Multimodal Architectures"],
    },
    {
        "icon": "💬",
        "category": "LLMs &amp; NLP",
        "items": ["LLM API Integration", "RAG Pipelines", "Prompt Engineering"],
    },
    {
        "icon": "📊",
        "category": "Statistics",
        "items": ["Hypothesis Testing", "Time-Series Diagnostics", "Feature Importance Analysis"],
    },
    {
        "icon": "👁️",
        "category": "Computer Vision",
        "items": ["OpenCV", "HuggingFace Transformers", "Open3D"],
    },
    {
        "icon": "⚙️",
        "category": "Data Engineering",
        "items": ["Data Cleaning", "Preprocessing", "Outlier Detection", "Pipeline Automation"],
    },
    {
        "icon": "☁️",
        "category": "Visualisation &amp; Deployment",
        "items": ["Streamlit", "Plotly", "GeoPandas", "Git/GitHub"],
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
        "icon": "📄",
        "title": "Published in Springer",
        "meta": "Secure Smart Cabin Using Optimized Arduino GSM Interface &nbsp;·&nbsp; DOI: 10.1007/978-981-99-7622-5_20",
        "description": "This work has been published as a peer-reviewed book chapter by "
                        "Springer, following presentation at a conference on the system's "
                        "design and results.",
    },
]

STATS = [
    {"number": "3.91", "label": "Grad GPA / 4.00"},
    {"number": "98.9%", "label": "Best Model Accuracy"},
    {"number": "9", "label": "Featured Projects"},
    {"number": "1", "label": "Published Paper (Springer)"},
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
    if links.get("paper"):
        buttons += (f'<a class="btn btn-secondary btn-sm" href="{links["paper"]}" '
                     f'target="_blank">📄 Paper</a>')
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
        f'<div class="marquee-item">⚡ <b>{topic}</b></div>' for topic in CURRENTLY_LEARNING
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
# 📍 PAGE ROUTING: ?page=resume shows the embedded resume viewer
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

        # PDF.js renders each page to a <canvas>, works in all browsers,
        # no plugin needed, no blob/data-URI restrictions.
        _VIEWER_TMPL = """<!DOCTYPE html>
<html>
<head>
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { background: #0A0E27; }
    #loading {
        color: #00E5FF;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        text-align: center;
        padding: 2rem;
        letter-spacing: 0.1em;
    }
    .page-wrap {
        margin: 0 auto 16px auto;
        box-shadow: 0 6px 24px rgba(0,0,0,0.5);
        border-radius: 4px;
        overflow: hidden;
        display: block;
        width: fit-content;
    }
    canvas { display: block; }
</style>
</head>
<body>
<div id="loading">⚡ Loading resume...</div>
<div id="pdf-container"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<script>
pdfjsLib.GlobalWorkerOptions.workerSrc =
    'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

var raw = atob('B64_DATA');
var bytes = new Uint8Array(raw.length);
for (var i = 0; i < raw.length; i++) bytes[i] = raw.charCodeAt(i);

pdfjsLib.getDocument({ data: bytes }).promise.then(function(pdf) {
    document.getElementById('loading').style.display = 'none';
    var container = document.getElementById('pdf-container');

    function renderPage(n) {
        pdf.getPage(n).then(function(page) {
            var vp0    = page.getViewport({ scale: 1 });
            var scale  = (container.clientWidth || 780) / vp0.width;
            var vp     = page.getViewport({ scale: scale });

            var canvas       = document.createElement('canvas');
            canvas.width     = vp.width;
            canvas.height    = vp.height;

            var wrap = document.createElement('div');
            wrap.className = 'page-wrap';
            wrap.appendChild(canvas);
            container.appendChild(wrap);

            page.render({ canvasContext: canvas.getContext('2d'), viewport: vp })
                .promise.then(function() {
                    if (n < pdf.numPages) renderPage(n + 1);
                });
        });
    }
    renderPage(1);

}).catch(function(err) {
    document.getElementById('loading').textContent = 'Could not load PDF: ' + err.message;
});
</script>
</body>
</html>"""
        _viewer_html = _VIEWER_TMPL.replace("B64_DATA", _b64)

        # ── Download + back row (above viewer so always visible) ──────
        dl_col, back_col, _ = st.columns([1, 1, 3])
        with dl_col:
            st.markdown(
                '<a class="btn btn-primary" '
                'href="data:application/pdf;base64,' + _b64 + '" '
                'download="Priyadharshini_Ramesh_Kumar_Resume.pdf" '
                'style="display:block;text-align:center;padding:.6rem 0;">⬇ Download PDF</a>',
                unsafe_allow_html=True,
            )
        with back_col:
            st.markdown(
                '<a class="btn btn-secondary" href="/" style="display:block;text-align:center;padding:.6rem 0;">← Portfolio</a>',
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # height: ~1200px per page × 2 pages + padding
        components.html(_viewer_html, height=2600, scrolling=True)

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
    <div class="status-badge"><span class="status-dot"></span> Open to Data Science / ML roles &amp; new opportunities</div>
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
    <h3>Let's talk! ✨</h3>
    <p>
        I'm actively looking for data science and ML engineering opportunities, and
        I'm always excited to connect, whether that's about a role, a collaboration,
        a new tool worth learning, or just a good problem to think through together.
        No idea is too early-stage, no question too small. Reach out, I'd genuinely
        love to hear from you!
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
