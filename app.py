import streamlit as st
from experiment import run_experiment

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Temperature Experimenter",
    page_icon="🌡️",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    color: #BBBBBB;
    font-size: 18px;
    margin-bottom: 30px;
}

.response-card {
    background-color: #1B1F2A;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #333;
    margin-bottom: 15px;
}

.temp-header{
    text-align:center;
    font-size:28px;
    font-weight:bold;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown(
    '<div class="title">🌡️ Temperature Experimenter</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Send the same prompt 5 times at three different temperatures and compare the outputs.'
    '</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# Prompt Input
# -------------------------------------------------

prompt = st.text_area(
    "Enter your prompt",
    height=180,
    placeholder="Example: Write a mysterious story about a lighthouse..."
)

# -------------------------------------------------
# Button
# -------------------------------------------------

if st.button("🚀 Run Experiment", use_container_width=True):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
        st.stop()

    with st.spinner("Generating 15 responses..."):

        try:
            results = run_experiment(prompt)

        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

    st.success("Experiment completed!")

    st.divider()

    # ---------------------------------------------
    # Three Columns
    # ---------------------------------------------

    col1, col2, col3 = st.columns(3)

    temperatures = [0.2, 0.7, 1.4]
    columns = [col1, col2, col3]

    for column, temp in zip(columns, temperatures):

        with column:

            st.markdown(
                f"<div class='temp-header'>🌡️ Temperature {temp}</div>",
                unsafe_allow_html=True
            )

            for i, response in enumerate(results[temp], start=1):

                st.markdown(f"### Response {i}")

                st.code(response, language=None)

                st.markdown("---")