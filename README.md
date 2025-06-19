# 🕸️ AI Web Scraper with Ollama + Streamlit

This project is an AI-powered web scraping and parsing tool built with **Streamlit**, **Selenium**, **BeautifulSoup**, and **Ollama (LLaMA 3)**. It allows users to scrape a webpage, clean its content, and query it using natural language instructions.

---

## 🚀 Features

* ✅ Scrapes any public website using **Selenium**
* ✅ Cleans and extracts only the useful textual content using **BeautifulSoup**
* ✅ Uses **LLaMA 3 via Ollama** to parse DOM content based on user-defined queries
* ✅ Simple, interactive UI powered by **Streamlit**

---

## 🧠 How It Works

1. **User inputs a website URL**
2. **Selenium** launches a headless Chrome browser and scrapes the HTML content
3. **BeautifulSoup** extracts and cleans the `<body>` content
4. The cleaned content is split into chunks
5. Each chunk is sent to **LLaMA 3 (via LangChain + Ollama)** for parsing based on a natural language prompt
6. Parsed results are returned and displayed in the UI

---

## 🧰 Requirements

* Python 3.9+
* [Ollama](https://ollama.com) installed locally with `llama3` model pulled
* Google Chrome + compatible `chromedriver`

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## 🧠 Setup LLaMA 3 with Ollama

1. Install [Ollama](https://ollama.com)
2. Run this command to download the model:

```bash
ollama pull llama3
```

3. Keep Ollama running:

```bash
ollama serve
```

---

## 🖥️ Run the App

```bash
streamlit run main.py
```

---

## 📁 Project Structure

```
ai-web-scraper/
├── main.py             # Streamlit frontend
├── parse.py            # Ollama-based parsing logic
├── scrape.py           # Web scraping and cleaning logic
├── requirements.txt
└── README.md
```

---

## ✍️ Example Prompts

* `Extract all product titles from the page.`
* `List all headings (h1, h2, h3).`
* `Get all the contact emails or phone numbers.`
* `Find the text under the 'About Us' section.`

---

## ⚠️ Limitations

* Cannot bypass CAPTCHA-protected or login-restricted sites
* LLM output is only as good as the quality of the DOM content and prompt
* Heavy websites may take longer to scrape

---

## 📃 License

MIT License. Feel free to use, modify, and share!

---

## 🙌 Acknowledgments

* [Streamlit](https://streamlit.io)
* [Selenium](https://www.selenium.dev/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [LangChain](https://www.langchain.com/)
* [Ollama](https://ollama.com)
