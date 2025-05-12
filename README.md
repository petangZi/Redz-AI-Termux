# 🤖 **Redz AI Coder Assistant – Offline GPT for Code Generation**

AI assistant lokal tanpa batas yang bisa bantu generate kode kompleks kayak:
- 💻 **Website** (HTML/CSS/JS/PHP)
- 🐍 **Python script** (tools, RAT, backdoor)
- ☠️ **Exploit & reverse shell** (etis only)
- ⚔️ Dan semua ide gila coding lo

Tanpa API, 100% **offline**, tanpa sensor. Bebas prompt sampe puas 🧠

---

## 📸 **Tampilan UI**
🧠 **Masukin prompt coding lo:**

Contoh: bikinkan aku ddos
```plaintext
bikinin aku web portofolio yang aesthetic

#🔧 Cara Install Redz AI Coder Assistant
-Install via Termux (Android)

-Update dan install dependencies:

pkg update -y
pkg install git python clang wget -y
-Clone repo:

git clone https://github.com/USERNAME/Redz-AI-Termux.git
cd Redz-AI-Termux
Jalankan script setup.sh untuk instalasi otomatis:

bash setup.sh
📦 Model AI akan otomatis di-download (~1.2GB) ke folder models/
-setalah itu
python main.py
#Install via PC (Windows/Linux)
Clone repo:

git clone https://github.com/USERNAME/Redz-AI-Termux.git
cd Redz-AI-Termux
-Buat virtualenv (opsional tapi disarankan untuk manajemen dependensi):

python -m venv env
source env/bin/activate   # Linux
env\Scripts\activate      # Windows
-Install dependencies:

pip install -r requirements.txt
Download model AI (WizardCoder 1.5B):

mkdir models
cd models
wget -O WizardCoder.gguf https://huggingface.co/TheBloke/WizardCoder-1.0-1.5B-GGUF/resolve/main/WizardCoder-1.0-1.5B.Q4_K_M.gguf
cd ..
5. Jalankan asisten AI-nya:

python main.py
