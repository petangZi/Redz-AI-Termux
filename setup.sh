#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Updating Termux..."
pkg update -y && pkg upgrade -y

echo "[*] Installing dependencies..."
pkg install -y git python clang wget

echo "[*] Installing Python libraries..."
pip install -r requirements.txt

echo "[*] Making model folder..."
mkdir -p models
cd models

echo "[*] Downloading AI model (1GB+)..."
wget -O WizardCoder.gguf https://huggingface.co/TheBloke/WizardCoder-1.0-1.5B-GGUF/resolve/main/WizardCoder-1.0-1.5B.Q4_K_M.gguf

cd ..

echo "[*] Starting Redz AI Assistant..."
python main.py
