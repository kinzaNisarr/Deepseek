# **🧠 DeepSeek Chatbot**  
🚀 **AI-Powered Coding Assistant** using **DeepSeek** models via **Ollama** & **LangChain**  

## **📌 Overview**  
This project implements an **AI chatbot** that assists with **coding, debugging, and solution design** using **DeepSeek models (1.5B & 7B parameters)**. The chatbot is built with **Streamlit**, integrates with **Ollama**, and leverages **LangChain** for AI-driven conversations.  

## **⚙️ Features**  
✅ **Runs Locally** – No external API needed.  
✅ **Code Debugging** – AI suggests debugging strategies.  
✅ **Python Expertise** – AI helps with Python solutions.  
✅ **Interactive Chat** – Streamed responses for better UX.  
✅ **Customizable** – Choose between **DeepSeek 1.5B & 7B** models.  

## **📥 Installation**  

### **1️⃣ Install Ollama**  
Ollama is required to run DeepSeek models locally.  

**For macOS & Linux:**  
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
**For Windows:**  
[Download & Install Ollama](https://ollama.com/download)  

Verify installation:  
```bash
ollama --version
```

---

### **2️⃣ Download DeepSeek Model**  
Run the following command to pull the DeepSeek model:  
```bash
ollama pull deepseek-coder:1.5b
```
or  
```bash
ollama pull deepseek-coder:7b
```

To check available models:  
```bash
ollama list
```

---

### **3️⃣ Install Python Dependencies**  
Make sure you have Python **3.8+** installed. Then install dependencies:  

```bash
pip install -r requirements.txt
```
_(If `requirements.txt` is not available, install manually)_  
```bash
pip install streamlit langchain-core langchain_ollama
```

---

### **4️⃣ Run the Chatbot Locally**  
Once everything is installed, start the chatbot with:  

```bash
streamlit run app.py
```

The chatbot will open in your **web browser**, ready to assist with coding!

---

## **📡 API Usage (Optional)**  
If you want to use DeepSeek via API, first start the Ollama server:  

```bash
ollama serve
```

Then send a request using Python:  
```python
import requests

url = "http://localhost:11434/api/generate"
data = {
    "model": "deepseek-coder:1.5b",
    "prompt": "Explain recursion in Python",
    "stream": False
}

response = requests.post(url, json=data)
print(response.json())
```

---

## **🛠️ Project Structure**  

```
📂 deepseek-chatbot
 ├── app.py                # Streamlit chatbot application
 ├── requirements.txt       # Python dependencies
 ├── README.md              # Project documentation (this file)
```

---

## **🚀 Future Enhancements**  
🔹 **Add more DeepSeek models**  
🔹 **Improve UI with advanced formatting**  
🔹 **Integrate with databases for chat history storage**  

---

## **📜 License**  
This project is **open-source** under the **MIT License**.  

---

## **📬 Contact**  
For questions or contributions, reach out via GitHub or email at kinzanisar9@gmail.com.  

