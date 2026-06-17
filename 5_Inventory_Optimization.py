"""
styles.py  –  Shared design system for RetailPulse dashboard
Blue glassmorphism dark theme (reference image style, blue palette)
"""

# ── Color Palette ─────────────────────────────────────────────────────────────
BLUE_PRIMARY   = "#00BFFF"   # electric sky blue
BLUE_BRIGHT    = "#00D4FF"
BLUE_DEEP      = "#0066CC"
BLUE_GLOW      = "#0099FF"
BLUE_DIM       = "#1A6EBD"
ACCENT_CYAN    = "#00E5FF"
ACCENT_TEAL    = "#00B4A0"
ALERT_RED      = "#FF4D6D"
ALERT_ORANGE   = "#FF9A3C"
ALERT_GREEN    = "#00E096"

BG_BASE        = "#060B18"   # near-black navy
BG_CARD        = "rgba(10,20,50,0.72)"
BG_CARD_HOVER  = "rgba(0,102,204,0.18)"
BORDER_COLOR   = "rgba(0,191,255,0.18)"
BORDER_GLOW    = "rgba(0,191,255,0.45)"
TEXT_MAIN      = "#E8F4FF"
TEXT_MUTED     = "#7AA8CC"
TEXT_DIM       = "#3E6080"

# ── Plotly dark template overrides ───────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    template        = "plotly_dark",
    paper_bgcolor   = "rgba(0,0,0,0)",
    plot_bgcolor    = "rgba(6,11,24,0.0)",
    font            = dict(family="Inter, sans-serif", color=TEXT_MAIN, size=12),
    margin          = dict(l=0, r=0, t=28, b=0),
    legend          = dict(
        bgcolor     = "rgba(10,20,50,0.6)",
        bordercolor = BORDER_COLOR,
        borderwidth = 1,
        font        = dict(size=11),
    ),
    xaxis = dict(
        gridcolor  = "rgba(0,191,255,0.07)",
        linecolor  = "rgba(0,191,255,0.15)",
        tickfont   = dict(color=TEXT_MUTED),
    ),
    yaxis = dict(
        gridcolor  = "rgba(0,191,255,0.07)",
        linecolor  = "rgba(0,191,255,0.15)",
        tickfont   = dict(color=TEXT_MUTED),
    ),
)

BLUE_SEQ  = [BLUE_DEEP, BLUE_GLOW, BLUE_PRIMARY, BLUE_BRIGHT, ACCENT_CYAN]
QUAL_COLORS = [
    "#00BFFF","#00E5FF","#0066CC","#00B4A0",
    "#4FC3F7","#0288D1","#00ACC1","#26C6DA",
]

