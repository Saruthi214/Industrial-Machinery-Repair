import json
import streamlit as st
from PIL import Image
from ultralytics import YOLO

# ---------- Page config ----------
st.set_page_config(
    page_title="Industrial Machinery Repair Assistant",
    page_icon="🔧",
    layout="wide",
)

# ---------- Styles ----------
st.markdown("""
<style>
:root {
    --bg:#12161d; --card:#1a2029; --border:#2a3240;
    --text:#eaecef; --muted:#8b95a7;
    --primary:#f5a524; --accent:#3bc9db;
    --success:#22c55e; --warning:#eab308; --danger:#ef4444;
}
.stApp { background: var(--bg); color: var(--text); }
section[data-testid="stSidebar"] { background:#151a22; }
h1,h2,h3,h4 { color: var(--text) !important; }
.block-container { padding-top: 2rem; max-width: 1200px; }

.hero-badge{
    display:inline-flex;align-items:center;gap:6px;
    background:#1a2029;border:1px solid var(--border);
    padding:4px 10px;border-radius:999px;font-size:12px;color:var(--muted);
}
.hero-title{ font-size:44px;font-weight:800;line-height:1.1;margin:14px 0 8px; }
.hero-grad{
    background: linear-gradient(90deg,var(--primary),var(--accent));
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.hero-sub{ color:var(--muted);max-width:640px;margin-bottom:24px; }

.card{
    background:var(--card);border:1px solid var(--border);
    border-radius:12px;padding:20px;margin-bottom:18px;
}
.card-title{ font-size:14px;font-weight:600;color:var(--text);margin-bottom:12px; }

.sev{
    display:inline-flex;align-items:center;gap:6px;
    padding:4px 10px;border-radius:999px;font-size:12px;font-weight:600;
    border:1px solid;
}
.sev-Low{ color:var(--success);background:rgba(34,197,94,.12);border-color:rgba(34,197,94,.35);}
.sev-Medium{color:var(--warning);background:rgba(234,179,8,.12);border-color:rgba(234,179,8,.35);}
.sev-High{  color:var(--danger); background:rgba(239,68,68,.12);border-color:rgba(239,68,68,.4);}
.sev-Critical{color:var(--danger);background:rgba(239,68,68,.2); border-color:rgba(239,68,68,.6);}

.meter-wrap{background:#0f141b;border-radius:999px;height:8px;overflow:hidden;}
.meter-fill{height:100%;background:linear-gradient(90deg,var(--primary),var(--accent));border-radius:999px;}

.step{
    display:flex;gap:12px;align-items:flex-start;
    background:rgba(255,255,255,.03);border:1px solid var(--border);
    border-radius:8px;padding:10px 12px;margin-bottom:8px;font-size:14px;
}
.step-num{
    flex:0 0 24px;height:24px;border-radius:999px;
    background:rgba(245,165,36,.15);color:var(--primary);
    display:flex;align-items:center;justify-content:center;
    font-weight:700;font-size:12px;border:1px solid rgba(245,165,36,.35);
}
.prev-item{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:var(--muted);margin-bottom:6px;}
.check{color:var(--success);font-weight:800;}

.stButton>button{
    background:var(--primary)!important;color:#1a1206!important;
    border:none!important;font-weight:600!important;border-radius:8px!important;
    padding:.55rem 1.1rem!important;
}
.stButton>button:hover{ filter:brightness(1.08); }
[data-testid="stFileUploader"] section{
    background:var(--card);border:1px dashed var(--border);border-radius:12px;
}
/* Upload button */
[data-testid="stFileUploader"] button{
    background-color: #F5A524 !important;
    color: black !important;
    border: 1[px solid white!important;
}

/* Upload button text */
[data-testid="stFileUploader"] button *{
    color: black !important;
}
[data-testid="stFileUploaderFileInfo"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ---------- Load model & guide ----------
@st.cache_resource
def load_model():
    return YOLO("runs/detect/train/weights/best.pt")

@st.cache_data
def load_guide():
    with open("repair_guide.json", "r") as f:
        return json.load(f)

model = load_model()
repair_data = load_guide()

# ---------- Header ----------
st.markdown("""
<div class="hero-badge">✨ AI vision inspection</div>
<div class="hero-title">Detect welding defects.<br>
  <span class="hero-grad">Get repair steps in seconds.</span>
</div>
<div class="hero-sub">Upload a photograph of your weld. The model identifies the defect class,
rates severity, and returns a certified repair and prevention protocol.</div>
""", unsafe_allow_html=True)

# ---------- Layout ----------
left, right = st.columns([1.1, 1])

with left:
    st.markdown('<div class="card"><div class="card-title">🖼️ Weld image</div>',
                unsafe_allow_html=True)
    uploaded = st.file_uploader(
        "Upload welding image", type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )
    if uploaded:
        image = Image.open(uploaded)
        st.image(image, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    detect = st.button("🔍  Detect Defect", disabled=not uploaded, use_container_width=False)

    # trained classes chips
    chips = "".join(
        f'<span class="sev sev-{d["severity"]}" style="margin:4px 6px 0 0;">{n}</span>'
        for n, d in repair_data.items()
    )
    st.markdown(f'<div class="card"><div class="card-title">Trained defect classes</div>{chips}</div>',
                unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if not uploaded:
        st.markdown("""
        <div style="text-align:center;padding:60px 10px;color:var(--muted);">
          <div style="font-size:36px;">🔎</div>
          <div style="font-weight:600;color:var(--text);margin-top:8px;">Awaiting analysis</div>
          <div style="font-size:13px;margin-top:6px;">
            Upload an image and press <b>Detect Defect</b>.
          </div>
        </div>
        """, unsafe_allow_html=True)

    elif detect:
        with st.spinner("Running inference…"):
            results = model.predict(image)
            result = results[0]

        if len(result.boxes) == 0:
            st.markdown("""
            <div style="text-align:center;padding:60px 10px;">
              <div style="font-size:40px;color:var(--success);">✔</div>
              <div style="font-weight:700;font-size:18px;margin-top:6px;">No defect detected</div>
              <div style="color:var(--muted);font-size:13px;">Weld looks clean.</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            class_id  = int(result.boxes.cls[0])
            confidence = float(result.boxes.conf[0])
            defect     = model.names[class_id]
            info       = repair_data.get(defect)
            severity   = info["severity"] if info else "Low"

            st.markdown(f"""
            <div style="font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);">
              Detected defect
            </div>
            <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:6px 0 16px;">
              <div style="font-size:28px;font-weight:800;">{defect}</div>
              <span class="sev sev-{severity}">● {severity} severity</span>
            </div>
            <div style="background:#0f141b;border:1px solid var(--border);
                 border-radius:10px;padding:12px 14px;margin-bottom:18px;">
              <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:6px;">
                <span style="color:var(--muted);">Model confidence</span>
                <span style="font-family:monospace;">{confidence*100:.2f}%</span>
              </div>
              <div class="meter-wrap"><div class="meter-fill" style="width:{confidence*100:.1f}%;"></div></div>
            </div>
            """, unsafe_allow_html=True)

            if info:
                st.markdown(f"""
                <div class="card-title">⚠️ Cause</div>
                <div style="color:var(--muted);font-size:14px;margin-bottom:16px;">{info['cause']}</div>
                """, unsafe_allow_html=True)

                st.markdown('<div class="card-title">🔧 Repair Steps</div>', unsafe_allow_html=True)
                for i, step in enumerate(info["repair"], 1):
                    st.markdown(
                        f'<div class="step"><div class="step-num">{i}</div><div>{step}</div></div>',
                        unsafe_allow_html=True,
                    )

                st.markdown('<div class="card-title" style="margin-top:14px;">🛡️ Prevention</div>',
                            unsafe_allow_html=True)
                for step in info["prevention"]:
                    st.markdown(
                        f'<div class="prev-item"><span class="check">✔</span><span>{step}</span></div>',
                        unsafe_allow_html=True,
                    )
    else:
        st.markdown("""
        <div style="text-align:center;padding:60px 10px;color:var(--muted);">
          <div style="font-weight:600;color:var(--text);">Ready to analyze</div>
          <div style="font-size:13px;margin-top:6px;">Press <b>Detect Defect</b>.</div>
        </div>
        """, unsafe_allow_html=True)

analysis = st.container()

with analysis:
    st.markdown(
        """
        <div class="card">
        """,
        unsafe_allow_html=True,
    )

    # all your analysis code here

    st.markdown("</div>", unsafe_allow_html=True)
