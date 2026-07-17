# 🌡️ Temperature Experimenter

A Streamlit application that demonstrates how the **temperature parameter** affects the creativity, diversity, and consistency of Large Language Models (LLMs).

Instead of explaining temperature theoretically, this project lets you **see the difference** by sending the **same prompt** to an LLM **15 times**:

* **5 responses at Temperature = 0.2**
* **5 responses at Temperature = 0.7**
* **5 responses at Temperature = 1.4**

The results are displayed side by side, making it easy to compare how model behavior changes as temperature increases.

---

## 🚀 Features

* 🌡️ Compare three temperature settings simultaneously
* 🔁 Generate 15 responses from the same prompt
* 🎨 Modern Streamlit interface
* 📊 Side-by-side comparison layout
* ⚡ Fast response generation using the Groq API
* 📥 Download experiment results as JSON
* 💡 One-click sample prompts
* 🌙 Clean dark-themed UI

---

## 📸 Preview

```
🌡️ Temperature Experimenter

Prompt
────────────────────────────────────────

Write a story about a dragon.

[ Run Experiment ]

────────────────────────────────────────

❄️ Temperature 0.2      ⚖️ Temperature 0.7      🔥 Temperature 1.4

Response 1              Response 1              Response 1

Response 2              Response 2              Response 2

Response 3              Response 3              Response 3

Response 4              Response 4              Response 4

Response 5              Response 5              Response 5
```

---

# 📂 Project Structure

```
temperature-experimenter/

├── app.py
├── experiment.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠️ Technologies Used

* Python
* Streamlit
* Groq API
* Llama 3.3 70B Versatile
* python-dotenv

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/your-username/temperature-experimenter.git

cd temperature-experimenter
```

---

## Create a virtual environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

Get your free API key from Groq and replace the placeholder with your own key.

---

# ▶️ Run the application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

# 🧠 How It Works

1. The user enters a creative writing prompt.
2. The application sends the same prompt to the LLM.
3. The prompt is generated:

   * 5 times at **0.2**
   * 5 times at **0.7**
   * 5 times at **1.4**
4. All 15 responses are displayed side by side.
5. Users can compare how creativity and randomness change with temperature.

---

# 📖 What You'll Learn

This project demonstrates several important LLM and Python concepts:

* Calling an LLM API
* Prompt engineering
* Temperature tuning
* Loops
* Functions
* Dictionaries
* Lists
* Environment variables
* Streamlit UI development
* Displaying structured experimental results

---

# 🌡️ Understanding Temperature

| Temperature | Behavior                                                     |
| ----------- | ------------------------------------------------------------ |
| **0.2**     | More deterministic, consistent, and predictable responses    |
| **0.7**     | Balanced creativity and coherence                            |
| **1.4**     | Highly creative, diverse, and sometimes unexpected responses |

---

# 🎯 Learning Objective

The goal of this project is to provide a practical understanding of how the **temperature** parameter influences text generation. By comparing multiple outputs side by side, users can observe the effects directly instead of relying on theoretical explanations.

---

# 🚀 Future Improvements

* Support multiple LLMs
* Adjustable temperature slider
* Adjustable number of generations
* Export to Markdown or PDF
* Token usage statistics
* Response generation time
* Side-by-side diff view
* Markdown rendering
* Prompt history
* Experiment history

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project helpful, consider giving it a star!