# ── Global CSS ────────────────────────────────────────────────────────────────
GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    color: #E8F4FF;
}
.main { background-color: #060B18 !important; }
.block-container { padding-top: 1.2rem !important; padding-bottom: 2rem !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #060F28 0%, #040810 100%) !important;
    border-right: 1px solid rgba(0,191,255,0.12) !important;
}
[data-testid="stSidebar"] * { color: #C8E0FF !important; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── KPI Card ── */
.kpi-card {
    background: rgba(10,24,60,0.72);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(0,191,255,0.18);
    border-top: 2px solid #00BFFF;
    border-radius: 14px;
    padding: 20px 22px 16px;
    margin-bottom: 10px;
    position: relative;
    overflow: hidden;
    transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
    box-shadow: 0 4px 32px rgba(0,0,0,0.45), inset 0 0 30px rgba(0,102,204,0.04);
}
.kpi-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00BFFF, transparent);
    opacity: 0.6;
}
.kpi-card:hover {
    transform: translateY(-4px);
    border-color: rgba(0,191,255,0.45);
    box-shadow: 0 8px 40px rgba(0,102,204,0.28), 0 0 20px rgba(0,191,255,0.1);
}
.kpi-label {
    font-size: 0.70rem;
    font-weight: 600;
    color: #7AA8CC;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 6px;
}
.kpi-value {
    font-size: 2.1rem;
    font-weight: 800;
    color: #00BFFF;
    line-height: 1.1;
    letter-spacing: -0.5px;
    text-shadow: 0 0 20px rgba(0,191,255,0.5);
}
.kpi-delta {
    font-size: 0.78rem;
    font-weight: 500;
    color: #00E096;
    margin-top: 5px;
    display: flex;
    align-items: center;
    gap: 4px;
}
.kpi-delta.neg { color: #FF4D6D; }
.kpi-icon {
    position: absolute;
    top: 16px; right: 18px;
    font-size: 1.8rem;
    opacity: 0.18;
}

/* ── Glass Card ── */
.glass-card {
    background: rgba(10,24,60,0.65);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(0,191,255,0.15);
    border-radius: 16px;
    padding: 22px 24px;
    margin-bottom: 14px;
    box-shadow: 0 4px 40px rgba(0,0,0,0.4);
}

/* ── Section Header ── */
.section-header {
    font-size: 1.1rem;
    font-weight: 700;
    color: #E8F4FF;
    border-bottom: 1px solid rgba(0,191,255,0.2);
    padding-bottom: 8px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(0,191,255,0.3), transparent);
    margin-left: 8px;
}

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #060F28 0%, #0A1A3A 50%, #060B18 100%);
    border: 1px solid rgba(0,191,255,0.14);
    border-radius: 20px;
    padding: 44px 40px;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 10px;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -60px; left: 50%; transform: translateX(-50%);
    width: 600px; height: 200px;
    background: radial-gradient(ellipse, rgba(0,191,255,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-size: 3.2rem;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -1px;
    line-height: 1.1;
}
.hero-sub {
    font-size: 1.15rem;
    color: #00BFFF;
    font-weight: 600;
    margin: 10px 0 6px;
}
.hero-desc {
    font-size: 0.88rem;
    color: #7AA8CC;
    margin-bottom: 22px;
}

/* ── Badge ── */
.badge {
    display: inline-block;
    border-radius: 20px;
    padding: 5px 16px;
    font-size: 0.78rem;
    font-weight: 500;
    margin: 4px;
    border: 1px solid;
}
.badge-blue  { background: rgba(0,102,204,0.18); color:#00BFFF; border-color:rgba(0,191,255,0.35); }
.badge-cyan  { background: rgba(0,229,255,0.12); color:#00E5FF; border-color:rgba(0,229,255,0.30); }
.badge-teal  { background: rgba(0,180,160,0.14); color:#00E096; border-color:rgba(0,224,150,0.30); }
.badge-orange{ background: rgba(255,154,60,0.14); color:#FF9A3C; border-color:rgba(255,154,60,0.30); }

/* ── Feature Card ── */
.feature-card {
    background: rgba(8,18,45,0.75);
    border: 1px solid rgba(0,191,255,0.14);
    border-top: 2px solid rgba(0,191,255,0.45);
    border-radius: 14px;
    padding: 22px 18px;
    text-align: center;
    height: 100%;
    transition: transform 0.22s ease, border-color 0.22s ease;
}
.feature-card:hover {
    transform: translateY(-5px);
    border-top-color: #00BFFF;
    box-shadow: 0 8px 32px rgba(0,102,204,0.25);
}
.feature-icon  { font-size: 2.1rem; }
.feature-title { font-size: 0.95rem; font-weight: 700; color: #E8F4FF; margin: 10px 0 6px; }
.feature-desc  { font-size: 0.80rem; color: #7AA8CC; line-height: 1.55; }

/* ── Workflow Step ── */
.workflow-step {
    background: rgba(8,18,45,0.6);
    border-left: 3px solid #00BFFF;
    border-radius: 10px;
    padding: 14px 18px;
    margin: 6px 0;
    transition: background 0.2s;
}
.workflow-step:hover { background: rgba(0,102,204,0.14); }
.workflow-num {
    background: #00BFFF;
    color: #060B18;
    font-weight: 800;
    font-size: 0.72rem;
    border-radius: 50%;
    width: 20px; height: 20px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-right: 8px;
}
.workflow-title { font-size: 0.93rem; font-weight: 600; color: #E8F4FF; }
.workflow-desc  { font-size: 0.80rem; color: #7AA8CC; margin-top: 4px; }

/* ── Insight Box ── */
.insight-box {
    background: rgba(0,102,204,0.10);
    border: 1px solid rgba(0,191,255,0.15);
    border-left: 3px solid #00BFFF;
    border-radius: 10px;
    padding: 13px 18px;
    margin: 6px 0;
    color: #C8E0FF;
    font-size: 0.88rem;
    line-height: 1.55;
}

/* ── Problem Card ── */
.problem-card {
    background: rgba(8,18,45,0.65);
    border-left: 3px solid #FF4D6D;
    border-radius: 10px;
    padding: 15px 18px;
    margin: 6px 0;
}

/* ── Dataset Info Card ── */
.dataset-card {
    background: rgba(8,18,45,0.75);
    border: 1px solid rgba(0,191,255,0.13);
    border-top: 2px solid #00E5FF;
    border-radius: 12px;
    padding: 18px;
}

/* ── Stat row ── */
.stat-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid rgba(0,191,255,0.08);
    font-size: 0.85rem;
}
.stat-row:last-child { border-bottom: none; }
.stat-key   { color: #7AA8CC; }
.stat-val   { color: #00BFFF; font-weight: 600; }

/* ── Divider ── */
hr { border-color: rgba(0,191,255,0.12) !important; margin: 18px 0 !important; }

/* ── Tables ── */
.stDataFrame { background: rgba(10,24,60,0.6) !important; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(6,11,24,0.8);
    border-radius: 10px;
    padding: 4px;
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    color: #7AA8CC !important;
    font-weight: 500;
    padding: 6px 18px !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(0,102,204,0.35) !important;
    color: #00BFFF !important;
    font-weight: 700;
}

/* ── Buttons ── */
.stDownloadButton > button, .stButton > button {
    background: linear-gradient(135deg, #0066CC, #0099FF) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    transition: opacity 0.2s, transform 0.2s !important;
}
.stDownloadButton > button:hover, .stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

/* ── Select / Input ── */
.stSelectbox > div, .stMultiselect > div {
    background: rgba(10,24,60,0.7) !important;
    border-color: rgba(0,191,255,0.2) !important;
    color: #E8F4FF !important;
}

/* ── Metric ── */
[data-testid="stMetric"] {
    background: rgba(10,24,60,0.6);
    border: 1px solid rgba(0,191,255,0.14);
    border-radius: 12px;
    padding: 14px 16px;
}
[data-testid="stMetricValue"] { color: #00BFFF !important; font-weight: 800 !important; }
[data-testid="stMetricDelta"] { color: #00E096 !important; }

/* ── Alert / Info ── */
.stAlert, .stInfo { border-radius: 10px !important; border-left: 3px solid #00BFFF !important; }

/* ── Footer ── */
.rp-footer {
    text-align: center;
    color: #3E6080;
    font-size: 0.75rem;
    padding: 14px 0 4px;
    border-top: 1px solid rgba(0,191,255,0.08);
    margin-top: 24px;
}
</style>
"""

# ── Sidebar HTML ──────────────────────────────────────────────────────────────
SIDEBAR_HTML = """
<div style='text-align:center; padding:16px 0 10px;'>
  <div style='font-size:2.6rem; filter:drop-shadow(0 0 12px #00BFFF88);'>🛒</div>
  <div style='font-size:1.25rem; font-weight:800; color:#E8F4FF; margin-top:6px;
              letter-spacing:-0.5px;'>RetailPulse</div>
  <div style='font-size:0.72rem; color:#00BFFF; font-weight:600;
              text-transform:uppercase; letter-spacing:0.12em;'>
    AI Analytics Platform
  </div>
</div>
<div style='height:1px; background:linear-gradient(90deg,transparent,rgba(0,191,255,0.35),transparent);
            margin:12px 0;'></div>
"""

SIDEBAR_FOOTER = """
<div style='margin-top:20px; padding:12px 14px;
            background:rgba(0,102,204,0.08);
            border:1px solid rgba(0,191,255,0.1);
            border-radius:10px;'>
  <div style='font-size:0.72rem; color:#7AA8CC; line-height:1.8;'>
    👤 <b style='color:#C8E0FF;'>Satya Sourav Das</b><br>
    🏢 <b style='color:#C8E0FF;'>Zidio Development</b><br>
    📊 Data Science &amp; Analytics
  </div>
</div>
<div style='text-align:center; margin-top:14px; font-size:0.65rem; color:#3E6080;'>
  RetailPulse v1.0 · All data synthetic
</div>
"""
