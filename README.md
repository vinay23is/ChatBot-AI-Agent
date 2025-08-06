

## 🤖 ChatBot AI Agent (Ollama + Mistral)

A simple Python-based AI agent powered by [Ollama](https://ollama.ai) and the **Mistral** model. This project demonstrates how to interact with a local AI model via the command line.

---

### ✨ Features

* 💬 Simple interactive AI agent in the terminal
* ⚡ Powered by **Mistral** (via Ollama)
* 🖥 Lightweight and easy to run locally
* 🔑 Extensible for future features (API integrations, memory, tools, etc.)

---

### 🛠 Prerequisites

Before running the project, ensure you have:

* **Python 3.9+** installed
* [Ollama](https://ollama.ai) installed and running on your system
* Git (if cloning from GitHub)

---

### 📥 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/vinay23is/ChatBot-AI-Agent.git
   cd ChatBot-AI-Agent
   ```

2. **Create a virtual environment (recommended)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Mac/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Make sure Ollama is running**, and pull the Mistral model:

   ```bash
   ollama pull mistral
   ```

---

### 🚀 Usage

Run the AI agent in your terminal:

```bash
python3 agent.py
```

Example interaction:

```
🤖 Simple AI Agent (Ollama - Mistral) (type 'exit' to quit)

You: hey
Agent: Hello! How can I help you today?
You: exit
Agent: Goodbye!
```

---

### 📂 Project Structure

```
ChatBot-AI-Agent/
│
├── agent.py            # Main script for running the AI agent
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignored files
```

---

### 🔮 Future Improvements

* Add conversation history (memory)
* Integrate with APIs and tools
* Web or desktop interface
* Multiple model support

---

### 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Push and open a Pull Request

---

### 📜 License

This project is licensed under the **MIT License**.

---

Would you like me to also **add some badges (Python, Ollama, License, Stars)** at the top of your README to make it look even better? (like a professional open-source project)

