import os
import json
import requests
from time import perf_counter

# ======== CONFIGURACIÓN ========
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
DEEPSEEK_URL = os.getenv("DEEPSEEK_API_URL", "http://192.168.100.6:6900/v1/chat/completions")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-coder-v2-lite-instruct")

# ======== SESIÓN HTTP GLOBAL ========
session = requests.Session()
session.headers.update({
    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    "Content-Type": "application/json"
})

# Pool de conexiones persistentes
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10)
session.mount("http://", adapter)

# --- 4️⃣ Consulta a DeepSeek (Streaming optimizado) ---
def ask_deepseek_stream(prompt: str, temperature: float = 0.6, max_tokens: int = 1024):
    messages = [
        {"role": "user", "content": f"{prompt}"}
    ]

    payload = {
        "model": DEEPSEEK_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": True  # activamos streaming
    }

    print("💬 DeepSeek está generando respuesta...\n")
    try:
        with session.post(DEEPSEEK_URL, json=payload, stream=True, timeout=120) as resp:
            resp.raise_for_status()
            respuesta = ""
            for line in resp.iter_lines():
                if not line or not line.startswith(b"data: "):
                    continue
                data_raw = line[len(b"data: "):].decode("utf-8")
                if data_raw.strip() == "[DONE]":
                    break
                try:
                    data = json.loads(data_raw)
                    delta = data["choices"][0]["delta"].get("content", "")
                    print(delta, end="", flush=True)
                    respuesta += delta
                except Exception:
                    continue
        print("\n\n✅ Respuesta completa recibida.")
        return respuesta
    except Exception as e:
        print(f"❌ Error consultando DeepSeek: {e}")
        return ""

# ======== PROCESO PRINCIPAL ========
if __name__ == "__main__":

    while True:
        question = input("❓ Ingresa tu pregunta (o 'salir'): ").strip()
        if question.lower() in ("salir", "exit", "quit"):
            print("👋 Saliendo del asistente...")
            break

        t0 = perf_counter()

        # 3️⃣ DeepSeek Streaming
        print("------------------------------------------------------------")
        respuesta = ask_deepseek_stream(question)
        print("------------------------------------------------------------")

        print(f"⏱️ Tiempo total: {perf_counter() - t0:.2f} segundos\n")
