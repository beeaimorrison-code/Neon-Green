import streamlit as st
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Beeai Morrison | Strategic Architect", page_icon="⚡", layout="wide")

# --- 2. CUSTOM THEME (BLUE, WHITE, NEON GREEN) ---
st.markdown("""
    <style>
    /* Light Blue to White Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #ffffff 100%);
        color: #1e293b;
    }
    
    /* Sidebar: Deep Navy Blue */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        color: #ffffff;
    }
    
    /* Neon Green Accented Cards */
    .glass-card {
        background: #ffffff;
        border: 2px solid #22c55e; /* Neon Green */
        border-radius: 24px;
        padding: 32px;
        transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        box-shadow: 0 10px 15px -3px rgba(34, 197, 94, 0.1);
    }
    
    .glass-card:hover {
        transform: translateY(-8px);
        border-color: #3b82f6; /* Switches to Blue on hover */
        box-shadow: 0 20px 25px -5px rgba(59, 130, 246, 0.2);
    }
    
    .hero-name {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -1px;
    }
    
    .neon-text {
        color: #22c55e;
        font-weight: bold;
    }

    .process-step {
        color: #3b82f6;
        font-weight: bold;
        font-size: 1.4rem;
        display: flex;
        align-items: center;
    }
    
    .process-step::before {
        content: '';
        display: inline-block;
        width: 12px;
        height: 12px;
        background-color: #22c55e;
        border-radius: 50%;
        margin-right: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR / DP LOGIC (SMART SEARCH) ---
with st.sidebar:
    st.markdown("<h3 style='color: #22c55e;'>Digital Identity</h3>", unsafe_allow_html=True)
    
    # Check for DP (PNG, JPG, or JPEG)
    if os.path.exists("profile.png"):
        st.image("profile.png", use_container_width=True)
    elif os.path.exists("profile.jpg"):
        st.image("profile.jpg", use_container_width=True)
    elif os.path.exists("profile.jpeg"):
        st.image("profile.jpeg", use_container_width=True)
    else:
        st.info("Upload 'profile.png' or 'profile.jpg' to GitHub.")
    
    st.markdown("---")
    st.markdown("<p style='color: #22c55e;'>🟢 <b>System Status: Active</b></p>", unsafe_allow_html=True)
    st.caption("Strategic Consultancy Available.")
    st.divider()
    
    st.markdown("<h4 style='color: #22c55e;'>The Philosophy</h4>", unsafe_allow_html=True)
    st.write("Ensuring that technical systems don't just function—they command attention and deliver results.")

# --- 4. HERO SECTION ---
col_h1, col_h2 = st.columns([2, 1])

with col_h1:
    # UPDATED: Name in Title Case
    st.markdown('<h1 class="hero-name" style="font-size: 4rem; margin-bottom:0;">Beeai Morrison</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #3b82f6; margin-top:0;">Technical Rigor & <span class="neon-text">Creative Conversion</span></h3>', unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"""
        <p style="font-size: 1.2rem; line-height: 1.7; font-style: italic; color: #475569;">
            "My approach aligns the rigors of standard academic research with the unique requirements 
            of specific projects. I provide strategic support for M.Sc. and B.Sc. candidates, 
            ensuring that theses, dissertations, and high-level technical assignments meet 
            institutional demands while maintaining the creative edge of the project's vision."
        </p>
    """, unsafe_allow_html=True)

# --- 5. THE THREE CORE PILLARS ---
st.write("##")
p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""<div class="glass-card">
        <h3 style="color: #3b82f6;">🎓 Academic Rigor</h3>
        <p>Strategic guidance for high-stakes research. Aligning unique project visions with the strict demands of institutional boards.</p>
    </div>""", unsafe_allow_html=True)

with p2:
    st.markdown("""<div class="glass-card">
        <h3 style="color: #22c55e;">✍️ Direct-Response</h3>
        <p>Engineering communication frameworks and video scripts for health, tech, and lifestyle brands that trigger action.</p>
    </div>""", unsafe_allow_html=True)

with p3:
    st.markdown("""<div class="glass-card">
        <h3 style="color: #3b82f6;">📈 Systematic SEO</h3>
        <p>Data-driven visibility. Crafting metadata architecture that ensures visionary content is discovered, ranked, and valued.</p>
    </div>""", unsafe_allow_html=True)

# --- 6. THE METHODOLOGY ---
st.write("##")
st.write("---")
st.markdown("<h2 style='color: #0f172a;'>The Methodology</h2>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)

with m1:
    st.markdown('<p class="process-step">01. Discovery</p>', unsafe_allow_html=True)
    st.write("Mapping the rigors of your specific academic or brand requirements to establish a solid foundation.")

with m2:
    st.markdown('<p class="process-step">02. Engineering</p>', unsafe_allow_html=True)
    st.write("Building the system with technical precision and architectural integrity.")

with m3:
    st.markdown('<p class="process-step">03. Calibration</p>', unsafe_allow_html=True)
    st.write("Final optimization for institutional defense or global search engine visibility.")

# --- 7. CONNECT HUB (Direct Contact Section) ---
st.write("##")
st.write("---")
st.markdown("<h2 style='text-align: center; color: #0f172a;'>Get In Touch</h2>", unsafe_allow_html=True)

# Centering the contact buttons
c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])

with c2:
    st.markdown("""
        <div style="text-align: center;">
            <a href="mailto:beeaimorrison@gmail.com" target="_blank">
                <img src="https://img.icons8.com/ios-filled/50/3b82f6/gmail.png" width="45">
                <p style="color: #3b82f6; font-size: 0.9rem; margin-top: 5px; font-weight: bold;">Email</p>
            </a>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://wa.me/2348108397680" target="_blank">
                <img src="https://img.icons8.com/ios-filled/50/22c55e/whatsapp.png" width="45">
                <p style="color: #22c55e; font-size: 0.9rem; margin-top: 5px; font-weight: bold;">WhatsApp</p>
            </a>
        </div>
    """, unsafe_allow_html=True)

# --- 8. FINAL FOOTER ---
st.write("##")
st.markdown("<p style='text-align: center; color: #94a3b8; margin-top: 50px;'>© 2026 Beeai Morrison | Strategic Execution</p>", unsafe_allow_html=True)
