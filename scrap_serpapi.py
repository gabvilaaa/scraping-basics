from serpapi import GoogleSearch
import json
import tkinter as tk
from tkinter import scrolledtext

# Search on Serpapi
def pesquisa():
    termo_pesquisa = entrada.get()  # Get the seach term
    params = {
        "q": termo_pesquisa,
        "location": "Brazil",
        "hl": "pt",
        "google_domain": "google.com.br",
        "api_key": ""    #get your own API token on serpapi.com
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Save on JSON
    with open('resultados_google.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

# Function to see the JSON on tkinter text container
def show():
    with open('resultados_google.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    formatted_data = json.dumps(data, ensure_ascii=False, indent=4)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.INSERT, formatted_data)

# Window creation
root = tk.Tk()
root.title("Busca no Google com SerpAPI")

# Input
entrada = tk.Entry(root, width=50, font=("Arial", 12))
entrada.pack(pady=10)

# Button to search
botao_busca = tk.Button(root, text="Buscar", command=pesquisa)
botao_busca.pack(pady=10)

# Scroll
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30, font=("Times New Roman", 10))
text_area.pack(padx=10, pady=10)

# Load JSON
botao = tk.Button(root, text="Carregar e Mostrar JSON", command=show)
botao.pack(pady=10)

# Run app
root.mainloop()



