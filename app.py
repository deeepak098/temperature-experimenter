
import json
import streamlit as st
from experiment import run_experiment

st.set_page_config(
    page_title="🌡️ Temperature Experimenter",
    page_icon="🌡️",
    layout="wide",
)

st.markdown("""
<style>
.stApp{
background:linear-gradient(135deg,#0f172a,#111827,#1e293b);
color:white;
}
.block-container{padding-top:2rem;padding-bottom:3rem;max-width:1400px;}
.hero{
text-align:center;
padding:20px;
margin-bottom:20px;
background:rgba(255,255,255,.05);
border:1px solid rgba(255,255,255,.08);
border-radius:18px;
backdrop-filter:blur(8px);
}
.hero h1{
font-size:3rem;
margin-bottom:.2rem;
}
.hero p{color:#cbd5e1;font-size:1.1rem;}
.temp-card{
padding:12px;
border-radius:14px;
text-align:center;
font-weight:bold;
margin-bottom:10px;
color:white;
}
.blue{background:#2563eb;}
.purple{background:#7c3aed;}
.orange{background:#ea580c;}
.response{
background:#1e293b;
border:1px solid #334155;
border-radius:12px;
padding:12px;
margin-bottom:15px;
}
.small{color:#94a3b8;font-size:.9rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>🌡️ Temperature Experimenter</h1>
<p>Run the <b>same prompt</b> five times at three different temperatures and compare how creativity changes.</p>
</div>
""", unsafe_allow_html=True)

examples = [
    "Write a funny story about a dragon.",
    "Describe Earth from an alien's perspective.",
    "Write a pirate bedtime story.",
    "Invent a new superhero."
]

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

cols = st.columns(len(examples))
for c, ex in zip(cols, examples):
    if c.button(ex, use_container_width=True):
        st.session_state.prompt = ex

prompt = st.text_area(
    "📝 Prompt",
    value=st.session_state.prompt,
    height=180,
    placeholder="Enter any creative writing prompt..."
)

run = st.button("🚀 Run Experiment", use_container_width=True)

if run:
    if not prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()

    progress = st.progress(0)
    with st.spinner("Generating 15 responses..."):
        progress.progress(20)
        results = run_experiment(prompt)
        progress.progress(100)

    st.success("✅ Experiment Completed!")

    total = sum(len(v) for v in results.values())

    a,b,c = st.columns(3)
    a.metric("Temperatures", "3")
    b.metric("Responses", total)
    c.metric("Prompt Length", len(prompt))

    st.divider()

    headers = [
        ("❄️ Low Creativity","0.2","blue"),
        ("⚖️ Balanced","0.7","purple"),
        ("🔥 High Creativity","1.4","orange"),
    ]

    cols = st.columns(3)

    for col,(title,temp,css) in zip(cols,headers):
        with col:
            st.markdown(
                f"<div class='temp-card {css}'>{title}<br><span style='font-size:28px'>{temp}</span></div>",
                unsafe_allow_html=True
            )

            for i,text in enumerate(results[float(temp)],1):
                st.markdown(f"<div class='response'><b>Response {i}</b></div>", unsafe_allow_html=True)
                st.code(text, language=None)

    export = {
        str(k):v for k,v in results.items()
    }

    st.download_button(
        "📥 Download Results",
        data=json.dumps(export, indent=2),
        file_name="temperature_experiment_results.json",
        mime="application/json",
        use_container_width=True
    )

st.markdown(
"<hr><div class='small' style='text-align:center'>Built with Streamlit • Groq • Llama</div>",
unsafe_allow_html=True)
