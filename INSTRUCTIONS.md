# 🚀 Llama 2 Chatbot Installation & Usage Guide

This guide provides step-by-step instructions to **run the ChatBot** in your Windows system for the **Llama 2 Model** from this repository:  
**`Retail-QnA-Chatbot-LLaMA2-GPT2/Llama 2 Model`**

---

## **1️⃣ Download the Model from Google Drive**

1. Go to **https://drive.google.com/drive/folders/171I3cCbr3BONz7w71wA8_349xP-ACFOJ?usp=sharing**
2. Download **all model files**:  
   - `model.safetensors`  
   - `config.json`  
   - `tokenizer.json`  
3. **If the download is a zip, extract it.**

💡 *Tip: Keep all model files in a single folder for easier setup.*

---

## **2️⃣ Install Python 3.10**

1. Download Python 3.10 from:  
   👉 https://www.python.org/downloads/release/python-3100/  
2. Run the installer.  

---

## **3️⃣ Setup Project in VS Code**

1. Open **VS Code**.  
2. Open the **Terminal** → `Terminal → New Terminal`.  

---

## **4️⃣ Create and Activate a Virtual Environment**

Run the following commands in **VS Code terminal**:  

C:\Users\XYZ\AppData\Local\Programs\Python\Python310\python.exe -m venv .venv

.venv\Scripts\activate

## **5️⃣ Clone the Project Repository
git clone https://github.com/umerulla/Retail-QnA-Chatbot-LLaMA2-GPT2.git
cd "Retail-QnA-Chatbot-LLaMA2-GPT2/Llama 2 Model"


## ** 6️⃣ Install Python Dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements_for_windows.txt


## **7️⃣ Place All Model Files
Retail-QnA-Chatbot-LLaMA2-GPT2/Llama 2 Model/llama2-final

Files should include:
model.safetensors
config.json
tokenizer.json
(any additional model files)

## **8️⃣ Set the Model Path in runbot.py
Open runbot.py in VS Code.
At the top, set the model path like this:
model_path = r"C:/FULL/PATH/TO/Retail-QnA-Chatbot-LLaMA2-GPT2/Llama 2 Model/llama2-final"
💡 Replace with your actual absolute path.

## **9️⃣ Run the Chatbot
python runbot.py


## **🔟 Usage Notes
⏳ CPU Execution: Responses may take 2–4+ minutes based on your PC Ram and processor





