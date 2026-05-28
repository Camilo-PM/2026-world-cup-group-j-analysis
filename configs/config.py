from pathlib import Path

# ======================================
# BASE PATHS
# ======================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
FINAL_DIR = DATA_DIR / "final"

HTML_DIR = RAW_DIR / "html"

REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# ======================================
# SETTINGS
# ======================================

LAST_N_MATCHES = 10

# ======================================
# TEAMS
# ======================================

TEAMS = {
    "Algeria": [
        HTML_DIR / "algeria.html",
        HTML_DIR / "algeria_2025.html",
    ],

    "Argentina": [
        HTML_DIR / "argentina.html",
        HTML_DIR / "argentina_2025.html",
    ],

    "Austria": [
        HTML_DIR / "austria.html",
        HTML_DIR / "austria_2025.html",
    ],

    "Jordan": [
        HTML_DIR / "jordan.html",
        HTML_DIR / "jordan_2025.html",
    ],
}

# ======================================
# OUTPUT FILES
# ======================================

RAW_MATCHES_FILE = RAW_DIR / "group_j_last_10_raw.csv"

CLEAN_MATCHES_FILE = (
    PROCESSED_DIR / "group_j_last_10_clean.csv"
)

SUMMARY_FILE = FINAL_DIR / "group_j_summary.csv"

TABLEAU_FILE = FINAL_DIR / "group_j_tableau.csv"