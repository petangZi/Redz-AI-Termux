from llama_cpp import Llama
from colorama import Fore, Style, init
import os
import time

# Init warna terminal
init(autoreset=True)

# Banner awal
def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(Fore.CYAN + "=" * 50)
    print(Fore.MAGENTA + " 🔧  Redz AI Coding Assistant (Offline GPT)")
    print(Fore.YELLOW + " 💬  Ketik ide coding lo dan AI bakal bantuin")
    print(Fore.CYAN + "=" * 50)

# Load model (pastikan path bener!)
def load_model():
    print(Fore.BLUE + "[+] Loading model... (sabar dikit bro)")
    model = Llama(
        model_path="models/WizardCoder.gguf",
        n_ctx=2048,
        n_threads=4  # ganti sesuai core hp lu
    )
    return model

# Proses prompt user
def generate_code(llm, prompt):
    try:
        output = llm(
            f"[INST] {prompt} [/INST]",
            max_tokens=1024,
            temperature=0.7,
            top_p=0.9,
            stop=["</s>"]
        )
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return f"❌ Gagal generate: {e}"

# Main loop
def main():
    show_banner()
    llm = load_model()

    while True:
        try:
            print(Fore.LIGHTGREEN_EX + "\n🧠 Masukin prompt coding lo  ya ganzz:")
            prompt = input(Fore.LIGHTWHITE_EX + ">>> ")

            if not prompt.strip():
                print(Fore.RED + "⚠️ Prompt kosong, ketik sesuatu yaa.")
                continue

            print(Fore.LIGHTYELLOW_EX + "\n⏳ Tunggu bentar, AI mikir ya ganzz...\n")
            time.sleep(1.5)

            code_result = generate_code(llm, prompt)
            print(Fore.LIGHTBLACK_EX + "-" * 50)
            print(Fore.CYAN + code_result)
            print(Fore.LIGHTBLACK_EX + "-" * 50)

        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Keluar dari Redz AI. See you muachh!")
            break

# Eksekusi
if __name__ == "__main__":
    main()
